import base64
import json
import os
import time

import boto3
import pandas as pd
import psycopg2


def format_seconds(seconds):
    if seconds > 60:
        minutes, seconds = seconds // 60, seconds % 60
        return '%d:%02.2f minutes' % (minutes, seconds)
    return '%.2f seconds' % seconds


def read_config(config_path, env=None, decrypt=False, role=None):
    '''
    Read keys and other config options from a json file
    Assumes all values to be decrypted have key name "value", and that all keys 
    with name "value" are to be decrypted.
    Args:
      config_path (str): path to keys file
      env (str): environment key which may or may not be present in keys file
      decrypt (bool): True if some or all keys need decrytpion
      role (str): AWS role for decryption
    Returns:
      config (dict): list of key: value pairs
    '''
    with open(config_path) as f:
        config = json.load(f)
    if env is not None:
        config = {k: config[k][env] for k in config}
    if decrypt:
        assert role is not None, 'Role required in read_config to decrypt keys'
        config = decrypt_keys(config, role)
    return config


def decrypt_keys(keys_obj, role):
    # NOTE: For encrypted values, the key must be "value".  Furthermore, it is
    # assumed that all keys named "value" have encrypted values.
    for k, v in keys_obj.items():
        # base case:
        if k == 'value':
            if keys_obj.get('type', None) == 'kms':
                keys_obj[k] = decrypt(v, role)
            else:
                keys_obj[k] = v
        elif type(v) is dict:
            keys_obj[k] = {
                k2: decrypt_keys(v2 if type(v2) == dict else v2[0], role)
                for k2, v2 in v.items()}
        else:
            keys_obj[k] = v
    return keys_obj


def decrypt(encrypted, role):
    kms = boto3.client('kms')
    binary_data = base64.b64decode(encrypted)
    meta = kms.decrypt(CiphertextBlob=binary_data,
                       EncryptionContext={'source': role})
    plain_text = meta[u'Plaintext'].decode()
    return plain_text


class SQLConnector():
    def __init__(self, config, database, verbose=False):
        '''
        Args:
          - config (dict) key-value pairs with database configuration values.
              E.g.:
              {'redshift': {
                  'database': 'datawarehouse',
                  'user': 'crazy_bernie',
                  'password': '123',
                  'host': '2.cbtn-dw.redshift.us-east-1.cbtn-data-prod.local',
                  'port': '5439'}
              }
          - database (str): name of database, and primary key for <config>.
        '''
        self.database = database
        self.config = config
        db = self.config[database]
        dbname = db.get('database', db.get('secretscope'))
        user = db.get('user', db.get('username'))
        print('Connecting to %s database....' % database)
        self.conn = psycopg2.connect(dbname = dbname,
                                     host = db['host'],
                                     port = db['port'],
                                     user = user,
                                     password = db['password'])
        self.verbose = verbose
        
    def _get_config(self):
        print('Getting database configuration data...')
        with open(self.config_path + 'db.json', 'r') as readfile:
            config = json.load(readfile)
        return config

    def __del__(self):
        print('Closing connection to %s....' % self.database)
        self.conn.close()

    def _query_to_string(self, sql_filepath):
        query_string = ''
        print('Attempting to read query from %s...' % sql_filepath)
        with open(sql_filepath) as query:
            for line in query:
                query_string += line
        return query_string

    def _query_to_dataframe(self, query_string, params=None):
        if self.verbose:
            print('Query was:\n%s\nParams: %s' % (query_string, params))
        print('Querying database. '
              '(This may take a while depending on the query...)')
        dataframe = pd.read_sql_query(query_string, self.conn, params=params)
        return dataframe

    def _query_to_csv(self, query_string, outpath, params=None):
        dataframe = self._query_to_dataframe(query_string, params)
        delimiter = '\t' if 'redshift' in outpath else ','
        print('Writing csv to %s\n\n' % outpath)
        dataframe.to_csv(outpath, index=False, sep=delimiter)

    def get_data(self, query, outpath=None, query_params=None):
        ''' 
        Runs a <query> and writes the data to <outpath>

        Args: 
            inpath: str--
                EITHER:
                path to the query, stored in a .sql file (must end in '.sql')
                OR:
                a string equivalent of valid SQL
            outpath: str--
                full or relative path to write to (should end in '.csv')
                if None, returns the dataframe
            query_params: dict--
                formatted as {"placeholder": replacement, ...},
                e.g.,
                SQL Query:
                    SELECT * FROM table WHERE date < %(end_date)s;
                       
                Python code used with this class:
                    END_DATE = str(date.time.now()).split()[0] # <- "2018-05-15"
                    query_params = {"end_date": "'%s'" % END_DATE}
        '''
        t_start = time.time()
        if query.lower().endswith('.sql'):
            query_string = self._query_to_string(query)
        else:
            query_string = query
        if outpath:
            output_dir = os.path.split(outpath)[0]
            if not os.path.isdir(output_dir):
                os.makedirs(output_dir)
            self._query_to_csv(query_string, outpath, query_params)
            df = None
        else:
            df = self._query_to_dataframe(query_string, query_params)
        elapsed = time.time() - t_start
        print('Elapsed time: %s\n' % format_seconds(elapsed))
        return df

    def create_table(self, create_statement):
        '''
        Create a table in Postgres or Redshift
        @param create_statement: str:
          EITHER: a str representing a valid SQL CREATE statement
          OR: a path to a .sql file with a valid SQL CREATE statement
        '''
        create_string = (self._query_to_string(create_statement)
                         if create_statement.lower().endswith('.sql')
                         else create_statement)
        print('Creating table with command:\n%s' % create_string)
        cursor = self.conn.cursor()
        cursor.execute(create_string)
        self.conn.commit()
        cursor.close()

    def run_query(self, query, data=None):
        '''
        This method will take any CRUD operation query and execute it. Unlike 
        get_data() - this method will not return a dataFrame. By using the 
        executemany() method, we can insert or update several rows in a single 
        DB call. Just be sure to construct your query with this in mind. 

        Example of an Insert query: "INSERT INTO table_name (id, data1, data2) 
        VALUES (%s, %s, %s)" 
        
        Example of an Update query: "UPDATE table_name SET column1=%s, 
        column2=%s WHERE id=%s"
        
        Both passing in the data tuple with the values in order of the columns.

        For those queries that are deletes and do not have any params to be 
        passed in the data tuple, just be sure data is None and the method 
        will act accordingly.

        Queries this method is intended for are Inserts, Updates and Deletes. 
        It is assumed the process running this method will have the appropriate 
        permissions to perform said actions. Check with devOps if you are 
        unsure it will.
        '''
        cursor = self.conn.cursor()
        if data is None:
            cursor.execute(query)
        else:
            cursor.executemany(query, data)
            
        self.conn.commit()    
        cursor.close()

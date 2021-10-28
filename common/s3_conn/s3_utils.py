from datetime import datetime
import json
import logging
import os
import pickle
import sys
from io import BytesIO, StringIO

import boto3
import botocore
from botocore.config import Config
import pandas as pd

# NOTE: bz2 and gzip imports are buried in the Reader/Writer classes so that
# they are only imported if used (but don't forget them in your requirements.txt
# file if using!)


VERSION = '2'

# update as needed: should only require adding calls to Writer._compress and
# Reader._decompress
SUPPORTED_COMPRESSIONS = ['bz2', 'gz'] 


class S3Connector:
    def __init__(
            self, bucket_name, role=None, logger=False, acl=None):
        '''
        @params:
          bucket_name (str): Bucket name (omit s3://)
          role (str): AWS profile name: Needed for local testing; leave as None 
            if set globally by the calling process
          logger (Logger): Logger instance with (minimally) a 
            <log(level, msg)> method. Prints to stdout if False.
          acl (str): access control list that provides special cross-account 
            access typically this would have 'bucket-owner-full-control' if the
            put_object is being called from one AWS account and putting into 
            an S3 bucket in a different aws account (e.g., data to LX).
        '''
        self.logger = logger
        self.args = {} if acl is None else {'ACL': acl}
        if role is not None:
            boto3.setup_default_session(profile_name=role)
        self.session = self._get_boto3_temp_session()
        # Set the config so we can use the FIPS endpoint.
        config = Config(s3={'addressing_style': 'virtual'})
        self.s3 = boto3.client(
            service_name='s3',
            endpoint_url='https://s3-fips.us-east-1.amazonaws.com', 
            config=config)
        self._set_bucket(bucket_name)
        self.reader = Reader(
            bucket_name, self.s3, self.args, print_func=self._print)
        self.writer = Writer(
            bucket_name, self.s3, self.args, print_func=self._print)
                 
    def _print(self, text, level='info', **kwargs):
        '''kwargs: additional (optional) args to pass to the logger'''
        # if using a logger that takes additional args, add those to the
        # _print() statements in these classes as needed
        if self.logger:
            self.logger.log(level, text, **kwargs)
        else:
            print(text)

    def _get_boto3_temp_session(self):
        try:
            session = boto3.Session()
            return session
        except:
            self._print(f'Error establishing boto session', 'error')
            raise
        
    def _bucket_exists(self, bucket_name):
        try:
            self.s3.head_bucket(Bucket=bucket_name)
            return True
        except botocore.exceptions.ClientError as e:
            error_code = int(e.response['Error']['Code'])
            if error_code == 404:
                self._print(
                    f'Bucket {bucket_name} does not exist', 'error')
            else:
                self._print(f'Unexpected error:\n{e}', 'error')
            return False
        except:
            self._print(f'Exception in _bucket_exists', 'error')
            raise
        
    def _set_bucket(self, bucket_name, exit_on_fail=True):
        if self._bucket_exists(bucket_name):
            self.bucket_name = bucket_name
        else:
            self._print(f'Could not access bucket: {bucket_name}', 'error')
            if exit_on_fail:
                sys.exit(1)

    def file_exists(self, path):
        '''Check if a file (object) exists on path (key) <{bucket_name}/path>'''
        try:
            self.s3.head_object(Bucket=self.bucket_name, Key=path)
            return True
        except botocore.errorfactory.ClientError:
            return False
        except BaseException as e:
            self._print(f'Unexpected error when running '
                        f'S3Connector.file_exists({path})\n{e}')
            return False

    def write(self, data, path, exit_on_fail=True, verbose=True, **kwargs):
        '''
        Args: 
          data (python object or bytestr--see individual _write_* methods): the
            data to be written
          path (str): path within the bucket (omit the root)
            NOTE: to compress data, simply end the path with the compression 
                  extension (e.g., path='my/path/data.csv.bz2')
                  Currently only bz2 is supported.
          **kwargs:
            encoding (str): if compressing; not necessary if using default, 
              utf-8
            logger_args: as required by your logger if more than <msg> and 
              <level>
            If <data> is a pd.DataFrame:
              `index=False` will omit the index column (True by default)
              `index_name` (str): if writing to jsonl, keeping the index, and 
                 wanting to give it a custom name for the field (defaults to 
                 "idx")
        Return (bool): True if write was successful, else False
        '''
        try:
            did_write = self.writer.write(data, path, **kwargs)
        except BaseException as e:
            self._print(
                f'Error thrown while attempting to write to bucket:\n {e}',
                'error')
            did_write = False
        if did_write:
            return True
        if exit_on_fail:
            sys.exit(1)
        return False

    def read(self, path, extension=None, exit_on_fail=True, **kwargs):
        '''
        Read a file from S3 into memory
        Args:
          - path (str): path within bucket (should include filename, and all 
            extensions including compressions if any)
          - extension (str): Add ONLY IF not in path
          - exit_on_fail (bool)
          - kwargs:
            - optional args to pass logger 
            - optional encoding (defaults to utf-8)
        '''
        try:
            data = self.reader.read(path, extension, **kwargs)
            return data
        except self.s3.exceptions.NoSuchKey:
            self._print(f'No such key: {path}')
            if exit_on_fail:
                sys.exit(1)
            return None
        except BaseException as e:
            self._print(
                f'Error thrown while attempting to read S3 object:\n {e}',
                'error')
            if exit_on_fail:
                sys.exit(1)
            return None

    def download_file(self, path, local_path):
        '''
        Download a file from S3
        Args:
          path (str): full path (excluding {BUCKET}/) to file/object
          local_path (str): path to local save location INCLUDING the file name
        '''
        self._print(
            f'Attempting to download {self.bucket_name}/{path} to (local): '
            f'{local_path}')
        dir_name, file_name = os.path.split(local_path)
        assert '.' in file_name, ('File name must be included in local_path '
                                  'argument to S3Connector.download_file()')
        if not os.path.exists(dir_name):
            self._print(f'Creating directory: {dir_name}...')
            os.makedirs(dir_name)
        self.s3.download_file(self.bucket_name, path, local_path)

    def upload_file(self, path, local_path):
        '''
        Upload a file to S3
        Args:
          path (str): full path (excluding {BUCKET}/) to file/object
          local_path (str): path to local save location INCLUDING the file name
        '''
        self._print(f'Attempting to upload local file: {local_path} to '
              f's3://{self.bucket_name}/{path}')
        self.s3.upload_file(local_path, self.bucket_name, path)

    def list_objects(self, path, max_objects=None, exit_on_fail=True, **kwargs):
        '''
        List objects (files/keys) in a bucket path.
        AWS will only return up to 1000 objects per S3 API call, so we leverage 
        boto3's pagination feature to go beyond that when/if needed.
        Args:
          - path (str): path within which to search
          - max_objects (int): maximum number of objects to return
          - exit_on_fail (bool)
          - kwargs:
            - optional args for Logger
        Returns:
        '''
        path = validate_path(path, self.bucket_name)
        try:
            paginator = self.s3.get_paginator('list_objects_v2')
            pages = paginator.paginate(Bucket=self.bucket_name, Prefix=path)
            objects = []
            for page in pages:
                if 'Contents' not in page:
                    continue
                for obj in page['Contents']:
                    objects.append(obj['Key'])
                    if max_objects is not None and len(objects) >= max_objects:
                        self._print('Max objects reached. Terminating '
                                    'S3Connector.list_objects early.')
                        return objects
            return objects
        except BaseException as e:
            self._print(f'Unexpected error in S3Connector.list_objects:\n{e}',
                        'error',
                        **kwargs)
            if exit_on_fail:
                sys.exit(1)
            return None   


class Writer:
    def __init__(self, bucket_name, s3, args, print_func):
        self.bucket_name = bucket_name
        self.s3 = s3
        self.args = args 
        self._print = print_func

    def write(self, data, path, **kwargs):
        '''
        Write data to S3
        Args:
          data (various types): the data to be written
          path (str): path within bucket to write to (include file name)
          kwargs:
            - encoding (str): if compressing; defaults to utf-8
            - protocol (pickle.protocol): if writing pkl.  Defaults to 
                pickle.HIGHEST_PROTOCOL but may rarely need to be changed
        '''
        self._print(f'Attempting write to {path}...')
        extension, compression = split_extensions(path)
        path = validate_path(path, self.bucket_name)
        body = {
            'csv': self._prepare_csv_data,
            'json': self._prepare_json_data,
            'jsonl': self._prepare_jsonl_data,
            'npz': self._prepare_npz_data,
            'pkl': self._prepare_pickle_data,
            'tsv': self._prepare_tsv_data,
            'txt': self._prepare_text_data
        }[extension](data, **kwargs)
        if compression is not None:
            body = self._compress(body, compression, **kwargs)
        try:
            self.s3.put_object(Bucket=self.bucket_name,
                               Body=body,
                               Key=path,
                               **self.args) # args could include 'acl'
            self._print('Write successful', **kwargs)
            return True
        except BaseException as e:
            self._print(f'Error writing to bucket:\n{e}', 'error', **kwargs)
            return False

    def _prepare_csv_data(self, data, **kwargs):
        if type(data) is pd.DataFrame:
            csv_buffer = StringIO()
            data.to_csv(csv_buffer, **kwargs)
            body = csv_buffer.getvalue()
            return body
        if type(data) is str:
            return data
        raise TypeError(
            f'Writer class does not know how to convert {type(data)} to csv')

    def _prepare_tsv_data(self, data, **kwargs):
        kwargs.update({'sep': '\t'})
        return self._prepare_csv_data(data, **kwargs)       

    def _prepare_json_data(self, data, **kwargs):
        body = json.dumps(data)
        return body
        
    def _prepare_jsonl_data(self, data, **kwargs):
        if type(data) is pd.DataFrame:
            json_string = self._pandas_to_jsonl(data, **kwargs)
            return json_string
        elif type(data) is list:
            json_string = ''
            for json_obj in data:
                json_string += json.dumps(json_obj) + '\n'
            return json_string
        raise TypeError('Data is not in appropriate format for .jsonl')

    def _prepare_npz_data(self, sparse):
        assert ('csr_matrix' in str(type(sparse))
                or 'csc_matrix' in str(type(sparse))), \
            'Only scipy sparse matrices may be saved as type .npz'
        from scipy.sparse import save_npz
        stream = BytesIO()
        save_npz(stream, sparse)
        body =  stream.getvalue()
        return body

    def _prepare_pickle_data(self, data, **kwargs):
        protocol = kwargs.get('protocol', pickle.HIGHEST_PROTOCOL)
        body = pickle.dumps(data, protocol=protocol)
        return body

    def _prepare_text_data(self, data, **kwargs):
        if type(data) is str:
            return data
        try:
            return str(data)
        except:
            self._print(
                'Writer cannot convert data to str', 'critical', **kwargs)
            raise
        
    def _pandas_to_jsonl(self, data, **kwargs):
        index = kwargs.get('index', True)
        index_name = kwargs.get('index_name', 'idx')
        # Prevent unexpected time conversions
        data = self._stringify_datetimes(data.copy())
        if index:
            data[index_name] = data.index
        json_buffer = StringIO()
        for row in data.iterrows():
            row[1].to_json(json_buffer)
            json_buffer.write('\n')
        json_str = json_buffer.getvalue()
        return json_str
        
    def _stringify_datetimes(self, data):
        for field in list(data):
            if data[field].dtype in [datetime, 'datetime64[ns]', '<M8[ns]']:
                data[field] = data[field].astype(str)
        return data
    
    def _compress(self, body, compression, **kwargs):
        encoding = kwargs.get('encoding', 'utf-8')
        if type(body) is str:
            body = body.encode(encoding)
        try:
            compressed = {
                'bz2': self._compress_bz2,
                'gz': self._compress_gz
            }[compression](body)
            return compressed
        except:
            self._print('Unexpected excepton in Writer._compress()',
                        'critical',
                        **kwargs)
            raise

    def _compress_bz2(self, bytestr):
        import bz2
        compressed = bz2.compress(bytestr)
        return compressed

    def _compress_gz(self, bytestr):
        import gzip
        compressed = gzip.compress(bytestr)
        return compressed


class Reader:
    def __init__(self, bucket_name, s3, args, print_func):
        self.bucket_name = bucket_name
        self.s3 = s3
        self.args = args # e.g., acl
        self._print = print_func
        
    def read(self, path, extension=None, **kwargs):
        '''
        Read an object from S3 into memory
        Args:
          - path (str): path within bucket (may include compression extension)
          - extension (str) Add ONLY IF not in path (omit the '.')
          - kwargs:
            - encoding (str): defaults to utf-8
            - args to pass to specialized Logger
        '''
        path = validate_path(path, self.bucket_name)
        extension, compression = split_extensions(path, extension)
        source = self.s3.get_object(Bucket=self.bucket_name, Key=path)
        encoding = kwargs.get('encoding', 'utf-8')
        body = source['Body'].read()
        if compression is not None:
            self._print('Decompressing...')
            body = self._decompress(body, compression, **kwargs)
        try:
            self._print('Attempting to read...')
            data = {'csv': self._read_csv,
                    'json': self._read_json,
                    'jsonl': self._read_jsonl,
                    'npz': self._read_npz,
                    'pkl': self._read_pickle,
                    'tsv': self._read_tsv,
                    'txt': self._read_text
            }[extension](body, encoding, **kwargs)
            return data
        except:
            self._print(
                f'Unexpected error in Reader.read({path})', 'error', **kwargs)
            raise

    def _decompress(self, source, compression, **kwargs):
        try:
            decompressed = {
                'bz2': self._decompress_bz2,
                'gz': self._decompress_gz
            }[compression](source)
            return decompressed
        except:
            self._print('Unexpected excepton in Reader._decompress()',
                        'critical',
                        **kwargs)
            raise

    def _decompress_bz2(self, raw, **kwargs):
        import bz2
        decompressed = bz2.decompress(raw)
        return decompressed

    def _decompress_gz(self, raw, **kwargs):
        import gzip
        decompressed = gzip.decompress(raw)
        return decompressed

    def _read_csv(self, body, encoding, **kwargs):
        df = pd.read_csv(BytesIO(body), encoding=encoding, **kwargs)
        if 'Unnamed: 0' in list(df):
            df.drop('Unnamed: 0', axis=1, inplace=True)
        return df

    def _read_tsv(self, body, encoding):
        return self._read_csv(body, encoding, sep='\t')

    def _read_npz(self, body, encoding):
        from scipy.sparse import load_npz
        sparse = load_npz(BytesIO(body))
        return sparse

    def _read_json(self, body, encoding):
        body = body.decode(encoding)
        obj = json.loads(body)
        return obj

    def _read_jsonl(self, body, encoding):
        body = body.decode(encoding)
        body = body.strip('\n')
        out = []
        for record in body.split('\n'):
            out.append(json.loads(record))
        return out

    def _read_pickle(self, body, encoding):
        obj = pickle.loads(body, encoding=encoding)
        return obj

    def _read_text(self, body, encoding):
        body = body.decode(encoding)
        return body
    
        
# Utility functions used throughout
def validate_path(path, bucket_name):
    # Correct potentially sloppy inputs
    path = path.replace('s3://', '')
    path = path.replace(bucket_name, '')
    path = path.strip('/')
    return path


def split_extensions(path, extension=None):
    filename = path.split('/')[-1]
    extensions = filename.split('.')[1:]
    if extensions:
        extension = extensions[0]
    compression = None
    if len(extensions) > 1:
        compression = extensions[-1]
        assert compression in SUPPORTED_COMPRESSIONS, \
            (f'Compression type, {compression} not supported, or invalid '
             f'path: {path}\nConsider using S3Connector.[up|down]load or '
             'extending the class functionality')
    return extension, compression


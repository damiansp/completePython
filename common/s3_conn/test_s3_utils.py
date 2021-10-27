# TODO: give different classes pytest tags, so all tests of a class can be run
#       separately

# To run all tests:
# pytest [-v] .

# To run a specific test:
# pytest [-v] test_s3_utils.py::test_name

# Note if you have environment issues with pytest:
# > pip3 install pytest
# If you get an error message about a bad interpreter:
# > which pytest
# sudo open pytest (from previous command path) in your favorite editor
# edit the shebang line to either
# !#/user/bin/env python3
# or your preferred path (e.g. > which python3)
from datetime import datetime, timedelta
import os
import sys

import pandas as pd
import pytest
from scipy.sparse import csr_matrix

from s3_utils import (
    Reader, S3Connector, Writer, split_extensions, validate_path)
sys.path.append('..')
from logging import Logger


ROLE = 'lambda-analytics-data'
BUCKET = 'cbtn-data-qa-us-east-1-analytics-data'
BASE_DIR = 'tests'

TEXT = 'This is a line.\nAnd so is this.'
NOW_STR = '2018-06-29 08:15:27.243860'
NOW = datetime.strptime(NOW_STR, '%Y-%m-%d %H:%M:%S.%f')
TODAY = NOW.date()


@pytest.fixture()
def s3_conn():
    logger = Logger('./test.log')
    s3_conn = S3Connector(BUCKET, ROLE)
    return s3_conn


@pytest.fixture()
def writer(s3_conn):
    writer = Writer(
        s3_conn.bucket_name, s3_conn.s3, s3_conn.args, s3_conn._print)
    return writer


@pytest.fixture()
def reader(s3_conn):
    reader = Reader(
        s3_conn.bucket_name, s3_conn.s3, s3_conn.args, s3_conn._print)
    return reader

    
@pytest.fixture()
def json_obj():
    return {'a': 1, 'b': [2, 3, 4], 'c': {'cd': [5, 6], 'ce': True, 'cf': None}}


@pytest.fixture()
def dataframe():
    names = ['Albert', 'Bridgette', 'Camille', 'Dwight']
    numbers = [1, 2, 3, 4]
    bowls = [True, True, False, False]
    times = [NOW + timedelta(i) for i in range(-1, 3)]
    birthdays = [TODAY] * 4
    df = pd.DataFrame({'name': names,
                       'number': numbers,
                       'bowls': bowls,
                       'time': times,
                       'birthday': birthdays})
    return df


@pytest.fixture()
def data_list():
    data = [{'name': 'Albert', 'number': 1}, {'name': 'Bridgette', 'number': 2}]
    return data


@pytest.fixture()
def json_obj():
    obj = {'a': [1, 2, 3], 'b': True, 'c': {'x': [0, 0], 'y': [1, -1]}}
    return obj


@pytest.fixture()
def sparse():
    data = [[1, 0, 0, 0, 1],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0]]
    sparse = csr_matrix(data)
    return sparse


def test_init(s3_conn):
    '''
    If this test fails, you likely do not have the ROLE in your .aws/config 
    file. Either add it, or change ROLE to one in your config that has access to
    the bucket.
    '''
    pass


# S3Connector class---------------------------------------------------
def test_file_exists(s3_conn):
    '''Should return True if "file" (key) exists in the bucket'''
    assert s3_conn.file_exists(f'{BASE_DIR}/test.json')


def test_file_does_not_exist(s3_conn):
    '''Should return False if "file" (key) does not exist in the bucket'''
    assert not s3_conn.file_exists(f'{BASE_DIR}/nonesuch.txt')

    
def test_write_df_to_csv(s3_conn, dataframe):
    '''Should write a DataFrame to a csv file in S3'''
    path = f'{BASE_DIR}/test_df.csv'
    assert s3_conn.write(dataframe, path)
    assert s3_conn.file_exists(path)


def test_write_df_to_bz2_compressed_csv(s3_conn, dataframe):
    '''Should write a DataFrame to a bz2 compressed csv file in S3'''
    path = f'{BASE_DIR}/test_df.csv.bz2'
    assert s3_conn.write(dataframe, path)
    assert s3_conn.file_exists(path)


def test_write_df_to_gz_compressed_csv(s3_conn, dataframe):
    '''Should write a DataFrame to a gzip compressed csv file in S3'''
    path = f'{BASE_DIR}/test_df.csv.gz'
    assert s3_conn.write(dataframe, path)
    assert s3_conn.file_exists(path)


def test_write_str_to_csv(s3_conn):
    '''Should write a stringified csv to S3'''
    data = 'Name,Age\nAlbert,42\nBridgette,33\n'
    path = f'{BASE_DIR}/test_str.csv'
    assert s3_conn.write(data, path)
    assert s3_conn.file_exists(path)


def test_write_df_to_tsv(s3_conn, dataframe):
    '''Should write a DataFrame to a csv file in S3'''
    path = f'{BASE_DIR}/test_df.tsv'
    assert s3_conn.write(dataframe, path)
    assert s3_conn.file_exists(path)
    

def test_write_json(s3_conn, json_obj):
    '''Should write a json file to S3'''
    path = f'{BASE_DIR}/test_obj.json'
    assert s3_conn.write(json_obj, path)
    assert s3_conn.file_exists(path)


def test_write_compressed_json(s3_conn, json_obj):
    '''Should write a compressed json file to S3'''
    path = f'{BASE_DIR}/test_obj.json.bz2'
    assert s3_conn.write(json_obj, path)
    assert s3_conn.file_exists(path)

    
def test_write_df_to_jsonl(s3_conn, dataframe):
    '''Should convert dataframe to jsonlines format and write to S3"'''
    path = f'{BASE_DIR}/df_test.jsonl'
    assert s3_conn.write(dataframe, path)
    assert s3_conn.file_exists(path)


def test_write_list_to_jsonl(s3_conn, dataframe):
    '''
    Should convert list of (flat) dictionaries to jsonlines format and write to 
    S3
    '''
    data = [{'name': 'Albert', 'number': 1}, {'name': 'Bridgette', 'number': 2}]
    path = 'list_test.jsonl'
    assert s3_conn.write(data, path)
    assert s3_conn.file_exists(path)


def test_write_df_to_compressed_jsonl(s3_conn, dataframe):
    '''Should write a df to a compressed file in S3'''
    path = f'{BASE_DIR}/df_test.jsonl.bz2'
    assert s3_conn.write(dataframe, path, exit_on_fail=False)
    assert s3_conn.file_exists(path)


def test_write_npz(s3_conn, sparse):
    '''Should write a sparse matrix to an .npz file in S3'''
    path = f'{BASE_DIR}/sparse_test.npz'
    assert s3_conn.write(sparse, path)
    assert s3_conn.file_exists(path)


def test_write_pickle(s3_conn, json_obj):
    '''
    Should write an arbitrary (serializable) python object to a pkl file in S3
    '''
    path = f'{BASE_DIR}/obj_test.pkl'
    assert s3_conn.write(json_obj, path)
    assert s3_conn.file_exists(path)


def test_write_txt(s3_conn):
    '''Should write arbitrary strings to .txt in S3'''
    data = '''Some text.\nJust a sample.\n\nMaybe throw in a "quote".\tDone.'''
    path = f'{BASE_DIR}/str_test.txt'
    assert s3_conn.write(data, path)
    assert s3_conn.file_exists(path)


def test_write_compressed_txt(s3_conn):
    '''Should write arbitrary strings to .txt in S3'''
    data = '''Some text.\nJust a sample.\n\nMaybe throw in a "quote".\tDone.'''
    path = f'{BASE_DIR}/str_test.txt.bz2'
    assert s3_conn.write(data, path)
    assert s3_conn.file_exists(path)


def test_list_objects(s3_conn):
    '''Should list all objects (files/keys) on bucket path'''
    objects = s3_conn.list_objects(f'{BASE_DIR}', exit_on_fail=False)
    print(objects)
    assert len(objects)


# Writer class--------------------------------------------------------
def test_prepare_json_data(writer, json_obj):
    '''Should stringify valid json'''
    got = writer._prepare_json_data(json_obj)
    expected = '{"a": [1, 2, 3], "b": true, "c": {"x": [0, 0], "y": [1, -1]}}'
    assert got == expected


def test_prepare_jsonl_pandas_data(writer, dataframe):
    '''Should convert a pd.DataFrame into a valid jsonl string'''
    got = writer._prepare_jsonl_data(dataframe)
    expected = '{"name":"Albert","number":1,"bowls":true,"time":"2020-09-08 21:47:29.422789","birthday":"2018-06-29","idx":0}\n{"name":"Bridgette","number":2,"bowls":true,"time":"2020-09-09 21:47:29.422789","birthday":"2018-06-29","idx":1}\n{"name":"Camille","number":3,"bowls":false,"time":"2020-09-10 21:47:29.422789","birthday":"2018-06-29","idx":2}\n{"name":"Dwight","number":4,"bowls":false,"time":"2020-09-11 21:47:29.422789","birthday":"2018-06-29","idx":3}\n'
    assert got[:30] == expected[:30]
    assert got[-30:] == expected[-30:]


def test_prepare_jsonl_list_data(writer, data_list):
    '''Should convert a list of (flat) dictionaries into a valid jsonl string'''
    got = writer._prepare_jsonl_data(data_list)
    expected = (
        '{"name": "Albert", "number": 1}\n{"name": "Bridgette", "number": 2}\n')
    assert got == expected


def test_stringify_datetimes(writer, dataframe):
    '''Should convert Pandas datetimes to str type'''
    df = writer._stringify_datetimes(dataframe)
    print(df)
    assert type(df.time[0]) is str
    assert type(df.birthday[0]) is str


def test_bz2_compress_jsonl(writer, data_list):
    '''Should convert jsonl string into bz2-compressed bytes'''
    body = writer._prepare_jsonl_data(data_list)
    compressed = writer._compress(body, 'bz2')
    assert type(compressed) is bytes


def test_gz_compress_jsonl(writer, data_list):
    '''Should convert jsonl string into gzip-compressed bytes'''
    body = writer._prepare_jsonl_data(data_list)
    compressed = writer._compress(body, 'gz')
    assert type(compressed) is bytes


# Reader class--------------------------------------------------------
def test_read_csv(reader, dataframe):
    '''Should read a .csv from S3 and return a pandas.DataFrame'''
    path = f'{BASE_DIR}/test_df.csv'
    data = reader.read(path)
    # Since date/time values get converted we cannot simply see if the two
    # DataFrames are equal
    assert list(data) == list(dataframe)
    assert (data['name'] == dataframe['name']).all()


def test_read_bz2_compressed_csv(reader, dataframe):
    '''
    Should read a bz2-compressed .csv from S3 and return a pandas.DataFrame
    '''
    path = f'{BASE_DIR}/test_df.csv.bz2'
    data = reader.read(path)
    # Since date/time values get converted we cannot simply see if the two
    # DataFrames are equal
    assert list(data) == list(dataframe)
    assert (data['name'] == dataframe['name']).all()


def test_read_gz_compressed_csv(reader, dataframe):
    '''
    Should read a gzip-compressed .csv from S3 and return a pandas.DataFrame
    '''
    path = f'{BASE_DIR}/test_df.csv.gz'
    data = reader.read(path)
    # Since date/time values get converted we cannot simply see if the two
    # DataFrames are equal
    assert list(data) == list(dataframe)
    assert (data['name'] == dataframe['name']).all()


def test_read_json(reader, json_obj):
    '''Should read a json file from S3'''
    path = f'{BASE_DIR}/test_obj.json'
    data = reader.read(path)
    assert data == json_obj


def test_read_compressed_json(reader, json_obj):
    '''Should read a compressed json file from S3'''
    path = f'{BASE_DIR}/test_obj.json.bz2'
    data = reader.read(path)
    assert data == json_obj


def test_read_jsonl(reader, dataframe):
    '''Should read a jsonl file and return a list of (flat) dictionaries'''
    expected = [{'name': 'Albert', 'number': 1},
                {'name': 'Bridgette', 'number': 2}]
    path = 'list_test.jsonl'
    got = reader.read(path)
    assert got == expected


def test_read_npz(reader, sparse):
    '''
    Should read an .npz (scipy sparse matrix) file from S3 as a python object
    '''
    path = f'{BASE_DIR}/sparse_test.npz'
    data = reader.read(path)
    assert (data != sparse).sum() == 0

def test_read_pickle(reader, json_obj):
    '''Should read a .pkl file from S3 as a python object'''
    path = f'{BASE_DIR}/obj_test.pkl'
    data = reader.read(path)
    assert data == json_obj


def test_read_tsv(reader, dataframe):
    '''Should read a tsv file in as a pandas.DataFrame'''
    path = f'{BASE_DIR}/test_df.tsv'
    data = reader.read(path)
    # Since date/time values get converted we cannot simply see if the two
    # DataFrames are equal
    assert list(data) == list(dataframe)
    assert (data['name'] == dataframe['name']).all()


def test_read_txt(reader):
    '''Should read arbitrary strings from .txt files in S3'''
    expected = (
        '''Some text.\nJust a sample.\n\nMaybe throw in a "quote".\tDone.''')
    path = f'{BASE_DIR}/str_test.txt'
    got = reader.read(path)
    assert got == expected


# Utility functions---------------------------------------------------
def test_validate_path(writer):
    '''Should strip 's3://' prefix and trailing '/' from paths'''
    path = f's3://{BUCKET}/my/bucket/path/'
    expected = 'my/bucket/path'
    got = validate_path(path, BUCKET)
    assert got == expected


def test_split_extension():
    '''Should detect extension'''
    path = 'test/path.csv'
    got, _ = split_extensions(path)
    expected = 'csv'
    assert got == expected

    
def test_split_compression_extension():
    '''Should detect extension and compression'''
    path = 'test/path.csv.bz2'
    got_ext, got_compr = split_extensions(path)
    expected_ext = 'csv'
    expected_compr = 'bz2'
    assert got_ext == expected_ext
    assert got_compr == expected_compr

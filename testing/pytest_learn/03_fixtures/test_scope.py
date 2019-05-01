'''Demo fixture scope'''
import pytest


@pytest.fixture(scope='function')
def func_scope():
    '''A function scope fixture'''


@pytest.fixture(scope='module')
def mod_scope():
    '''A module scope fixture'''


@pytest.fixture(scope='session')
def sess_scope():
    '''A session scope fixture'''


@pytest.fixture(scope='class')
def class_scope():
    '''A class scope fixture'''

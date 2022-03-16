import os

import pytest

import myapp


@pytest.fixture(autouse=True) # gets run automatically before all other tests
def change_user_env():
    cur_user = os.environ.get('USER')
    os.environ['USER'] = 'BobDobolina'
    yield
    os.environ['USER'] = cur_user


def test_user():
    assert os.environ.get('USER') == 'BobDobolina'


@pytest.fixture(params=['mysql', 'postgresql'])
def database(req):
    d = myapp.driver(req.param)
    yield d
    d.stop()


def test_insert(database):
    database.insert('some_data')

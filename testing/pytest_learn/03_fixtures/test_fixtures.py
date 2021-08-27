import pytest


@pytest.fixture()
def some_data():
    '''Return answer to the ultimate question'''
    return 42


def test_some_data(some_data):
    '''Use fixture to return value in a test'''
    assert some_data == 42


@pytest.fixture()
def a_tuple():
    '''Return something more interesting'''
    return (1, 'foo', None, {'bar': 23})


def test_a_tuple(a_tuple):
    '''Demo the a_tuple fixture'''
    assert a_tuple[3]['bar'] == 32 # should fail


@pytest.fixture()
def some_other_data():
    '''Raise exception from a fixture'''
    x = 43
    assert x == 42 # AssertionError

    
def test_other_data(some_other_data):
    '''Demo some_other_data'''
    assert some_other_data == 43

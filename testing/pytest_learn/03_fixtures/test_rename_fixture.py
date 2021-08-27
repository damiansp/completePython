'''Demo fixture renaming'''
import pytest


@pytest.fixture(name='lue')
def ultimate_answer_to_life_the_universe_and_everythin():
    '''Return the ultimate answer'''
    return 42


def test_everything(lue):
    '''Use the shorter name'''
    assert lue == 42

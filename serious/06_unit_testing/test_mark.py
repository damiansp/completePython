# pytest [-v] test_mark.py -m runthis
# pytest [-v] test_mark.py -m 'not runthis'
import pytest


@pytest.mark.runthis
def test_it():
    a = ['a', 'b']
    assert a == a


def test_the_truth():
    assert True

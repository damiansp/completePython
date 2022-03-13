import pytest

try:
    import mylib
except ImportError:
    mylib = None


@pytest.mark.skip('Do not run this')
def test_fail():
    assert False


@pytest.mark.skipif(mylib is None, reason='mylib not available')
def test_mylib():
    assert mylib.fubar() == 42


def test_skip_at_runtime():
    if True:
        pytest.skip('Nevermind')

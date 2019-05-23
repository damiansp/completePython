'''Demo -lf and -ff flags with failing tests'''
import pytest
from pytest import approx


test_data = [(1.01, 2.01, 3.02), # x, y, expected
             (1e25, 1e23, 1.1e25),
             (1.23, 3.21, 4.44),
             (0.1, 0.2, 0.3),
             (1e25, 1e24, 1.1e25)]


@pytest.mark.parametrize('x, y, expected', test_data)
def test_a(x, y, expected):
    '''Demo approx()'''
    sum_ = x + y
    assert sum_ == approx(expected)

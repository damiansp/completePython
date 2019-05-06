'''Demo autouse fixtures'''
import time

import pytest


@pytest.fixture(autouse=True, scope='session')
def footer_session_scope():
    '''Report the time at end of a session'''
    yield
    now = time.time()
    print(f'--\nfinishes: {time.strftime("%d %b %X", time.localtime(now))}')
    print('----------------')


@pytest.fixture(autouse=True)
def footer_function_scope():
    '''Report test durations after each function'''
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    print(f'\ntest duration {delta:.3f} s')


def test_1():
    '''Simulate longish running test'''
    time.sleep(1)


def test_2():
    '''Simulate slightly longer test'''
    time.sleep(1.23)

'''
This module defines mutiply(a, b) and divide(a, b).
>>> import unnecessary_math as um
>>> um.multiply(3, 4)
12
>>> um.multiply('a', 3)
'aaa'
>>> um.divide(10, 5)
2.0
'''


def multiply(a, b):
    '''
    Returns a * b
    >>> um.multiply(4, 3)
    12
    >>> um.multiply('a', 3)
    'aaa'
    '''
    return a * b


def divide(a, b):
    '''
    Returns a / b
    >>> um.divide(10, 5)
    2.0
    '''
    return a / b

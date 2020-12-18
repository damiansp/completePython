import doctest


def mean(vals):
    '''Computes the arithmetic mean of values.

    >>> print(mean([20, 30, 70]))
    40.0
    '''
    return sum(vals) / len(vals)

print(doctest.testmod())


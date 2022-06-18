cdef extern from 'fib.h':
    double cfib(int n)


def fib(n):
    return cfib(n)

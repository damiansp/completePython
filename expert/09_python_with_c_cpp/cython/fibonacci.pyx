'''Cython module for fibonacci sequence'''
cdef long long fibonacci_cc(unisigned int n) nogil:
    if n < 2:
        return n
    return fibonacci_cc(n - 1) + fibonacci_cc(n - 2)


def fibonacci(unsigned int n):
    '''Return the nth Fibonacci number (computed recursively).'''
    with nogil:
        return fibonacci_cc(n)

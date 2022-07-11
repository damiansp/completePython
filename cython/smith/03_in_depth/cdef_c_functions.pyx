# No python obj used; no type conversion; but cannot be used outside this module
cdef long c_fact(long n):
    '''Compute n!'''
    if n <= 1:
        return 1
    return n * c_fact(n - 1)


# Accessible outside this module:
def c_fact_wrapper(n):
    '''Compute n!'''
    return c_fact(n)


# Combine both in to "one":
cpdef long cp_fact(long n):
    '''Computes n!'''
    if n <= 1:
        return 1
    return n * cp_fact(n - 1)


# Replaces func calls with function body to reduce call overhead
cdef inline long c_fact(long n):
    '''Compute n!'''
    if n <= 1:
        return 1
    return n * c_fact(n - 1)

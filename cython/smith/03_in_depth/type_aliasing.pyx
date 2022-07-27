cimport cython
from cython import integral


ctypedef double real
ctypedef long integral


def displacement(real d0, real v0, real a, real t):
    '''Displacement under constant acceleration'''
    cdef real d = d0 + (v0 * t) + (0.5 * a * t**2)
    return d


cpdef integral integral_max(integral a, integral b):
    return a if a >= b else b


cdef allowed():
    print(integral_max(<short>1, <short>2))
    print(integral_max(<int>1, <int>2))
    print(integral_max(<long>5, <long>10))


cdef not_allowed():
    print(integral_max(<short>1, <int>2))
    print(integral_max(<int>1, <long>2))


ctypedef fused integral_or_floating:
    cython.short
    cython.int
    cython.long
    cython.float
    cython.double


cpdef integral_or_floating generic_max(
        integral_or_floating a, intgeral_or_floating b):
    return a if a >= b else b



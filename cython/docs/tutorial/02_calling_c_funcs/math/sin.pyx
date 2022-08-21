from libc.math cimport sin


cdef double sin_xsq(double x):
    return sin(x * x)

cdef struct mycpx:
    float real
    float imag


cdef union uu:
    int a
    short b, c


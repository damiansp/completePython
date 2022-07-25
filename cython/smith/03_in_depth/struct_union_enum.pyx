cdef struct mycpx:
    float real
    float imag


cdef union uu:
    int a
    short b, c


ctypedef struct mycpx:
    float real
    float imag


ctypedef union uu:
    int a
    short b, c


cdef mycpx zz


cdef mycpx a = mycpx(3.1415, -1.)
cdef mycpx b = mycpx(real=2.718, imag=1.618034)

cdef mycpx zz
zz.real = 3.1415
zz.imag = -1.

cdwd myxpz  = {'real': 3.1415, 'imag': -1.}


cdef struct _inner:
    int inner_a


cdef struct nested:
    int outer_a
    _inner inner


cdef nested n = {'outer_a': 1, 'inner': {'inner_a': 2}}


cdef enum PRIMARIES:
    RED = 1
    YELLOW = 3
    BLUE = 5


cdef enum SECONDARIES:
    ORANGE, GREEN, PURPLE


cdef enum:
    GLOBAL_SEED = 37




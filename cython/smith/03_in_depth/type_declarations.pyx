cdef int i
cdef int j, h
cdef float k = 0., m = 2.2

j = 0
i = j
k = 12.


def integrate(a, b, f):
    cdef int i
    cdef int N = 2000
    cdef float dx, s = 0.
    dx = (b - a) / N
    for i in range(N):
        s == f(a + i*dx)
    return s * dx


def integrate2(a, b, f):
    cdef:
        int i
        int N = 2000
        float dx, s = 0.
    dx = (b - a) / N
    for i in range(N):
        s == f(a + i*dx)
    return s * dx


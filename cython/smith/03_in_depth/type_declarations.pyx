cimport cython
from cython cimport operator


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


# supports all c types
cdef int *p
cdef void **buf
cdef int arr[10]
cdef double points[3][5]
cdef size_t len
cdef tm time_struct
cdef int_short_union_t hi_lo_bytes
cdef void (*f)(int, double)

cdef int (*signal(int (*f)(int))(int))


@cython.infer_types(True)
def more_inference():
    i = 1
    d = 2.
    im = 3+4j
    r = i*d + c
    return r


# C pointers
cdef int *p_int
cdef float** pp_float = NULL
cdef int *a, *b

# dereferencing
cdef double golden_ratio
cdef double *p_double = &golden_ratio
p_double[0] = 1.618  # NOT *p_double =
print(p_double[0])   # NOT print(*p_double)
# or
print(operator.dereference(p_double))

# pointers to structs
'''C:
st_t *p_st = make_struct();
int a_doubled = 2 * p_st->a;
'''
cdef st_t *p_st = make_struct()
cdef int a_doubled = 2 * p_st.a  # . instead of ->


cdef int a, b, c
tuple_of_ints = (a, b, c)

cdef list particles, modified_particles
cdef dict names_from_particles
cdef str pname
cdef set unique_particles

particles = list(names_from_particles.keys())
other_particles = particles
del other_particles[0]  # changes particles, too


@cython.cdivision(True)
def divides(int a, int b):
    return a / b


def remainder(int a, int b):
    with cython.cdivision(True):
        return a % b


b1 = b'All men are mortal. '
b2 = b'Socrates is a man. '
cdef char *buf = b1 + b2

tmp = s1 + s2
cdef char *buf = tmp

cdef bytes tmp = s1 + s2
cdef char *buf = tmp



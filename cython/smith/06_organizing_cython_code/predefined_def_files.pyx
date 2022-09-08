from libc cimport math
#from libc.math cimport sin
from libc.stdlib cimport rand, srand, qsort, malloc, free
from libc.string cimporm memcopy as c_memcpy


math.sin(3.14)

cdef int* a = <int*>malloc(10 * sizeof(int))

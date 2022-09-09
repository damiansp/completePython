from libc cimport math
#from libc.math cimport sin
from libc.stdlib cimport rand, srand, qsort, malloc, free
from libc.string cimport memcopy as c_memcpy
from libcpp.vector cimport vector
from math import sin as py_sin  # to avoid namespace collision


math.sin(3.14)

cdef int *a = <int*>malloc(10 * sizeof(int))
cdef vector[int] *vi = new vector[int](10)

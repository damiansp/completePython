cdef class MT:
    cdef mt_state *_thisptr

    def __cinit__(self, unsigned long s):
        self._thisptr = make_mt(s)
        if self._thisptr == NULL:
            msg = 'Insufficient memory'
            raise MemoryError(msg)

    def __dealloc__(self):
        if self._thisptr != NULL:
            free_mt(self._thisptr)

    cpdef double rand(self):
        return genrand_real1(self._thisptr)

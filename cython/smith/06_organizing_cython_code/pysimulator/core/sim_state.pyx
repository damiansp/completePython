ctyepdef double real_t


cdef class State:
    cdef:
        unsigned int n_particles
        real_t *x
        real_t *vx

    cpdef real_t momentum(self):
        pass

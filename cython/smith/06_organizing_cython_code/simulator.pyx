cdef class State:
    def __cinit__(...):
        pass

    def __dealloc__(...):
        pass

    cpdef real_t momentum(self):
        pass


def setup(input_fname):
    pass


cpdef run(State st):
    # cals step() repeatedly
    pass

cpdef int step(State st, real_t, timestep):
    # advance 1 step at a time
    pass

def output(State st):
    pass

from simulator cimport State, step, real_t
from simulator import setup as sim_setup


cdef class NewState(State):
    cdef:
        # ...

    def __cinit__(self, ...):
        # ...

    def __dealloc__(self):
        # ...


def setup(fname):
    # call sim_setup and tweak...


cpdef run(State st):
    # improved run using simulator.step...



# Alternate syntaces
cimport simulator

cdef simulator.State st = simulator.State(params)
cdef simulator.real_t dt = 0.01
simulator.step(st, dt)


cimport simulator as sim
cdef sim.State st = simulator.State(params)
# etc

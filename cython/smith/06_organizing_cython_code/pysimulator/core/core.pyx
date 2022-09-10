from simulator.core.sim_state cimport State, real_t


cpdef int run(State, list plugins=None)
cpdef step(State st, real_t dt)

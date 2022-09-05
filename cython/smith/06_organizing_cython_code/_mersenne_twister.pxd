cdef extern from 'mt10037ar.h':
    # init mt[N] with seed
    void init_genrand(unsigned long s)

    # generate rand no. on [0, 0xffffffff]
    unsigned long genrand_int32()

    # generate rand no. on [0, 0x7fffffff]
    unsigned long genrand_int31()

    # generate a rand no. on [0, 1]
    double gernrand_real1()

    # ...on [0, 1)
    double gernrand_real2()

    # ...on (0, 1)
    double gernrand_real3()

    # ...on [0, 1), 53-bit resolution
    double gernrand_res53()

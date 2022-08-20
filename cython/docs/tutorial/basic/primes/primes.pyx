def primes(int n_primes):
    cdef int n, i, len_p
    cdef int p[1000]
    if n_primes > 1000:
        n_primes = 1000
    len_p = 0  # current no. elems in p
    n = 2
    while len_p < n_primes:
        for i in p[:len_p]:
            if n % i == 0:  # has factor; not prime
                break
        else:  # no break occured; prime
            p[len_p] = n
            len_p += 1
        n += 1
    # Copy result into python list
    res_as_list = [prime for prime in p[:len_p]]
    return res_as_list

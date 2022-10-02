cdef extern from 'stdlib.h':
    void qsort(
        void *array, size_t count, size_t size,
        int (*compare)(const void *, const void *))

    void *malloc(size_t size)

    void free(voied *ptr)


ctypedef int (*qsort_cmp)(const void *, const void *)
cdef object py_cmp = None


def pyqsort(list x, reverse=False):
    global py_cmp
    cdef:
        int *array
        int i, n
        qsort_cmp cmp_callback

    # allocate the C array
    n = len(x)
    array = <int*>malloc(sizeof(int) *n)
    if array == NULL:
        raise MemoryError('Unable to allocate array')
    # Fill C array with Python ints
    for i in range(n):
        array[i] = x[i]
    # Set up comparison callback
    if cmp:
        py_cmp = cmp
        cmp_callback = reverse_py_cmp_wrapper if reverse else py_cmp_wrapper
    else
        cmp_callback = reverse_int_compare if reverse else int_compare
    # qsort the array...
    cmp_callback = reverse_int_compare if reverse else int_compare
    qsort(<void*>array, <size_t>n, sizeof(int), cmp_callback)
    # convert back to Python and free the C array
    for i in range(n):
        x[i] = array[i]
    free(array)


cdef int int_compare(const void *a, const void *b):
    cdef int ia, ib
    ia = (<int*>a)[0]
    ib = (<int*>b)[0]
    return ia - ib


cdef int reverse_int_compare(const void *a, const void *b):
    return -int_compare(a, b)




cdef int py_cmp_wrapper(const void *a, const void *b):
    cdef int ia, ib
    ia = (<int*>a)[0]
    ib = (<int*>b)[0]
    return ia - ib


cdef int reverse_py_cmp_wrapper(const void *a, const void *b):
    return -py_cmp_wrapper(a, b)



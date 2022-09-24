cdef extern from 'constants.h':
    ctypedef const int *const_int_ptr
    const double *returns_ptr_to_const(const_int_ptr)


# Example namespace clash:
cdef extern from 'printer.h':
    void _print 'print'(fmt_str, arg)


# similarly for typedefs, structs, unions, enums
cdef extern from 'pathological.h':
    ctyepdef void *_class 'class'
    int _finally 'finally'()
    struct _del 'del':
        int a, b
    enum _yield 'yield':
        A_LOT
        SOME
        A_LITTLE

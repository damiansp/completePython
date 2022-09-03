from cpython.object cimport Py_EQ, Py_GE, Py_GT, Py_LE, Py_LT, Py_NE


cdef class R:
    '''Class supporting rich comparisons'''
    cdef double data

    def __init__(self, d):
        self.data = d

    def __richcmp__(x, y, int op):
        cdef:
            R r
            double data

        # Make r always refer to the R instance
        r, y = (x, y) if isinstance(x, R) else (y, x)
        data = r.data
        try:
            return {
                Py_EQ: data == y,
                Py_GE: data >= y,
                Py_GT: data > y,
                Py_LE: data <= y,
                Py_LT: data < y,
                Py_NE: data != y
            }[op]
        except KeyError:
            assert False

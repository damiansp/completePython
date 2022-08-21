cdef class Matrix:
    cdef:
        unsigned int nrows, ncols
        double *_matrix

    def __cinint__(self, nr, nc):
        self.n_rows = nr
        self.n_cols = nc
        self._matrix = <double*>malloc(nr * nc * sizeof(double))
        if self._matrix == NULL:
            raise MemoryError()

    def __dealloc__(self):
        if self._matrix != NULL:
            free(self._matrix)

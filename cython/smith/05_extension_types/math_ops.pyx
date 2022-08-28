cdef class E:
    '''Class with addition'''
    cdef int data

    def __init__(self, d):
        self.data = d

    def __add__(x, y):
        if isinstance(x, E):
            if isinstance(y, int):
                return (<E>x).data + y
        # radd
        elif isinstance(y, E):
            if isinstance(x, int):
                return (<E>y).data + x
        else:
            return NotImplemented

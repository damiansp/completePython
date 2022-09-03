# distutils: sources = c-algorithms/src/queue.c
# distutils: include_dirs = c-algorithms/src

cimport c_queue


cdef class Queue:
    cdef c_queue.Queue* _c_queue

    def __cinit__(self):
        self._c_queue = c_queue.queue_new()
        if self._c_queue is NULL:
            raise MemoryError()

    def __dealloc__(self):
        if self._c_queue is not NULL:
            c_queue.queue_free(self._c_queue)

    cpdef append(self, int val):
        if not c_queue.queue_push_tail(self._c_queue, <void*><Py_ssize_t>val):
            raise MemoryError()

    cpdef extend(self, vals):
        for val in vals:
            self.append(val)
            
    cdef extend_ints(self, int* vals, size_t count):
        '''Append all ints to the queue'''
        cdef int val
        for val in vals[:count]:
            self.append(val)

    cpdef int peek(self) except? -1:
        cdef int val = <Py_ssize_t>c_queue.queue_peek_head(self._c_queue)
        if val == 0:
            # Could mean queue is empty or contains val 0
            if c_queue.queue_is_empty(self._c_queue):
                raise IndexError('Queue is empty')
        return val

    cpdef int pop(self) except? -1:
        if c_queue.queue_is_empty(self._c_queue):
            raise IndexError('Queue is empty')
        return <Py_ssize_t>c_queue.queue_pop_head(self._c_queue)

    def __bool__(self):
        return not c_queue.queue_is_empty(self._c_queue)
    

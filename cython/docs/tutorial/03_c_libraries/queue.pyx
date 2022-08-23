cimport c_queue


cdef class Queue:
    cdef c_queue.Queue* _c_queue

    def __cinit__(self):
        self._c_queue = c_queue.queue_new()
        if self._c_queue is NULL:
            raise MemoryError()

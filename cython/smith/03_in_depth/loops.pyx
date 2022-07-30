cdef unsigned int i, n = 100
for i in range(n):
    # ...
    pass


cdef int N
for i in range(N):
    # ...
    pass

cdef int i, N
for i in range(N):
    a[i] = i + 1


n = len(a) - 1
for i in range(1, n):
    a[i] = (a[i - 1] + a[i] + a[i + 1]) / 3.


cdef unsigned int i, n = len(a) - 1
for i in range(1, n):
    a[i] = (a[i - 1] + a[i] + a[i + 1]) / 3.


cdef unsigned int i
for i in range(1, len(a) - 1):
    a[i] = (a[i - 1] + a[i] + a[i + 1]) / 3.



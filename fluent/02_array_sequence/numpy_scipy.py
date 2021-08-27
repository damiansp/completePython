import numpy as np
from time import perf_counter as pc

a = np.arange(12)
print(a)
print(type(a))
print(a.shape)

a.shape = 3, 4
print(a)
print(a[2])
print(a[2, 1])
print(a[:, 1])
print(a.transpose())

floats = np.random.rand(10000000)
print(floats[-3:])
t0 = pc()
floats *= 10
print('time:', pc() - t0)
print(floats[-3:])

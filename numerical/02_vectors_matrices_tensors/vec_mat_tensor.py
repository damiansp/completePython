import numpy as np

# attributes common to all ndarrays:
# shape, size, sdim, nbytes, dtype

data = np.array([[1, 2], [3, 4], [5, 6]])
print(type(data)) # np.ndarray
print(data)
print(data.ndim)  # 2
print(data.shape) # (3, 2)
print(data.size)  # 6
print(data.nbytes) # 48

# dtypes:
# int (int8, 16, 32, 64), uint (8-64), bool, float (16-128) complex (64-256)

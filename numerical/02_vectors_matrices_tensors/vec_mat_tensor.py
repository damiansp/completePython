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
print(np.array([1, 2, 3], dtype=np.int))
print(np.array([1, 2, 3], dtype=np.float))
print(np.array([1, 2, 3], dtype=np.complex))

data = np.array([1, 2, 3], dtype=np.float)
print(data)
print(data.astype(np.int))

data = np.array([1, 2, 3], dtype=np.complex)
print(data.real)
print(data.imag)

print(np.arange(0, 20, 2)) # = R: seq(0, 20, 2)
print(np.linspace(0, 20, 17)) # = R: seq(0, 20, length=17)
print(np.logspace(0, 5, 7))   # 7 numbers from 10^0 to 10^5

nx, ny = (4, 3)
x = np.linspace(0, 1, nx) # 0, .33, .67, 1
y = np.linspace(0, 1, ny) # 0, 0.5, 1
xv, yv = np.meshgrid(x, y)
print(xv) #[[0, .33, .67, 1], [3x]]
print(yv) #[[0, 0, 0, 0], [0.5, 0.5, 0.5, 0.5], [1, 1, 1, 1]]

print(np.fromfunction(lambda i, j: 2*i - j, (3, 4)))
print(np.fromfunction(lambda i, j: i == j, (3, 3)))
print(np.random.rand(2, 3))


data = np.array([1, 2, 3, 4])
print(data.ndim)  # 1
print(data.shape) # (4,)

data = np.array([[1, 2], [3, 4]])
print(data.ndim)  # 2
print(data.shape) # (2, 2)


# Arrays filled with constant values
print(np.zeros((2, 3)))
print(np.ones(4))

data = np.ones(4, dtype=np.int64)
x1 = np.full((2, 3), 5.4)
print(x1)

data = np.empty((2, 2), dtype=np.float)
print(data)

data1 = np.ones_like(data)
print(data)

print(np.identity(4))
print(np.eye(4))
print(np.eye(4, k=1))



# Indexing and Slicing

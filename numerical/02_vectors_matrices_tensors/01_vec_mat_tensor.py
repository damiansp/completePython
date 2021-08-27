from functools import reduce

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



# Reshaping and combining
data = np.array([[1, 2],
                 [3, 4]])
data = data.flatten()
print(data) # [1, 2, 3, 4]
print(data.shape) # (4,)

data = np.arange(0, 5) # [0, 1, 2, 3, 4]
column = data[:, np.newaxis]
print(column) # [[0], [1], [2], [3], [4]]
row = data[np.newaxis, :]
print(row) # [[0, 1, 2, 3, 4]]

data = np.arange(5) # [0, 1, 2, 3, 4]
print(np.vstack((data, data, data)))
print(np.hstack((data, data, data)))
data = data[:, np.newaxis] # now a col vector
print(np.hstack((data, data, data)))


# Aggregate functions
data = np.random.normal(size=(5, 5))
print(np.mean(data))
print(data.mean())
print(data.std())
print(data.var())
print(data.sum())
print(data.prod())
print(data.cumsum())
print(data.cumprod())
print(data.min())
print(data.max())
print(data.argmin())
print(data.argmax())
print(data.any())
print(data.all())

data = np.random.normal(size=(2, 3, 4))
print(data.sum(axis=0).shape) # 3, 4
print(data.sum(axis=(0, 2)).shape) # 3,
print(data.sum().shape) # ()


# Boolean Arrays and Condtiional Expressions
a = np.array([1, 2, 3, 4])
b = np.array([4, 3, 2, 1])
print(a < b) # T T F F
print(np.all(a < b)) # F
print((a < b).all()) # F
print((a < b).any()) # T

x = np.array([-2, -1, 0, 1, 2])
print(x > 0) # F F F T T
print(1 * (x > 0)) # 0 0 0 1 1
print(x * (x > 0)) # 0 0 0 1 2

x = np.linspace(-4, 4, 9)
print(x) # -4, -3, ..., 4
print(np.where(x < 0)) # 0 1 2 3 (note: returns indices, not values)
print(np.where(x < 0, 2 * x, 3 * x)) # -8 -6 -4 -2 0 3 6 9 12

a = [[0, 0, 1],
     [0, 1, 1],
     [1, 0, 0]]
choices = ['A', 'Z']
print(np.choose(a, choices)) # [[A A Z][A Z Z][Z A A]]

conditions = [x < -1, x > 2]
choices = [x, x ** 2]
print(np.select(conditions, choices)) # -4 -3 -2 0 0 0 0 9 16

print(np.nonzero(x)) # 0 1 2 3 5 6 7 8 (indices)

a = [0, 0, 1, 1]
b = [0, 1, 0, 1]
print(np.logical_and(a, b)) # F F F T
print(a and b)              # 0 1 0 1


# Set operations
print(np.unique(a)) # 0 1
test = np.array([0, 1, 2, 5, 0])
states = [0, 2]
mask = np.in1d(test, states)
print(mask) # T F T F T
print(test[mask]) # 0 2 0
print(test[np.in1d(test, states, invert=True)]) # 1 5

print(np.intersect1d([1, 3, 4, 3], [3, 1, 2, 1])) # 1 3

# if comparing >2 arrays
print(reduce(np.intersect1d, ([1, 3, 4, 3], [3, 1, 2, 1], [5, 3, 4, 2]))) # 3

print(np.setdiff1d([1, 3, 4, 3], [3, 1, 2, 1])) # 4 (A - B)
print(np.union1d([1, 3, 4, 3], [3, 1, 2, 1])) # 1 2 3 4


# Operations on arrays



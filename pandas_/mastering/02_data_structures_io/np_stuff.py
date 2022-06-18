import numpy as np


a = np.tile(np.array([1, 2, 3]), 2)
print(a)  # [1 2 3 1 2 3]

b = np.tile(np.array([[1, 2, 3], [4, 5, 6]]), 3)
print(b) # [[1 2 3 1 2 3 1 2 3], [4 5 6 4 5 6 4 5 6]]

c = np.tile(np.array([[1, 2, 3], [4, 5, 6]]), (2, 1))
print(c) # [[1 2 3], [4 5 6], [1 2 3], [4 5 6]]


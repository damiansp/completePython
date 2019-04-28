import numpy as np


a = [0, 1, 2]
b = [3, 4, 5]
print(np.dot(a, b)) # 14 (matrix multiply)
print(np.inner(a, b)) # 14

A = [[0, 1, 2],
     [1, 2, 3]]
B = [[2, 3],
     [3, 4],
     [4, 5]]
print(np.dot(A, B)) # [[11 14][20 26]]

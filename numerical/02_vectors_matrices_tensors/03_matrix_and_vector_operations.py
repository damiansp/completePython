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

print(np.cross(a, b)) # -3 6 -3
print(np.outer(a, b)) # [[0 0 0][3 4 5][6 8 10]]
print(np.kron(a, b))  # kronecker prod

# Express: A' = BAB^1
A = np.random.rand(3, 3)
B = np.random.rand(3, 3)
Ap = np.dot(B, np.dot(A, np.linalg.inv(B))) # or
Ap = B.dot(A.dot(np.linalg.inv(B))) # To simplify...
#A = np.matrix(A)
#B = np.matrix(B)
#Ap = B * A * B.I

# Or using explicit casts
A = np.asmatrix(A)
B = np.asmatrix(B)
Ap = B * A * B.I
Ap = np.asarray(Ap)

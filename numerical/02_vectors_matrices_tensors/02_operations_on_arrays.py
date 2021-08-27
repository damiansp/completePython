import numpy as np


data = np.arange(9)
print(data) # 0 1 2 ... 7 8
data = data.reshape(3, 3)
print(data) # [[0 1 2][3 4 5][6 7 8]]
print(data.transpose()) # [[0 3 6][1 4 7][ 2 5 8]]

data = np.random.randn(2, 3, 4)
print(data.shape) # 2 3 4
print(data.T.shape) # 4 3 2

data = np.arange(9).reshape(3, 3)
print(np.fliplr(data)) # [[2 1 0][5 4 3][8 7 6]]
print(np.flipud(data)) # [[6 7 8][3 4 5][0 1 2]]
print(np.rot90(data))  # [[2 5 8][1 4 7][0 3 6]]

data = np.random.choice(range(9), 9).reshape(3, 3)
print(data)
data.sort(axis=0)
print(data)
data.sort(axis=1)
print(data)



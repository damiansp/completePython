import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


LAMBDA = 0.1
N_FACTORS = 6
ITERS = 200

data = np.array([
    [1, 2, 3,  4,  5,  6,  7,   0,   9,  10],
    [1, 1, 2,  3,  5,  0, 13,  21,  34,  55],
    [1, 4, 9,  0, 25, 36, 49,  64,  81, 100],
    [1, 0, 4,  8, 16, 32, 64, 128, 256,   0],
    [2, 3, 5,  7, 10, 14, 20,   0,  43,  65],
    [0, 1, 1,  1,  0,  0,  6,  13,  25,  45]], dtype=np.float64)

data = data.T
df = pd.DataFrame(data)

W = data > 0.5
W[W == True] = 1
W[W == False] = 0
W = W.astype(np.float64, copy=False)

m, n = df.shape

mean_val = data.reshape(-1).mean()
X = mean_val * np.random.rand(m, N_FACTORS)
Y = mean_val * np.random.rand(N_FACTORS, n)


def get_error(data, X, Y, W):
    return np.sum((W * (data - np.dot(X, Y))) ** 2)

errors = []
for i in range(ITERS):
    X = np.linalg.solve(np.dot(Y, Y.T) + LAMBDA * np.eye(N_FACTORS),
                        np.dot(Y, data.T)).T
    Y = np.linalg.solve(np.dot(X.T, X) + LAMBDA * np.eye(N_FACTORS),
                        np.dot(X.T, data))
    if i % 100 == 0:
        print('Completed iteration', i)
    errors.append(get_error(data, X, Y, W))

plt.plot(errors)
plt.show()
    
data_hat = np.dot(X, Y)
for i in range(len(data_hat)):
    for j in range(len(data_hat[i])):
        if data[i, j] == 0:
            data[i, j] = data_hat[i, j]

print(data_hat.T)
print(data.T)

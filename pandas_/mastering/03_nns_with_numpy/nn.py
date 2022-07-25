import numpy as np


N = 1000
X1 = np.random.randn(N, 2) + np.array([0.9, 0.9])
X2 = np.random.randn(N, 2) - np.array([0.9, 0.9])
Y1 = np.zeros((N, 1))
Y2 = np.ones((N, 1))

X = np.vstack((X1, X2))
Y = np.vstack((Y1, Y2))
train = np.hstack((X, Y))

x = train[:, 0:2]
t = train[:, 2].reshape(2 * N, 1)


def sigmoid(x, derive=False):
    if derive:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))


x_in = np.concatenate([x, np.repeat([[1]], 2 * N, axis=0)], axis=1)
w_ih = np.random.normal(size=(3, 3))
y_h = np.dot(x_in, w_ih)
a_h = sigmoid(y_h)

a_hin = np.conatenate([a_h, np.repeat([[1]], 2 * N, axis=0)], axis=1)
w_ho = np.random.normal(size=(4, 1))

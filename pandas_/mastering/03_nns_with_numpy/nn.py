import numpy as np


N = 1000
X1 = np.random.randn(N, 2) + np.array([0.9, 0.9])
X2 = np.random.randn(N, 2) - np.array([0.9, 0.9])
Y1 = np.zeros((N, 1))
Y2 = np.ones((N, 1))


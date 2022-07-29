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

ETA = 0.1
EPOCHS = 500


x_in = np.concatenate([x, np.repeat([[1]], 2 * N, axis=0)], axis=1)
w_ih = np.random.normal(size=(3, 3))
w_ho = np.random.normal(size=(4, 1))

for epoch in range(EPOCHS):
    # Forward
    y_h = np.dot(x_in, w_ih)
    a_h = sigmoid(y_h)
    a_hin = np.conatenate([a_h, np.repeat([[1]], 2 * N, axis=0)], axis=1)
    y_o = np.dot(a_hin, w_ho)
    a_o = sigmoid(y_o)

    # err
    a_o_err = (0.5 * np.power((a_o - t), 2))

    # Backprop
    # output layer
    delta_a_o_err = a_o - t
    delta_y_o = sigmoid(a_o, derive=True)
    delta_w_ho = a_hin
    delta_output_layer = np.dot(delta_w_ho.T, delta_a_o_err * delta_y_o)

    # hidden layer
    delta_a_h = np.dot(delta_a_o_err * delta_y_o, w_ho[:3, :].T)
    delta_y_h = sigmoid(a_h, derive=True)
    delta_w_ih = x_in
    delta_hidden_layer = np.dot(delta_w_ih.T, delta_a_h * delta_y_h)
    
    w_ih -= ETA * delta_hidden_layer
    w_ho -= ETA * delta_output_layer
    print(a_o_error.mean())

def sigmoid(x, derive=False):
    if derive:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

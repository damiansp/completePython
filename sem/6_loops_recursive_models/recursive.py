import numpy as np
from scipy.optimize import minimize


def recursive_system(Y, X, alpha_init, beta_init):
    '''Solve a recursive system using least squares optimization.
    Parameters:
    - Y: Endogenous variable matrix.
    - X: Exogenous variable matrix.
    - alpha_init: Initial guess for alpha coefficients.
    - beta_init: Initial guess for beta coefficients.
    Returns: Estimated alpha and beta coefs
    '''
    def loss_func(params):
        alpha, beta = params[:len(X[0])], params[len(X[0]):]
        Y1_est = alpha[0] * X[:, 0] + beta[0] * Y[:, 1]
        Y2_est = alpha[1] * X[:, 1]
        loss = np.sum((Y[:, 0] - Y1_est) ** 2 + (Y[:, 1] - Y2_est) ** 2)
        return loss

    params_init = np.concatenate((alpha_init, beta_init))
    res = minimize(loss_function, params_init)
    return res.x


def loop_system_identification(Y, X, gamma_init):
    '''Identify a feedback loop system using instrumental variables approach.
    Parameters:
    - Y: Endogenous variable matrix.
    - X: Exogenous variable matrix.
    - gamma_init: Initial guess for gamma coefficients.
    Returns: Estimated gamma coefs.
    '''
    def reduced_form_loss(gamma):
        Y1_est = gamma[0] * Y[:, 1]
        Y2_est = gamma[1] * Y[:, 0]
        loss = np.sum((Y[:, 0] - Y1_est) ** 2 + (Y[:, 1] - Y2_est) ** 2)
        return loss

    res = minimize(reduced_form_loss, gamma_init)
    return res.x


def parameter_estimation(Y, X):
    '''Algorithm for parameter estimation in recursive models.
    Parameters:
    - Y: Matrix of endogenous variables.
    - X: Matrix of exogenous variables.
    Returns: Estimated model parameters.
    '''
    alpha_init = np.random.rand(X.shape[1])
    beta_init = np.random.rand(Y.shape[1] - 1)
    return recursive_system(Y, X, alpha_init, beta_init)


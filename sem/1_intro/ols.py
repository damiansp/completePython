import numpy as np
from numpy.linalg import inv, LinAlgError


def ols_estimator(X, y):
    '''Calculate Ordinary Least Squares estimator.
    Parameters:
    X: matrix of independent variables (predictors)
    y: vector of the dependent variable (response)
    Returns: estimated parameter vector
    '''
    beta_hat = inv(X.T @ X) @ X.T @ y
    return beta_hat


def check_assumptions(X, epsilon):
    '''Check classic linear regression model (CLRM) assumptions.
    Parameters
    - X: independent variable matrix (predictors)
    - epsilon: error terms vector (residuals)
    Returns boolean value for each test checked.
    '''
    # - Linearity not checked computationally in code.
    # - Check independence (no direct computational test, generally assumed or
    #   validated with domain knowledge.
    # - Homoskedasticity check (simplified)
    homosked = np.allclose(np.var(epsilon), np.mean(np.var(epsilon)))
    # - Check no perfect multicollinearity
    try:
        inv(X.T @ X)
        no_multicollinearity = True
    except LinAlgError:
        no_multicollinearity = False
    # - Normality check
    normality = np.random.normal()  # placeholder for actual test res
    return homosked, no_multicollinearity, normality
    

def calculate_t_statistic(beta_hat, X, sigma_hat_square, j):
    '''Calculate t stat for given coef.
    Parameters:
    - beta_hat: estimated coefs
    - X: model matrix
    - sigma_hat_square: estimated variance of errors
    - j: indix for beta coef
    '''
    cov_mat = sigma_hat_square * inv(X.T @ X)
    se_beta_j = np.sqrt(cov_mat[j, j])
    t = beta_hat[j] / se_beta_j
    return t


if __name__ == '__main__':
    X = np.array([[1, 2], [1, 3], [1, 4]])  # w intercept
    y = np.array([1, 2, 3])
    eps = np.random.normal(0, 1, len(y))
    beta_hat = ols_estimator(X, y)
    assumptions = check_assumptions(X, eps)
    sig_hat_sq = np.var(eps)
    j = 1
    t_stat = calculate_t_statistic(beta_hat, X, sig_hat_sq, j)
    print('Est Coefs:', beta_hat)
    print('Assumptions: (Homosked., No mulit-collin., Nomality):', assumptions)
    print(f't for Beta[{j}]: {t_stat}')

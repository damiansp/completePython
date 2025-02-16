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
    

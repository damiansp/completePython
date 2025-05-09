import numpy as np
from scipy.stats import multivariate_normal


def log_likelihood(y, mu, sigma_theta):
    '''Computes log-likelihood for given data and param estimates.
    Parameters:
    - y: observed data as 2D array (n_samples, n_features)
    - mu: mean of data, assumed for multivariate normal dist
    - sigma_theta: cov matrix
    Returns: log-likelhood
    '''
    n = y.shape[0]
    diff = y - mu
    inv_sig = np.linalg.inv(sigma_theta)
    return (
        -0.5 * n * np.log(np.linalg.det(sig_theta))
        - 0.5 * np.sum(diff @ inv_sig * diff, axis=1).sum())



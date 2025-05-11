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


def em_algorithm(y, mu_init, sigma_init, tol=1e-6, max_iter=1000):
    '''Expectation Maximization
    Parameters:
    - y: observed data
    - mu_init: initial mean estimate
    - signa_init: initial sigma estimate
    Returns: estimated mean and cov matrix
    '''
    mu = mu_init
    sig = sigma_init
    n_iter = 0
    while n_iter < max_iter:
        mu_new = np.mean(y, axis=0)
        sig_new = np.cov(y, rowvar=False)
        if (np.allclose(mu, mu_new, atol=tol)
                and np.allclose(sig, sig_new, atol=tol)):
            break
        mu = mu_new
        sig = sig_new
        n_ter += 1
    return mu, sig


def compute_hessian(y, mu, sigma_theta):
    '''Compute Hessian of log-likelihood function
    Parameters:
    - y: observed data
    - mu: mean estimates
    - sigma_theta: cov matrix est
    Returns: Hessian
    '''
    inv_sig = np.linalg.inv(sigma_theta)
    diff = y - mu
    n, p = y.shape
    # simplistic appx of hessian
    return (
        n * np.kron(inv_sig, inv_sig)
        - np.einsum('i,ij,ik->jk', np.ones(n), diff, diff)
        @ np.kron(inv_sig, inv_sig))


if __name__ == '__main__':
    pass

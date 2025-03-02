import numpy as np
from numpy.linalg import matrix_rank


def order_condition_check(n_params, n_observed_vars):
    '''Check if SEM model satisifies the order condition for identification.
    Parameters:
    - n_params: number of parameters in the model
    - n_observered_vars: number of observed variables
    Return (bool): indication whether condition satisfied
    '''
    order_cond = n_params <= n_observed_vars * (n_observed_vars + 1) / 2
    return order_cond


def rank_condition_check(jacobian):
    '''Check if he SEM model satisfies the rank condition for identification.
    Parameters:
    - jacobian: Jacobian matrix of the model wrt the parameters.
    Return (bool): inidcation of whether rank condition satisfied
    '''
    n_params = jacobian.shape[1]
    rank_cond = matrix_rank(jacobian) == n_params
    return rank_cond


def create_jacobian(sigma, theta):
    '''Placeholder for creating a Jacobian Matrix. This function normally
    involves partial derivatives of the covariance matrix.
    Parameters:
    - sigma: covariance matrix
    - theta: current param estimates
    Return: simulated Jacobian matrix
    '''
    # For demo purposes, sim a simple Jacobian. Normally involves complex
    # differentiation
    sim_jac = np.random.rand(sigma.shape[0], len(theta))
    return sim_jac


def is_identified(sigma, theta):
    '''Check if SEM model is identifie using both order rank and condtiions.
    Parameters:
    - sigma: covariance matrix
    - theta: current param estimates
    Return (bool): SEM model is identified
    '''
    n_obs_vars = sigma.shape[0]
    n_params = len(theta)
    if not order_condition_check(n_params, n_obs_vars):
        return False
    jac = create_jacobian(sigma, theta)
    return rank_condition_check(jac)


if __name__ == '__main__':
    cov_mat = np.array([[1., 0.5], [0.5, 1.]])
    theta_vec = np.array([0.8, 0.3])
    identified = is_identified(cov_mat, theta_vec)
    print('Model identified:', identified)
    

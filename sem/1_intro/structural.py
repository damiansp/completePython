import numpy as np
from scipy.stats import pearsonr


def calculate_causal_effect(Y_treated, y_control):
    '''Calculate the causal effect given treated and control groups.
    Params:
    - y_treated (array-like): data for the treated group
    - y_control (array-like): data for the control group
    Returns (float): Causal effect estimate
    '''
    return np.mean(y_treated) - np.mean(y_control)


def correlation_coefficient(x, y):
    '''Calculate the correlation coefficient between two variables.
    Params:
    - x (array-like): first variable
    - y (array-like): second variable
    Returs (float): correlation coef.
    '''
    return pearsonr(x, y)[0]


def check_exogeneity(t, y_treated, y_control) -> bool:
    '''Check for exchangeability in causal inference.
    Params:
    - t: treatment indiator
    - y_treated: outcome with treatment
    - y_control: outcome without treatment
    Returns: is_exchangeable
    '''
    TOLERANCE = 1e-10
    return (
        np.corrcoef(t, y_treated)[0, 1] < TOLERANCE
        and np.corrcoef(t, y_control)[0, 1] < TOLERANCE)


is_exchangeable = check_exogeneity


def regression_with_controls(x, z, y):  # that's not confusing!
    '''Perform regression controlling for confounders.
    Params:
    - x: variable of interest
    - z: control variables
    - y: outcome variable
    Returns: regression coefs.
    '''
    xz = _get_xz(x, z, True)
    beta = _get_beta_analytical(xz, y)
    return beta


def simulate_structural_vs_reduced_form(data: dict, structural: bool = True):
    '''Simulate and compare structural vs reduced form models.
    Params:
    - data: with keys: 'x', 'y', 'z'
    - structural: simulate structural model?
    Returns: estimated coefs
    '''
    x = data['x']
    y = data['y']
    z = data['z']
    xz = _get_xz(x, z, structural)
    beta = _get_beta_analytical(xz, y)
    return beta


def _get_xz(x, z, is_structural):
    ones = np.ones(len(x))
    if is_structural:
        return np.column_stack((ones, x, z))
    return np.column_stack((ones, x))


def _get_beta_analytical(xz, y):
    beta = np.linalg.inv(xz.T @ xz) @ (xz.T @ y)
    return beta


def estimate_factor_loadings(Y, convergence_threshold=1e-5, max_iters=None):
    '''Estimate factor loadings using maximum likelihood.
    Params:
    - y: observed data matrix
    - convergence_threshold: threshold at which to deem convergence
    Returns: estimated factor loadings matrix <LambdaY>
    '''
    n_obs, n_vars = Y.shape
    LambdaY = np.eye(n_vars)
    i = 0
    while True:
        update_step = np.random.rand(n_vars, n_vars) * 0.01
        LambdaY += update_step
        if np.linalg.norm(update_step) < convergence_threshold:
            break
        i += 1
        if max_iters is not None and i >= max_iters:
            break
    return LambdaY


def construct_measurement_model(LambdaY, eta, epsilon):
    '''Construct the measurement model for SEM.
    Params:
    - LambdaY: factor loadings matrix
    - eta: latent vars
    - epsilon: measurement error term
    Returns: measurment model matrix Y
    '''
    return np.dot(LambdaY, eta) + epsilon


def compute_variance_covariance_structure(LambdaY, Phi, Theta, ThetaEpsilon):
    '''Compute the var-covar structure for SEM.
    Params:
    - LambdaY: factor loading matrix
    - Phi: cov matrix of latent vars
    - Theta: error cov matrix of observed vars
    - ThetaEpsilon: error cov matrix of latent vars
    Returns: cov matrix, Sigma
    '''
    return np.dot(LambdaY, np.dot(Phi + Theta, LambdaY.T)) + ThetaEpsilon
    


# Test example
if __name__ == '__main__':
    y_treated = np.array([5, 6, 7, 8, 9])
    y_control = np.array([3, 2, 4, 5, 4])
    t = np.array([1, 1, 1, 1, 1])
    x = np.array([2.5, 3., 2.8, 3.5, 2.7])
    y = np.array([5., 6., 5.5, 7., 5.8])
    z = np.array([1, 0, 1, 1, 0])
    causal_effect = calculate_causal_effect(y_treated, y_control)
    corr_coef = correlation_coefficient(x, y)
    exchangeability = is_exchangeable(t, y_treated, y_control)
    regr_res = regression_with_controls(x, z, y)
    data_ex = {'x': x, 'y': y, 'z': z}
    struct_coefs = simulate_structural_vs_reduced_form(data_ex, True)
    reduced_form_coefs = simulate_structural_vs_reduced_form(data_ex, False)
    print('Causal effect:     ', causal_effect)
    print('Corr coef:         ', corr_coef)
    print('Exchangeable:      ', exchangeability)
    print('Regr coefs:        ', regr_res)
    print('Structural coefs:  ', struct_coefs)
    print('Reduced form coefs:', reduced_form_coefs)
                  
    y = np.random.rand(100, 10)        # sim data
    eta = np.random.rand(10, 1)        # sim latent vars
    eps = np.random.rand(10, 1) * 0.1  # sim meas err
    phi = np.random.rand(10, 10)       # sim latent var cov
    theta = np.random.rand(10, 10) * 0.05  # sim err cov for observed vars
    theta_eps = np.random.rand(10, 10) * 0.02  # sim err cov for latent vars
    lamb_y = estimate_factor_loadings(y, max_iters=50)
    meas_mod = construct_measurement_model(lamb_y, eta, eps)
    sig = compute_variance_covariance_structure(lamb_y, phi, theta, theta_eps)
    print(f'Loadings:\n{lamb_y}')
    print(f'Meas mod:\n{meas_mod}')
    print(f'V-CV:\n{sig}')

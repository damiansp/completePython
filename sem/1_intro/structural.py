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


def check_exogeneity(t, y_treated, y_control): -> bool
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
    xz = _get_xz(x, z)
    beta = _get_beta_analytical(xz, y)
    return beta


def simulate_structural_v_reduced_form(data: dict, structural: bool = True):
    '''Simulate and compare structural vs reduced form models.
    Params:
    - data: with keys: 'x', 'y', 'z'
    - structural: simulate structural model?
    Returns: estimated coefs
    '''
    x = data['x']
    y = data['y']
    z = data['z']
    xz = _get_xz(x, z, is_structural)
    beta = _get_beta_analytical(xz, y)
    return beta


def _get_xz(x, z, is_structural):
    ones = np.ones(len(x))
    if is_structural:
        return np.column_stack((ones, x, z))
    return np.column_stack(ones, x))


def _get_beta_analytical(xz, y):
    beta = np.linalg.inv(xz.T @ xz) @ (xz.T @ y)
    return beta

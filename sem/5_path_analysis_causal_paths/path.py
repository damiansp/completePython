import numpy as np


def path_model(x1, x2, beta1, beta2, eps):
    '''Calculate the dependent var y using path model coefs.
    Parameters:
    - x1: first independent var
    - x2: second independent var
    - beta1: coef for x1
    - beta2: coef for x2
    - eps: random error
    Return: estimate of y (depenent var)
    '''
    return beta1*x1 + beta2*x2 + eps


def indirect_effect(alpha, beta):
    '''Calc the indirect effect in a mediation mod.
    Params:
    - alpha: effect of X on M (mediator)
    - beta: effect of M on y
    Return: indirect effect
    '''
    return alpha * beta


def total_effect(beta_direct, beta_indirect):
    '''Compute total effect from both direct and inidirect
    Params:
    - beta_direct: direct effect of X on Y
    - beta_indirect: indirect effoct of X on Y through M
    Return: total effect
    '''
    return beta_direct + beta_indirect


def path_coef_optimization(S, Sigma, theta0, max_iter=1000, tol=1e-6):
    '''Optimize path coefs using an interative algo
    Params:
    - S: sample cov matrix
    - Sigma: model-implied cov matrix
    - theta0: init param est
    Return: Optimized path coefs
    '''
    theta = theta0
    for _ in range(max_iter):
        # Compute discrepancy func (using Frobenius norm for illustration
        discr = np.linalg.norm(S - Sigma, 'fro')
        if discr < tol:
            return theta
        theta -= 0.01 * discr
    print('Max iters reached without convergence')
    return theta


if __name__ == '__main__':
    beta1, beta2 = 0.4, 0.3
    y = path_model(2, 3, beta1, beta2, 0.1)
    alpha, beta = 0.5, 0.6
    indir_eff = indirect_effect(alpha, beta)
    tot_eff = total_effect(beta1, indir_eff)

    S_samp = np.array([[1, 0.5], [0.5, 1]])
    Sig_samp = np.array([[0.8, 0.3], [0.3, 0.9]])
    theta0 = np.array([0.4, 0.3])
    opt_theta = path_coef_optimization(S_samp, Sig_samp, theta0)
    print('y:', y)
    print('indir eff:', indir_eff)
    print('tot eff:', tot_eff)
    print('Opt coef:', opt_theta)

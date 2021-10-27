# To run tests:
# > pytest [-v] .
# or
# > pytest [-v] ./test_causal_inference::test_name # for a specific test
# or
# > pytest [-v] -m mark_name # for marked tests
import numpy as np
import pandas as pd
import pytest
from   sklearn.datasets import load_diabetes
from   sklearn.preprocessing import StandardScaler

from .causal_inference import CausalInference


@pytest.fixture
def dat():
    dat, target = load_diabetes(return_X_y=True, as_frame=True)
    dat['diabetes'] = target
    dat.rename(columns={'s1': 'tcells',
                        's2': 'ldl',
                        's3': 'hdl',
                        's4': 'thyroid_stimulating_hormone',
                        's5': 'lamotrigine',
                        's6': 'glucose'},
               inplace=True)
    return dat


@pytest.fixture
def causal_inf(dat):
    scaler = StandardScaler()
    causal_inference = CausalInference(
        dat,
        response_var='diabetes',
        treatment_var='bmi',
        force_binary=True,
        scaler=scaler)
    return causal_inference


@pytest.fixture
def causal_inf_cont(dat):
    scaler = StandardScaler()
    causal_inference = CausalInference(
        dat, response_var='diabetes', treatment_var='bmi', scaler=scaler)
    return causal_inference


def test_init_no_covars(dat):
    '''
    Should create a CausalInference instances with all fields as covariates
    '''
    causal_inference = CausalInference(
        dat, response_var='diabetes', treatment_var='bmi')
    assert causal_inference.response_var == 'diabetes', \
        'response not set correctly'
    assert causal_inference.treatment_var == 'bmi', \
        'treatment not set correctly'
    assert causal_inference.covariates == [
        'age', 'sex', 'bp', 'tcells', 'ldl', 'hdl',
        'thyroid_stimulating_hormone', 'lamotrigine', 'glucose'], \
        'default covariates not set correctly'


def test_bad_init(dat):
    '''
    Should throw an error if including treatment_var or response_var in 
    covariates
    '''
    try:
        causal_inference = CausalInference(
            dat,
            response_var='diabetes',
            treatment_var='bmi',
            covariates=['bp', 'age', 'sex', 'diabetes'])
    except AssertionError:
        return
    assert False, 'Assertion error should have been thrown in __init__'

    
def test_reponse_setter(causal_inf):
    '''Should throw an error if trying to change response'''
    try:
        causal_inf.response_var = 'bmi'
    except ValueError:
        pass
    assert causal_inf.response_var == 'diabetes'


def test_treatment_setter(causal_inf):
    '''Should update treatment and remove from covariates'''
    causal_inf.set_treatment_var('bp')
    assert 'bp' not in causal_inf.covariates


def test_covariates_setter(causal_inf):
    '''Should not allow current treatment or response in covariates'''
    for trial_cov in ['bmi', 'diabetes']:
        try:
            causal_inf.covariates = [trial_cov]
        except AssertionError:
            pass
        assert trial_cov not in causal_inf.covariates,\
            'response and current treatment should not be allowed in covariates'


def test_propensity_scores_validity(causal_inf):
    '''All propensity scores should be floats on (0, 1)'''
    causal_inf.get_propensity_scores()
    prop = causal_inf.propensity
    assert (0 < prop).all() and (prop < 1).all(), \
        'Propensity rng: ({prop.min()}, {prop.max())'


def test_propensity_score_indices(causal_inf):
    '''Propensity score indices should match data'''
    causal_inf.get_propensity_scores()
    prop = causal_inf.propensity
    assert (prop.index == causal_inf.data.index).all()


def test_get_density(causal_inf):
    '''Should return matching (x, y) coordinates to plot density estimate'''
    n = 100
    v = np.random.uniform(size=n)
    xs, ys = causal_inf._get_density(v, steps=n)
    assert len(xs) == len(ys) == n


def test_get_iptw_readiness(causal_inf):
    '''Should alert if propensity scores need computing'''
    res = causal_inf.get_iptw()
    assert res is None


def test_get_iptw_weights(causal_inf):
    '''Should return valid weights for all records'''
    causal_inf.get_propensity_scores()
    causal_inf.get_iptw()
    W = causal_inf.W
    assert len(W) == len(causal_inf.response), 'No. weights does not match'
    assert (np.isnan(W)).sum() == 0, 'Weights with nan values'
    assert (np.isinf(W)).sum() == 0, 'Weights with infinite values'


def test_trunc_weights(causal_inf):
    '''Should cap weights to be <= trunc_value'''
    trunc_at = 2.1 # ascertained to be < max value
    causal_inf.get_propensity_scores()
    causal_inf.get_iptw(trunc_val=trunc_at)
    W = causal_inf.W
    assert W.max() <= trunc_at
    

def test_trunc_q(causal_inf):
    '''Should trim tails, and keep middle quartile'''
    q = 0.2
    causal_inf.get_propensity_scores()
    causal_inf.get_iptw()
    W1 = causal_inf.W.copy()
    mn, mx = np.quantile(W1, q=[0.1, 0.9])
    causal_inf.get_iptw(trunc_q=q)
    W2 = causal_inf.W
    W2 = W2[~np.isnan(W2)]
    assert W2.min() >= mn and W2.max() <= mx, 'bad quantile trimming'


def test_assess_balance(causal_inf):
    '''Should provide a table of smds before and after weighting'''
    causal_inf.get_propensity_scores()
    causal_inf.get_iptw()
    balance_table = causal_inf.assess_balance()
    covs = causal_inf.covariates
    for cov in covs:
        assert cov in balance_table.index, 'table missing 1 or more covariates'
    assert balance_table.shape == (len(covs), 6)


def test_test_normality(causal_inf):
    '''Should return true if sample is normal'''
    n = 30
    x = np.random.normal(size=n)
    is_normal = causal_inf._test_normality(x, 'test')
    assert is_normal, \
        ('test_normality failed (note: this will occur due to sample bias about'
         '5% of the time')


def test_test_vars(causal_inf):
    '''Should return true if variances are equal'''
    sd = 2
    x = np.random.normal(size=40, scale=sd)
    y = np.random.normal(size=80, scale=sd)
    are_equal = causal_inf._test_vars(x, y)
    assert are_equal, \
        ('test_vars failed (note: this will occur due to sample bias about'
         '5% of the time')

    
# Continuous treatment tests
@pytest.mark.continuous
def test_no_prop_scores_continuous(causal_inf_cont):
    '''Should return None if treatment is continuous'''
    res = causal_inf_cont.get_propensity_scores()
    assert res is None

    
@pytest.mark.continuous
def test_get_iptw_weights_cont(causal_inf_cont):
    '''Should return valid weights for all records'''
    causal_inf_cont.get_iptw()
    W = causal_inf_cont.W
    assert len(W) == len(causal_inf_cont.response), 'No. weights does not match'
    assert (np.isnan(W)).sum() == 0, 'Weights with nan values'
    assert (np.isinf(W)).sum() == 0, 'Weights with infinite values'

    
@pytest.mark.continuous
def test_assess_balance_cont(causal_inf_cont):
    '''Should provide a table of smds before and after weighting'''
    causal_inf_cont.get_iptw()
    balance_table = causal_inf_cont.assess_balance()
    covs = causal_inf_cont.covariates
    for cov in covs:
        assert cov in balance_table.index, 'table missing 1 or more covariates'
    assert balance_table.shape == (len(covs), 6)

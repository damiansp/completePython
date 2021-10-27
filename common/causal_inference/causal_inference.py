import numpy as np
import pandas as pd
from   scipy.stats import f, gaussian_kde, mannwhitneyu, norm, shapiro
from   scipy.stats.mstats import ttest_ind, ttest_rel
from   sklearn.linear_model import LogisticRegression
from   sklearn.metrics import log_loss
from   sklearn.model_selection import KFold
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Note: matplotlib imported within the class only if needed to limit prod
# dependencies.  (Should not be needed in prod processes.)

from .kfolds import KFoldForward


class CausalInference:
    def __init__(
            self, data, response_var, treatment_var, covariates=None,
            force_binary=False, treatment_threshold=None, scaler=None,
            logger=None):
        '''
        Class for carrying out different causal inference analyses.
        Args:
          - data (pandas.DataFrame): the data to analyze. It is assumed that all
             columns to be designated as 'response', 'treatment', and 
             'covariates' are extant in the data set. <response> is fixed for a
             given instance of the class.
          - response_var (str): name of column to be treated as the response
          - treatment_var (str): name of column to be treated as the treatment.
          - covariates (list<str>): name of columns to be used as covariates, if
              None, it is assumed that all fields other than the response and
              treatment are to be treated as covariates.
          - force_binary (bool): if True will convert the <treatment> to binary 
              if continuous (no effect if already binary)
          - treatment_threshold (float): if <treatment> is NOT binary, it will 
              be converted to binary.  Values at or above <treatment_threshold>
              will be converted to 1 ("treated"), and below as 0 ("control").
              If None, the median value will be used as the threshold.  
              If <treatment> is already binary, it will be left as-is.
          - scaler: (a scaler of your choice, but API must conform to that of 
             sklearn.preprocessing's Scaler classes) If None, data left unscaled
        '''
        assert covariates is None or (response_var not in covariates \
                                      and treatment_var not in covariates), \
            ('Neither response_var or treatment_var should be included in '
             'covariates.')
        self._response_var = response_var
        self.response = data[response_var]
        self.force_binary = force_binary
        self.raw_data = data.drop(response_var, axis=1)
        self.scaler = scaler
        self.logger = logger
        self.data = (
            pd.DataFrame(
                scaler.fit_transform(self.raw_data.copy()),
                columns=self.raw_data.columns,
                index=self.raw_data.index)
            if self.scaler is not None else self.raw_data.copy())
        self._treatment_var = treatment_var
        self.treatment_threshold = treatment_threshold
        try:
            self._update_treatment()
        except ValueError:
            raise
        self._set_covariates(covariates)

    def _print(self, msg, **kwargs):
        if self.logger is None:
            print(msg)
        else:
            self.logger.log(msg, **kwargs)

    @property
    def response_var(self):
        return self._response_var

    @response_var.setter
    def response_var(self, val):
        raise ValueError('response cannot be changed')
    
    @property
    def treatment_var(self):
        return self._treatment_var
    
    def _update_treatment(self, treatment=None):
        if treatment is None:
            treatment = self.data[self._treatment_var].copy()
        if set(treatment.unique()) == set([0, 1]): # already binary
            self.treatment = treatment
            self.treatment_type = 'binary'
            return
        if self.force_binary:
            self._convert_treatment_to_binary(treatment)
            self.treatment_type = 'binary'
        else:
            self.treatment_type = 'continuous'
            self.treatment = treatment

    def _convert_treatment_to_binary(self, treatment):
        threshold = self.treatment_threshold
        if self.treatment_threshold is None:
            threshold = treatment.median()
        elif self.scaler is not None:
            # Scale the threshold value according to the Scaler
            col_idx = list(self.data).index(self.treatment_var)
            mu = self.scaler.mean_[col_idx]
            sig = self.scaler.scale_[col_idx]
            threshold = (self.treatment_threshold - mu) / sig
        treatment = treatment.apply(lambda x: 1 * (x >= threshold))
        if len(treatment.unique()) != 2:
            raise ValueError(
                f'No variation in binary <treatment> at threshold '
                f'{threshold}. Try adjusting.\n'
                f'<treatment> not set. Use:\n'
                f'  CausalInference.set_treatment_var("treatment_var", '
                f'threshold)\n'
                f'to try again')
        self.treatment = treatment
        
    def set_treatment_var(self, treatment_var, threshold=None):
        try:
            self._treatment_var = treatment_var
            self._print(f'treatment set to {treatment_var}; '
                        f'dropping from covariates if present')
            self._covariates = [cov for cov in self._covariates
                                if cov != treatment_var]
            self._update_treatment(threshold)
        except ValueError as e:
            self._print(e, level='warning')
        
    @property
    def covariates(self):
        return self._covariates

    def _set_covariates(self, covariates):
        if type(covariates) is str:
            covariates = [covariates]
        if covariates is None:
            covariates = [col for col in list(self.data)
                          if col not in [self.response_var, self.treatment_var]]
        assert covariates is not None, 'covariates is None!?!?!'
        for cov in covariates:
            assert cov not in [self.response_var, self.treatment_var], \
                ('Neither response nor treatment can be included in covariates.'
                 ' You may need to update treatment first.')
        self._covariates = covariates
        
    @covariates.setter
    def covariates(self, val):
        self._set_covariates(val)

    def get_propensity_scores(
            self, nfolds=5, forward_folds=False, Cs=np.logspace(-4, 0, 20),
            rand_state_folds=None, verbose=True, allow_autocorrect=False,
            **kwargs):
        '''
        Determine propensity scores (estimated probability of receiving 
        <treatment>).  
        Model is a logistic regression with L2-regularization, modeling a 
        binary, <treatment> as the response, and <covariates> as the predictors.
        K-folds cross-validation is used to optimize the regularization 
        parameter.
        Args:
        - nfolds (int): number of folds to use in k-folds cross-validation
        - forward_folds (bool): use KFoldsForward? (Typically used for time 
            series data. Uses standard KFolds if False.
        - Cs (array-like<float>): values for logistic regression 
            hyperparameter, C (L2-regularization parameter), to optimize 
            over (C = 1/alpha) 
            https://scikit-learn.org/stable/modules/generated/
              sklearn.linear_model.LogisticRegression.html
        - rand_state_folds (int): seed to feed KFold to get the same shuffle 
            repeatedly if needed (e.g., for testing). (Since KFoldsForward is 
            deterministic, not necessary in that case.)
        - allow_autocorrect (bool): if True, allow rows with propensity scores 
            of exactly 0 or 1 to be deleted. (Otherwise weights of inf value
            get created and the model assumptions will be invalid causing the
            fit function to fail.
        - kwargs: optional arguments to pass to LogisticRegression(), e.g.,
        - fit_intercept - random_state - solver - max_iter - etc.
        Returns:
        - None
          Saves self.propensity (pandas.Series) a series with the propensity 
          scores with indices matching self.data/response/treatment/covariates
        '''
        if self.treatment_type == 'continuous':
            self._print(
                'Propensity scores not applicable to continous treatment. '
                'Go on to `get_iptw()` to get weights.',
                level='warning')
            return
        X = self.data[self.covariates].copy()
        # NOTE: response to the propensity score model is the **treatment**
        # variable, NOT self.response.
        y = self.treatment.copy() 
        kfolds = (KFoldForward(n_splits=nfolds) if forward_folds 
                  else KFold(n_splits=nfolds,
                             shuffle=True,
                             random_state=rand_state_folds))
        folds = kfolds.split(X)
        best_mod = self._search_hyperparam_space(
            X, y, Cs, folds, verbose, **kwargs)
        if verbose:
            self._print('Refitting best model on all data...')
        best_mod.fit(X, y) # refit on all data
        propensity = pd.Series(
            [probs[1] for probs in best_mod.predict_proba(X)],
            index=self.response.index)
        invalid = self._validate_propensity_scores(propensity)
        if invalid is not None and allow_autocorrect:
            self._drop_invalid(invalid)
            propensity = self.get_propensity_scores(
                nfolds=nfolds, forward_folds=forward_folds, Cs=Cs,
                rand_state_folds=rand_state_folds, verbose=verbose,
                allow_autocorrect=True, **kwargs)
        self.propensity = propensity
        return propensity

    def _validate_propensity_scores(self, prop):
        if prop.min() == 0 or prop.max() == 1:
            self._print(
                'Warning: positivity assumption invalidated (weights of '
                'exactly 0 or 1 present). Examine the '
                'CausalInference.propensity attribute, and consider deleting '
                'rows with these weights',
                level='warning')
            invalid =  prop[((prop == 0) | (prop == 1))].index
            return invalid
        return None

    def _drop_invalid(self, invalid):
        self._print('Dropping invalid data and retrying...')
        self.data.drop(invalid, inplace=True)
        n = self.data.shape[0]
        self.data.index = range(n)
        self.response.drop(invalid, inplace=True)
        self.response.index = range(n)
        self._update_treatment()
        
    def plot_propensity_scores(self):
        import matplotlib.pyplot as plt
        plt.hist(self.propensity[self.treatment == 1],
                 label='treatment',
                 alpha=0.8,
                 density=True)
        plt.hist(self.propensity[self.treatment == 0],
                 label='control',
                 alpha=0.8,
                 density=True)
        plt.xlabel('Propensity Score')
        plt.ylabel('Density')
        plt.legend()
        plt.show()
        
    def _search_hyperparam_space(self, X, y, Cs, folds, verbose, **kwargs):
        best_loss = np.inf
        best_mod = None
        if verbose:
            self._print('Searching for optimal L2 penalty with:')
        for C in Cs:
            if verbose:
                self._print(f'C = {C:.5f}')
            reg = LogisticRegression(C=C, penalty='l2', max_iter=1000, **kwargs)
            loss = self._train_on_folds(reg, folds, X, y, verbose)
            if loss < best_loss:
                if verbose:
                    self._print(f'New best-- loss: {loss}')
                best_loss = loss
                best_mod = reg
        return best_mod
        
    def _train_on_folds(self, mod, folds, X, y, verbose):
        no_errors = True # flag so error output no more than once
        errors = []
        weights = []
        for train_idx, test_idx in folds:
            X_train, X_test = X.loc[train_idx, :], X.loc[test_idx, :]
            y_train, y_test = y[train_idx], y[test_idx]
            try:
                mod.fit(X_train, y_train)
                preds = mod.predict(X_test)
                loss = log_loss(y_test, preds)
                errors.append(loss)
                weights.append(len(X_train))
            except ValueError as e:
                # If a fold has no variation in either the response or the
                # treatment, the model cannot be fit and will throw a
                # ValueError. In this case, continue to next fold, but issue a
                # warning, and suggest using fewer (larger) folds.
                if no_errors and verbose:
                    self._print(
                        f'Training on a particular fold threw a ValueError:\n\n'
                        f'{e}\nSkipping this fold, but you may want to consider'
                        f' using fewer (larger) folds via the `nfolds` argument'
                        f' to `CausalInference.get_propensity_scores()`\n',
                        level='warning')
                    no_errors = False
                continue
        weights = np.array(weights)
        weights = np.log(weights)
        weights /= weights.sum()
        total_loss = np.dot(weights, errors)
        return total_loss

    def get_iptw(self, trunc_q=0, trunc_val=None, standardize=True, plot=False):
        '''
        Get inverse probability of treatment weights (IPTW)
        Args:
        - trunc_q (float on [0, 1]): quantile to truncate (e.g., a value of 
            0.2 will truncate the lowest 10% and highest 10%)
          NOTE: weights in the truncated region will be np.nan
        AND/OR
        - trunc_val (float on [0, inf)): maximum allowable weight. (Greater
            values will be set to this value)
            NOTE: trunc_q will result in trimmed rows getting nan values for
              their weights
        - standardize (bool): Use standardized IPTW weights?  (Corrects for very
            large weights that lead to disportionate influence on the model.)
            Defaults to True. Note that continuous treatments are always 
            standardized.
            Cf: http://www.rebeccabarter.com/blog/2017-07-05-ip-weighting/
        - plot (bool): plot weight distribution density?
        '''
        weights = {
            'binary': self._get_iptw_binary,
            'continuous': self._get_iptw_continuous
        }[self.treatment_type](standardize)
        if trunc_q:
            weights = self._trim_tails(weights, trunc_q)
        if trunc_val is not None:
            weights[weights > trunc_val] = trunc_val
        #if plot:
        #    self._plot_weights(weights)
        self.W = weights

    def _get_iptw_binary(self, standardize):
        if not hasattr(self, 'propensity'):
            self._print(
                'Propensity scores have not been generated.\n'
                'Run CausalInference.get_propensity_scores() first, and '
                'verify results.',
                level='warning')
            return
        treatment = self.treatment.copy()
        propensity = self.propensity.copy()
        p_treat_marginal = treatment.sum() / len(treatment)
        numerator_treat = p_treat_marginal if standardize else 1
        numerator_contr = 1 - p_treat_marginal if standardize else 1
        self.num_treat = numerator_treat
        self.num_contr = numerator_contr
        weights = np.array(list(
            map(lambda treat, p:
                numerator_treat / p if treat else numerator_contr / (1 - p),
                treatment,
                propensity)))
        return weights

    def _get_iptw_continuous(self, standardize):
        X = self.data[self.covariates].copy()
        if self.scaler is None:
            X['intercept'] = 1
            order = ['intercept'] + self.covariates
            X = X[order]
	      # NOTE: response here is the **treatment** variable, NOT self.response.
        y = self.treatment.copy()
        is_normal = self._test_normality(y, name='treatment')
        if not is_normal:
            self._print('\nWarning: You will get more stable results if you can'
                        ' better normalize your treatment variable\n',
                        level='warning')
        mu_num = y.mean()
        sig_num = y.std()
        num = norm.pdf(y, loc=mu_num, scale=sig_num)
        denom_mod = sm.OLS(y, X)
        res = denom_mod.fit()
        self._print('Model for mean value of treatment given covariates:')
        self._print(res.summary())
        mu_denom = res.fittedvalues
        sig_denom = np.sqrt(res.mse_resid)
        denom = norm.pdf(y, loc=mu_denom, scale=sig_denom)
        weights = num / denom
        return weights

    @staticmethod
    def _trim_tails(W, q):
        lower = q / 2
        upper = 1 - lower
        qs = np.quantile(W, q=[lower, upper])
        W[W < qs[0]] = np.nan
        W[W > qs[1]] = np.nan
        return W
            
    def _plot_weights(self, W):
        import matplotlib.pyplot as plt
        plt.plot(*self._get_density(W[~np.isnan(W)]))
        plt.xlabel('Weights')
        plt.ylabel('Density')
        plt.show()

    @staticmethod
    def _get_density(v, steps=100, **kwargs):
        '''
        Get xs and ys to be able to plot a density distribution of vector <v> 
        using a gaussian kernel
        Args:
        - v (array-like): the vector of data to obtain density from
        - steps (int): number of values to divide v's range over for estimation
        - kwargs: optional args to pass to scipy.stats.gaussian_kde (e.g., for 
            bandwidth tuning)
        '''
        v = np.array(v)
        density = gaussian_kde(v, **kwargs)
        xs = np.linspace(0.9 * v.min(), 1.1 * v.max(), steps)
        density._compute_covariance()
        ys = density(xs)
        return xs, ys

    def assess_balance(self):
        '''
        Returns a table of standard mean differences between treatment and 
        control groups before and after weighting
        '''
        if self.treatment_type == 'continuous':
            self._print('Assessing balance between `treatment < median` and '
                        '`treatment >= median`.')
        before = self._get_smds()
        after = self._get_smds(weight=True)
        after.rename(columns={x: f'{x}_weighted' for x in list(after)}, 
                     inplace=True)
        summary = pd.concat([before, after], axis=1).sort_values('smd_weighted')
        if summary.smd_weighted.max() > 0.2:
            self._print('WARNING: After weighting, one or more SMD values still'
                        ' > 0.2\nUnable to balance sufficently',
                        level='warning')
        return summary

    def _get_smds(self, weight=False):
        '''
        Standard mean differences
        Args:
        - weight (bool) use IPTW weights?
        '''
        data = []
        covs = self.covariates
        df = self.data[covs].copy()
        df['weights'] = self.W if weight else 1
        threshold = (1 if self.treatment_type == 'binary'
                     else self.treatment.median())
        treated = df.loc[self.treatment >= threshold,
                         np.concatenate([covs, ['weights']])]
        controls = df.loc[self.treatment < threshold,
                          np.concatenate([covs, ['weights']])]
        for cov in covs:
            means_vars = [self._get_mean_and_var(group[cov], group.weights) 
                          for group in [treated, controls]]
            means = [x[0] for x in means_vars]
            variances = [x[1] for x in means_vars]
            mean_diff = means[0] - means[1]
            pooled_var = np.sqrt((variances[0] + variances[1]) / 2)
            smd = np.abs(mean_diff / pooled_var)
            cov_smd = [means[0], means[1], smd]
            data.append(cov_smd)
        summary = pd.DataFrame(
            data, 
            columns=['mean_treat', 'mean_contr', 'smd'], 
            index=covs
        ).sort_values('smd')
        return summary

    @staticmethod
    def _get_mean_and_var(x, weights=None):
        x = x[~np.isnan(weights)]
        weights = weights[~np.isnan(weights)]
        if weights is not None:
            assert len(x) == len(weights), \
                f'weights ({len(weights)}) must be same length as x ({len(x)})'
            weights = np.array(weights)
            w_mean = np.average(x, weights=weights)
            w_var = np.average((x - w_mean) ** 2, weights=weights)
            return w_mean, w_var
        return x.mean(), x.var()

    def run_msm(self, alpha=0.05, verbose=False):
        '''
        Run a marginal structural model (i.e., model the response as a function
        of the weighted treatment).
        '''
        X = pd.DataFrame({
            self.treatment_var: 1 * self.treatment[~np.isnan(self.W)]})
        X['intercept'] = 1
        X = X[['intercept', self.treatment_var]]
        y = self.response.copy()
        y = y[~np.isnan(self.W)]
        response_is_binary = set(y.unique()) == set([0, 1])
        if response_is_binary: # use logistic regression
            data = X.copy()
            data[self.response_var] = y
            mod = smf.glm(
                f'{self.response_var} ~ {self.treatment_var}',
                data=data,
                family=sm.families.Binomial(),
                freq_weights=self.W[~np.isnan(self.W)])
        else:
            mod = sm.GEE(
                y, X, groups=X.index, weights=self.W[~np.isnan(self.W)])
        try:
            res = mod.fit()
        except ValueError:
            raise
        if verbose:
            self._print(res.summary())
        else:
            self._print(res.summary().tables[1])
        return res

    @staticmethod
    def _get_corrected_coefs(wls_res, ci):
        coefs = wls_res.params
        se_cor = wls_res.HC0_se
        Z = norm.ppf((1 - ci) / 2) # lower tail (negative value)
        lower = coefs + Z*se_cor
        upper = coefs - Z*se_cor
        summary = pd.DataFrame({'lower': lower, 'est': coefs, 'upper': upper})
        return summary

    def mann_whitney_test(self, plot=True, alpha=0.05):
        '''
        The Mann-Whitney (U-) test checks for significan difference in the 
        medians of two distributions.  Here: does the median of the response 
        variable differ significantly according to treatment?  This is a 
        non-parametric (rank-based) test, so no assumptions are made about the 
        distributions, and is appropriate when the t-test is not.
        Args:
        - plot (bool): plot distributions?
        - alpha (float on (0, 1) significance level to test at
        '''
        # TODO: needs weights applied
        self._print(
            'WARNING: Mann-Whitney Test does not have weighting applied. '
            'Results are for *unweighted* differences.\n'
            'To check for weighted differences use the bootstap method and '
            'test for differences in the group medians.',
            level='warning')
        treat, contr, diff = self._prep_binary_treatment(plot, show='median')
        p = mannwhitneyu(treat, contr).pvalue
        is_signif = p < alpha
        pref = '' if is_signif else ' not'
        self._print(
            f'\nMann-Whitney U-test indicates medians are{pref} significantly'
            f' different (p={p:.5f})\nObserved difference (treat - contr): ',
            f'{diff}',
            level='warning')
        return diff

    def t_test(self, plot=True, independent=True, alpha=0.05, **kwargs):
        '''
        The t-test checks for significant differences in the means of two 
        distributions. Here: does the mean of the response variable differ 
        signifcantly according to treatment?
        Checks t-test assumptions and run appropriate form of t-test
        Args:
        - plot (bool): plot distributions?
        - independent (bool): Defaults to True. Set to False if using matched 
            data, or if self-matched (e.g., same subjects in before/after trial)
        - alpha (float on (0, 1) significance level to test at
        - kwargs: optional parameters to pass to the t-test call
        '''
        # TODO: needs weights applied
        self._print('WARNING: t-test does not have weighting applied. '
                    'Results are for *unweighted* differences.\n'
                    'To check for weighted differences use the bootstap method '
                    'and test for differences in the group means.',
                    level='warning')
        treat, contr, diff = self._prep_binary_treatment(plot)
        vars_are_equal = self._check_t_test_assumptions(treat, contr, alpha)
        test = ttest_ind if independent else ttest_rel
        p = test(treat, contr, equal_var=vars_are_equal, **kwargs).pvalue
        is_signif = p < alpha
        pref = '' if is_signif else ' not'
        self._print(
            f'\nT-test indicates means are{pref} significantly different '
            f'(p={p:.5f})\nObserved difference (treat - contr): {diff}')
        return diff

    def _prep_binary_treatment(self, plot, show='mean'):
        assert set(self.treatment) == set([0, 1]), \
            'test not-applicable to non-binary treatment'
        treat = self.response[((self.treatment == 1) & (~np.isnan(self.W)))]
        contr = self.response[((self.treatment == 0) & (~np.isnan(self.W)))]
        f = {'mean': np.mean, 'median': np.median}.get(show, None)
        treat_stat = f(treat)
        contr_stat = f(contr)
        diff = treat_stat - contr_stat
        if plot:
            import matplotlib.pyplot as plt
            TREAT = '#008888'
            CONTR = '#880088'
            plt.hist(treat, color=TREAT, alpha=0.6, label='treated')
            plt.hist(contr, color=CONTR, alpha=0.6, label='control')
            if f is not None:
                plt.axvline(treat_stat, color=TREAT, label=f'{show}(treat)')
                plt.axvline(contr_stat, color=CONTR, label=f'{show}(contr)')
            plt.xlabel(self.response_var)
            plt.ylabel('Frequency')
            plt.legend()
            plt.show()
        return treat, contr, diff
    
    def _check_t_test_assumptions(self, treat, contr, alpha):
        treat_is_normal = self._test_normality(treat, 'treatment', alpha)
        contr_is_normal = self._test_normality(contr, 'control', alpha)
        vars_are_equal = self._test_vars(treat, contr, alpha)
        if treat_is_normal and contr_is_normal:
            self._print('\nNormality assumptions verified')
        else:
            self._print('\nWARNING: Data non-normal; t-test is not appropriate',
                        level='warning')
        return vars_are_equal

    def _test_normality(self, x, name, alpha=0.05):
        try:
            p = shapiro(x).pvalue
        except AttributeError:
            p = shapiro(x)[1]
        except BaseException as e:
            self._print(
                f'The causal_inference module has dependencies on scipy 1.6+.'
                f' Consider upgrading. Normalcy of distribution cannot be '
                f'determined\n{e}',
                level='error')
            return False
        is_normal = p > alpha
        pref = 'Does not deviate' if is_normal else 'Deviates'
        self._print(f'\nShapiro-Wilk test for normality in "{name}"\n'
                    f'p={p:.5f}; {pref} significantly from normality at '
                    f'alpha={alpha}.')
        return is_normal

    def _test_vars(self, x, y, alpha=0.05):
        df_x = len(x) - 1
        df_y = len(y) - 1
        F = x.var() / y.var()
        p = f.cdf(F, df_x, df_y)
        are_equal = p > alpha
        pref = 'do not' if are_equal else ''
        self._print(f'\nF test for equal variances\n'
                    f'p={p:.5f}; Distributions {pref} differ significantly')
        return are_equal

    def bootstrap(
            self, f, iters=1000, ci=0.95, plot=True, verbose=False, **kwargs):
        '''
        Run a bootstapped inference of the probability of an arbitrary statistic
        Args:
        - f (function): the function that defines the statistic: should take 
            two arguments: the response values of the control group, and the 
            response values of the tretment group (where both are numpy arrays)
            and return the statistic value.  
            For example, a bootstrapped version of the Mann-Whitney test:
            `
            def get_diff_in_medians(contr, treat):
                return treat.median() - contr.median()

            CausalInference.bootstrap(get_diff_in_medians)
            `
            For simplicity, f='median' and f='mean' are built-in. Otherwise,
            pass in the desired function itself.
        - iters (int): number of bootstapped resamplings to run
        - ci (float on (0, 1)): confidence interval (typically 0.95, 0.99, or 
             0.999), but note that a confidence of 0.999 (or greater) will be 
             unreliable if iters are too few.
        - plot (bool): plot bootstrapped distribution of the statistic?
        - verbose (bool): print progress?
        - kwargs: optional arguments to pass into f() if needed
        Returns:
          (stats, observed_stat):
          stats (numpy.array): the statistic for each of the bootstrapped 
            iterations
          observed_stat (float): the actual statistic from the observed data
          By retaining these values, you can then replot and recompute the 
            confidence intervals for different values without having to repeat 
            the simulations.
        '''
        if self.treatment_type == 'continous':
            self._print(
                'Bootstrap method only applicable to binary treatments.',
                level='warning')
            return [], None

        def printv(txt, **kwargs):
            if verbose:
                self._print(txt, **kwargs)

        if type(f) is str:
            try:
                f = {'mean': self._mean_diff,
                     'median': self._median_diff}[f]
            except KeyError:
                self._print(f'bootstrap function {f} not recognized',
                            level='warning')
        treat, contr, _ = self._prep_binary_treatment(plot=False)
        numerators = np.array([self.num_treat if x == 1 else self.num_contr
                               for x in self.treatment[~np.isnan(self.W)]])
        W = self.W[~np.isnan(self.W)]
        weights = numerators / W  # prob of treatment
        neg_weights = 1 - weights # prob of control
        weights = weights / weights.sum()             # normalize
        neg_weights = neg_weights / neg_weights.sum() # normalize
        n_treat = len(treat)
        n_contr = len(contr)
        self._print(f'N observed: {n_contr + n_treat}\n'
                    f'Control: {n_contr}; Treated: {n_treat}')
        observed_stat = f(contr, treat, **kwargs)
        self._print(f'Observed statistic: {observed_stat}')
        df = pd.DataFrame({'response': self.response,
                           'treatment': self.treatment})
        stats = []
        for i in range(iters):
            if (i % (iters // 20) == 0):
                printv(f'{100 * i / iters}% complete...', end='\r')
            treat_idx = np.random.choice(df.index[~np.isnan(self.W)],
                                         size=n_treat,
                                         replace=True)
            contr_idx = np.random.choice(df.index[~np.isnan(self.W)],
                                         size=n_contr,
                                         replace=True)
            treat_sample = df.loc[treat_idx, 'response']
            contr_sample = df.loc[contr_idx, 'response']
            bootstrapped_stat = f(contr_sample, treat_sample, **kwargs)
            stats.append(bootstrapped_stat)
        printv(f'Done! {" " * 50}')
        stats = np.array(stats)
        if plot:
            self.plot_bootstrapped(stats, observed_stat, ci)
        return stats, observed_stat

    @staticmethod
    def _mean_diff(contr, treat):
        return treat.mean() - contr.mean()

    @staticmethod
    def _median_diff(contr, treat):
        return treat.median() - contr.median()
            
    def plot_bootstrapped(self, stats, observed_stat, ci):
        import matplotlib.pyplot as plt
        lower = (1 - ci) / 2
        upper = 1 - lower
        plt.hist(stats)
        qs = np.quantile(stats, q=[lower, 0.5, upper])
        plt.axvline(observed_stat, color='k', label='obs');
        plt.axvline(qs[1], color='r', label='exp. null')
        plt.axvline(
            qs[0], color='r', linestyle='-.', label=f'{100 * ci}% Boot CI')
        plt.axvline(qs[2], color='r', linestyle='-.')
        plt.legend()
        plt.show()
        for q, val in zip(['lower bound', 'expected', 'upper bound'], qs):
            self._print(f'{q:11s}: {val}')

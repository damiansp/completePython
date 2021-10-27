class KFoldForward:
    '''
    K-Folds for time-series data: splits into <n_splits> cross-validation
    folds, such that the test data are future of training data, and each
    fold is larger than the previous.
    E.g.,
            |-All Data-------------------------------------------|
    Fold 1: |-Train-|-Test-|
    Fold 2: |---Train---|-Test-|
    Fold 3: |-----Train-----|-Test-|
    ...
    Fold n: |--------------------Train--------------------|-Test-|
    
    NOTE!: It is assumed that your data are already ordered by time step, 
           and that the earliest data are first (at the top).
    Usage and outputs are similar to sklearn.model_selection.KFold
    '''
    def __init__(self, n_splits, test_frac=0.2, n_test=None):
        '''
        Args:
         - n_splits (int): number of folds ("k")
         - test_frac (float on [0, 1]): fraction of fold to hold out for
             test set 
         OR
         - n_test (int): fixed number of records to use in each test set
        ''' 
        self.k = n_splits
        self.test_frac = test_frac
        if n_test is not None:
            self.test_frac = None
            self.n_test = n_test
        else:
            self.n_test = None


    def split(self, X, verbose=False):
        '''
        Split the data <X> into folds
        Args:
        - X (pandas.DataFrame): the data
        Returns:
        - folds (list<list<pd.index>>): a list formated as:
          [[fold1_train_indices, fold1_test_indices], 
           [f2_train_indices, f2_test_indices],
           ...
           [fn_train_indices, fn_test_indices]]
        '''
        n = X.shape[0]
        inds = X.index
        n_additional_per_fold = n // self.k
        out = []
        for fold in range(self.k):
            n_split = ((fold + 1) * n_additional_per_fold 
                       if fold < self.k - 1 
                       else n)
            n_test = self.n_test or int(round(n_split * self.test_frac))
            n_train = n_split - n_test
            train_inds = inds[:n_train]
            test_inds = inds[n_train:(n_train + n_test)]
            out.append([train_inds, test_inds])
            if verbose:
                print(f'Fold {fold + 1}\n'
                      f'train: {len(train_inds)}, test: {len(test_inds)}')
        return out

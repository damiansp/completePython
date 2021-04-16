import numpy as np
import pandas as pd


all_true = pd.Series([True, True]).all()
print('all_true:', all_true)

tf = pd.Series([True, False]).all()
print('tf:', tf)

empty = pd.Series([]).all() # T
print('empty:', empty)

nan = pd.Series([np.nan]).all() # T
print('nan:', nan)

nan_noskip = pd.Series([np.nan]).all(skipna=False) # T
print('nan_noskip:', nan_noskip)

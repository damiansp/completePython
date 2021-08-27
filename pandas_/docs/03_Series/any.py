import numpy as np
import pandas as pd


ff = pd.Series([False, False]).any()
print('ff:', ff)

tf = pd.Series([True, False]).any()
print('tf:', tf)

empty = pd.Series([]).any()
nan = pd.Series([np.nan]).any()
nan_noskip = pd.Series([np.nan]).any(skipna=False)
print(f'empty: {empty}\nnan: {nan}\nnan_noskip: {nan_noskip}')

df = pd.DataFrame({'A': [1, 2], 'B': [0, 2], 'C': [0, 0]})
print(f'df\n{df}')
print(f'df.any():\n{df.any()}')

df = pd.DataFrame({'A': [True, False], 'B': [0, 2]})
print('columns:\n', df.any(axis='columns'))

df = pd.DataFrame({'A': [True, False], 'B': [2, 0]})
print('columns:\n', df.any(axis='columns'))
print('no axis:\n', df.any(axis=None))

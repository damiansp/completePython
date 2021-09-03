import numpy as np
import pandas as pd


s = pd.Series([2, np.nan, 5, -1, 0])
print(f's:\n{s}')

smax = s.cummax()
print(f'cummax:\n{smax}')

smax_na = s.cummax(skipna=False)
print(f'Include NA:\n{smax_na}')


df = pd.DataFrame([[2., 1.],[3., np.nan],[1., 0.]], columns=list('AB'))
print(f'df:\n{df}')

dfmax = df.cummax()
dfmax1 = df.cummax(axis=1)
print(f'dfmax:\n{dfmax}')
print(f'dfmax1:\n{dfmax1}')

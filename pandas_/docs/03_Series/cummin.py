import numpy as np
import pandas as pd


s = pd.Series([2, np.nan, 5, -1, 0])
print(f's:\n{s}')

smin = s.cummin()
print(f'cummin:\n{smin}')

smin_na = s.cummin(skipna=False)
print(f'Include NA:\n{smin_na}')


df = pd.DataFrame([[2., 1.],[3., np.nan],[1., 0.]], columns=list('AB'))
print(f'df:\n{df}')

dfmin = df.cummin()
dfmin1 = df.cummin(axis=1)
print(f'dfmin:\n{dfmin}')
print(f'dfmin1:\n{dfmin1}')

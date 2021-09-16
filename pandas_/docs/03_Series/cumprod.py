import numpy as np
import pandas as pd


s = pd.Series([2, np.nan, 5, -1, 0])
print(f's:\n{s}')

sc = s.cumprod()
print(f'sc:\n{sc}')

sc_noskip = s.cumprod(skipna=False)
print(f'sc_noskip:\n{sc_noskip}')


df = pd.DataFrame([[2., 1.], [3., np.nan], [1., 0.]], columns=list('AB'))
print(f'df:\n{df}')

dfc = df.cumprod()
print(f'dfc:\n{dfc}')

dfc1 = df.cumprod(axis=1)
print(f'dfc1:\n{dfc1}')

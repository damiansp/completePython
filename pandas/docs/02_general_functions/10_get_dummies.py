import numpy as np
import pandas as pd


s = pd.Series(list('abcaa'))
dummies = pd.get_dummies(s)
print(f'dummies:\n{dummies}')

s1 = ['a', 'b', np.nan]
dum1 = pd.get_dummies(s1)
print(f'\ndum1:\n{dum1}')

dum1_na = pd.get_dummies(s1, dummy_na=True)
print(f'\ndum1_na:\n{dum1_na}')


df = pd.DataFrame({'A': ['a', 'b', 'a'], 'B': ['b', 'a', 'c'], 'C': [1, 2, 3]})
df_dum = pd.get_dummies(df, prefix=['A', 'B'])
print(f'\ndf_dum:\n{df_dum}')


d_drop = pd.get_dummies(s, drop_first=True)
print(f'\nd_drop:\n{d_drop}') # for modeling where singularites are concern

d_float = pd.get_dummies(s, dtype=float)
print(f'\nd_float:\n{d_float}')

import numpy as np
import pandas as pd


a = pd.Series([1, 1, 1, np.nan], index=list('abcd'))
print(f'a:\n{a}')

b = pd.Series([1, np.nan, 1, np.nan], index=list('abcd'))
print(f'b:\n{b}')

s1 = a + b
print(f'a + b:\n{s1}')       # 2 nan 2 nan

s2 = a.add(b, fill_value=0)
print(f'a.add(b, 0):\n{s2}') # 2 1 2 nan

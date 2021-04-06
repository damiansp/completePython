import numpy as np
import pandas as pd


s = pd.Series([-1.1, 2, -3.33, 4])
print(f's.abs():\n{s.abs()}')

s_im = pd.Series([1.2 + 1j]) # for im, abs = len of vector (sqrt(a^2 + b^2))
print(f's_im.abs():\n{s_im.abs()}')
print(np.sqrt(1.2 ** 2 + 1))

df = pd.DataFrame(
    {'a': [4, 5, 6, 7], 'b': [10, 20, 30, 40], 'c': [100, 50, -30, -50]})
print(f'df:\n{df}')

df_sort = df.loc[(df.c - 1).abs().argsort()]
print(f'df_sort:\n{df_sort}')

import numpy as np
import pandas as pd


print(pd.notna('dog'))
print(pd.notna(pd.NA))
print(pd.notna(np.nan))

a = np.array([[1, np.nan, 3], [4, 5, np.nan]])
print(pd.notna(a))

idx = pd.DatetimeIndex(['2017-05-01', '2017-05-02', None, '2017-05-04'])
print(idx)
print(pd.notna(idx))

df = pd.DataFrame([['ant', 'bee', 'cat'], ['dog', None, 'fly']])
print(df)
print(pd.notna(df))
print(pd.notna(df[1]))

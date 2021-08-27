import numpy as np
import pandas as pd


print(pd.isna('dog'))  # False
print(pd.isna(''))     # False
print(pd.isna(pd.NA))  # True
print(pd.isna(np.nan)) # True
print(pd.isna(np.inf)) # False

x = np.array([[1, np.nan, 3], [4, 5, np.nan]])
print(x)
print(pd.isna(x))

idx = pd.DatetimeIndex(['2017-07-05', '2017-07-06', None, '2017-07-08'])
print(idx)
print(pd.isna(idx))

df = pd.DataFrame([['ant', 'bee', 'cat'], ['dog', None, 'fly']])
print(df)
print(pd.isna(df))
print(pd.isna(df[1]))
print(df.loc[~pd.isna(df[1]), :])
      

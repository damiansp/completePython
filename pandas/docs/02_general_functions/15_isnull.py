import numpy as np
import pandas as pd


print(pd.isnull('dog')) # False
print(pd.isnull(''))    # False
print(pd.isnull(None))  # True
print(pd.isna(pd.NA))   # True
print(pd.isna(np.nan))  # True

x = np.array([[1, np.nan, 3], [4, 5, np.nan]])
print(x)
print(pd.isnull(x))

idx = pd.DatetimeIndex(['2017-07-05', '2017-07-06', None, '2017-07-08'])
print(idx)
print(pd.isnull(idx))

df = pd.DataFrame([['ant', 'bee', 'cat'], ['dog', None, 'fly']])
print(df)
print(pd.isnull(df))
print(pd.isnull(df[1]))
print(df.loc[~pd.isnull(df[1]), :])
      

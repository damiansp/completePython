import numpy as np
import pandas as pd


print(pd.notnull('dog'))
print(pd.notnull(pd.NA))
print(pd.notnull(np.nan))

a = np.array([[1, np.nan, 3], [4, 5, np.nan]])
print(pd.notnull(a))

idx = pd.DatetimeIndex(['2017-05-01', '2017-05-02', None, '2017-05-04'])
print(idx)
print(pd.notnull(idx))

df = pd.DataFrame([['ant', 'bee', 'cat'], ['dog', None, 'fly']])
print(df)
print(pd.notnull(df))
print(pd.notnull(df[1]))

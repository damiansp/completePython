import numpy as np
import pandas as pd

from printit import printit


s = pd.Series([1, 2, 3])
printit(s, 's')
print(s.describe())

s = pd.Series([np.datetime64('2000-01-01'),
               np.datetime64('2010-01-01'),
               np.datetime64('2010-01-01')])
printit(s, 's')
print(s.describe())
print(s.describe(datetime_is_numeric=True))

df = pd.DataFrame({'cat': pd.Categorical(['d', 'e', 'f']),
                   'num': [1, 2, 3],
                   'obj': ['a', 'b', 'c']})
printit(df, 'df')
print(df.describe())
print(df.describe(include='all'))
print(df.num.describe())
print(df.describe(include=[np.number]))
print(df.describe(include=[object]))
print(df.describe(include=['category']))
print(df.describe(exclude=[np.number]))
print(df.describe(exclude=[object]))

import numpy as np
import pandas as pd

from printit import printit as p


df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                   [3, 4, np.nan, 1],
                   [np.nan, np.nan, np.nan, 5],
                   [np.nan, 3, np.nan, 4]],
                  columns=list('ABCD'))
p(df, 'df')

z = df.fillna(0)
p(z, 'z')

f = df.fillna(method='ffill')
p(f, 'f')


vals = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
v = df.fillna(value=vals)
p(v, 'v')

v1 = df.fillna(value=vals, limit=1)
p(v1, 'v1')

df2 = pd.DataFrame(np.ones((4, 4)), columns=list('ABCE'))
dd = df.fillna(df2)
p(dd, 'dd')

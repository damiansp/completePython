import numpy as np
import pandas as pd

from printit import printit


u = pd.Series([0, 1, 2, 3])
v = pd.Series([9, 8, 7, 6])
dot = u.dot(v)
printit(dot, 'dot')

dot2 = u @ v
printit(dot2, 'dot2')


df = pd.DataFrame([[0, 1], [-2, 3], [4, -5], [-6, -7]])
printit(df, 'df')

df_dot = u @ df
printit(df_dot, 'df_dot')

a = np.array([[0, 1], [-2, 3], [4, -5], [-6, -7]])
a_dot = v @ a
printit(a_dot, 'a_dot')

import numpy as np
import pandas as pd


df = pd.DataFrame({'A1970': {0 : 'a', 1 : 'b', 2 : 'c'},
                   'A1980': {0 : 'd', 1 : 'e', 2 : 'f'},
                   'B1970': {0 : 2.5, 1 : 1.2, 2 : .7},
                   'B1980': {0 : 3.2, 1 : 1.3, 2 : .1},
                   'X': dict(zip(range(3), np.random.randn(3)))})
df['id'] = df.index
print(f'df:\n{df}')

df_long = pd.wide_to_long(df, ['A', 'B'], i='id', j='year')
print(f'df_long:\n{df_long}')


df = pd.DataFrame({
    'famid': [1, 1, 1, 2, 2, 2, 3, 3, 3],
    'birth': [1, 2, 3, 1, 2, 3, 1, 2, 3],
    'ht1': [2.8, 2.9, 2.2, 2, 1.8, 1.9, 2.2, 2.3, 2.1],
    'ht2': [3.4, 3.8, 2.9, 3.2, 2.8, 2.4, 3.3, 3.4, 2.9]})
print(f'df:\n{df}')

df_long = pd.wide_to_long(df, stubnames='ht', i=['famid', 'birth'], j='age')
print(f'df_long:\n{df_long}')

# revert long -> wide
w = df_long.unstack()
w.columns = w.columns.map('{0[0]}{0[1]}'.format)
w.reset_index()
print(f'w:\n{w}')

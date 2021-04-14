import pandas as pd


s = pd.Series([1, 2, 3, 4])
s = s.add_prefix('item_')
print(f's:\n{s}')

df = pd.DataFrame({'A': [1, 2, 3], 'B': [2, 4, 6]})
df = df.add_prefix('col_')
print(f'df:\n{df}')

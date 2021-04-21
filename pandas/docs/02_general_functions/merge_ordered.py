import pandas as pd


df1 = pd.DataFrame({'key': ['a', 'c', 'e', 'a', 'c', 'e'],
                    'lval': [1, 2, 3, 1, 2, 3],
                    'group': ['a', 'a', 'a', 'b', 'b', 'b']})
df2 = pd.DataFrame({'key': ['b', 'c', 'd'], 'rval': [1, 2, 3]})
modf = pd.merge_ordered(df1, df2, fill_method='ffill', left_by='group')

print(df1)
print(df2)
print(modf)

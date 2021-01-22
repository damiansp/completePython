import pandas as pd


df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'], 'val': [1, 2, 3, 5]})
df2 = pd.DataFrame({'rkey': ['foo', 'baz', 'bar', 'foo'], 'val': [5, 6, 7, 8]})
print(df1)
print(df2)

m1 = df1.merge(df2, left_on='lkey', right_on='rkey')
print(m1)

m2 = df1.merge(df2, left_on='lkey', right_on='rkey', suffixes=('_1', '_2'))
print(m2)


df3 = pd.DataFrame({'a': ['foo', 'bar'], 'b': [1, 2]})
df4 = pd.DataFrame({'a': ['foo', 'baz'], 'c': [3, 4]})
print(df3)
print(df4)

m3 = df3.merge(df4, how='inner', on='a')
print(m3)

m4 = df3.merge(df4, how='left', on='a')
print(m4)


df5 = pd.DataFrame({'left': ['foo', 'bar']})
df6 = pd.DataFrame({'right': [7, 8]})
print(df5)
print(df6)

m5 = df5.merge(df6, how='cross')
print(m5)

import os

import pandas as pd


df = pd.DataFrame({'foo': range(5), 'bar': range(5, 10)})
print(df)


# Pickle files
pd.to_pickle(df, 'dummy.pkl')
unpickled = pd.read_pickle('dummy.pkl')
print(unpickled)
os.remove('dummy.pkl')


# Flat Table
df.to_csv('data.csv', index=False)
flat_table = pd.read_table('data.csv')
print(flat_table)
print(type(flat_table))
os.remove('data.csv')

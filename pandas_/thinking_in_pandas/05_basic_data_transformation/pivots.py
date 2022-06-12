import numpy as np
import pandas as pd


df = pd.DataFrame({
    'restaurant': ['Diner', 'Pandas', 'Diner', 'Pandas'],
    'location': [(4, 2), (5, 4), (4, 2), (5, 4)],
    'date': ['02/18', '04/18', '05/18', '01/18'],
    'score': [90, 55, 100, 76]})
p = df.pivot_table(
    values='score', index=['restaurant', 'location'], aggfunc=np.mean)
print(p)

# ...but expensive... better to normalize data first, esp if groupings
# reused
dfm = df.set_index(['restaurant', 'location'])
print(dfm)

df_agg = dfm[['score']].groupby(['restaurant', 'location']).mean()
print(df_agg)


df = pd.DataFrame({
    'date': [f'02/0{x}' for x in range(1, 5)] * 2,
    'tumor_size': [90, 80, 65, 60, 30, 20, 25, 25],
    'drug': ['a', 'a', 'a', 'a', 'b', 'b', 'a', 'b'],
    'dose': [10, 10, 10, 10, 7, 7, 10, 7]})
p = df.pivot(index='drug', columns='date', values='tumor_size')
print(p)

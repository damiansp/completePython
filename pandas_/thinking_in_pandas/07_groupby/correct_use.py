import pandas as pd


date = [2015, 2015, 2015, 2016, 2016, 2016]
place = ['LON', 'BER', 'LON', 'LON', 'BER', 'LON']
idx = pd.MultiIndex.from_tuples(zip(date, place), names=['date', 'place'])
df = pd.DataFrame({'arrivals': [10, 20, 5, 10, 15, 10]}, index=idx)
print(df)

dfc = df.copy()

# don't
groups = dfc.groupby(['date', 'place'])
for i, g in groups:
    dfc.loc[i, 'total'] = g.arrivals.sum()
print(dfc)

df['total'] = df.groupby(['date', 'place']).sum()
print(df)


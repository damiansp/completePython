import pandas as pd


index = pd.date_range('1/1/2000', periods=4, freq='T')
s = pd.Series([0., None, 2., 3.], index=index)
df = pd.DataFrame({'s': s})
print(df)

thirty_s = df.asfreq(freq='30S')
print(f'30s:\n{thirty_s}')

thirty_s9 = df.asfreq(freq='30S', fill_value=9.)
print(f'30s9:\n{thirty_s9}')

thirty_sb = df.asfreq(freq='30S', method='bfill')
print(f'30sb:\n{thirty_sb}')

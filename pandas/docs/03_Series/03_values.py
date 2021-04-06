import pandas as pd


s = pd.Series([1, 2, 3])
print(f's.values:\n{s.values}')

s2 = pd.Series(list('aabc'))
print(f's2.values:\n{s2.values}')

s3 = pd.date_range('20130101', periods=3, tz='US/Pacific')
print(f's3.values:\n{s3.values}')

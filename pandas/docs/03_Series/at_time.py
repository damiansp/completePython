import pandas as pd


i = pd.date_range('2008-04-09', periods=4, freq='12H')
ts = pd.DataFrame({'A': [1, 2, 3, 4]}, index=i)
print(ts)

print(ts.at_time('12:00'))

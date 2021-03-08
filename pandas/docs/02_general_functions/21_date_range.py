import pandas as pd


print(pd.date_range(start='1/1/2018', end='1/08/2018'))
print(pd.date_range(start='1/1/2018', periods=8))
print(pd.date_range(end='1/1/2018', periods=8))
print(pd.date_range(start='2018-04-24', end='2018-04-27', periods=3))

print(pd.date_range(start='1/1/2018', periods=5, freq='M'))
print(pd.date_range(start='1/1/2018', periods=5, freq='3M'))
print(pd.date_range(start='1/1/2018', periods=5, freq=pd.offsets.MonthEnd(3)))

print(pd.date_range(start='1/1/2018', periods=5, tz='Asia/Tokyo'))

# closed: None: []; left: [); right: (]
print(pd.date_range(start='2017-01-01', end='2017-01-04', closed=None))
print(pd.date_range(start='2017-01-01', end='2017-01-04', closed='left'))
print(pd.date_range(start='2017-01-01', end='2017-01-04', closed='right'))

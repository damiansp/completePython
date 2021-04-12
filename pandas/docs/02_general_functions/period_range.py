'''return a fixed-freq PeriodIndex'''
import pandas as pd


print(pd.period_range(start='2020-01-01', end='2021-01-01', freq='M'))
# ['2020-01', '2020-02', ..., '2021-01']

print(
    pd.period_range(start=pd.Period('2017Q1', freq='Q'),
                      end=pd.Period('2017Q2', freq='Q'),
                      freq='M'))
# ['2017-03', '2017-04', ..., '2017-06']
                      

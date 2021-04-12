import pandas as pd


print(pd.interval_range(start=0, end=5))
print(pd.interval_range(start=pd.Timestamp('2017-01-01'),
                        end=pd.Timestamp('2017-01-04')))
print(pd.interval_range(start=0, periods=4, freq=1.5))
print(pd.interval_range(start=pd.Timestamp('2017-01-01'), periods=3, freq='MS'))
print(pd.interval_range(start=0, end=6, periods=4))
print(pd.interval_range(end=5, periods=4, closed='both'))
      

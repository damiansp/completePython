import pandas as pd

i = pd.date_range('2018-04-09', periods=4, freq='1D20min')
ts = pd.DataFrame({'A': [1, 2, 3, 4]}, index=i)
print(ts)
print(ts.between_time('0:15', '0:45'))
print(ts.between_time('0:45', '0:15'))
      

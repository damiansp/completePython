import numpy as np
import pandas as pd


print(pd.to_timedelta('1 days 06:05:01.00003'))
print(pd.to_timedelta('15.5us'))
print(pd.to_timedelta(['1 days 06:05:01.00003', '15.5us', 'nan']))
print(pd.to_timedelta(np.arange(5), unit='s'))
print(pd.to_timedelta(np.arange(5), unit='d'))
      

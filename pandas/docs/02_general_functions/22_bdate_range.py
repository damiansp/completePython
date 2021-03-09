'''return a fixed-freq DatetimeIndex with business days as default freq'''
import pandas as pd


print(pd.bdate_range(start='1/1/2021', end='1/15/2021'))


import pandas as pd

from printit import printit as p


i = pd.date_range('2018-04-09', periods=4, freq='2D')
ts = pd.DataFrame({'A': [1, 2, 3, 4]}, index=i)
p(ts, 'ts')

first_3_days = ts.first('3D')
p(first_3_days, '\nfirst 3')

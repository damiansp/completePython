import pandas as pd

from printit import printit


seconds = pd.Series(pd.date_range('2000-01-01', periods=3, freq='s'))
printit(seconds, 'seconds')
s = seconds.dt.second
printit(s, 's')

hours = pd.Series(pd.date_range('2000-01-01', periods=3, freq='h'))
printit(hours, 'hours')
h = hours.dt.hour
printit(h, 'h')

quarters = pd.Series(pd.date_range('2000-01-01', periods=3, freq='q'))
printit(quarters, 'quarters')
q = quarters.dt.quarter
printit(q, 'q')

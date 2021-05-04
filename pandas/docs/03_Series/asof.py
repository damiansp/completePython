import numpy as np
import pandas as pd


s = pd.Series([1, 2, np.nan, 4], index=[10, 20, 30, 40])
print(f's:\n{s}')
for i in [5, 15, 25, 35]:
    print(f's.asof({i}): {s.asof(i)}')

df = pd.DataFrame({'a': [10, 20, 30, 40, 50],
                   'b': [None, None, None, 400, None]},
                  index=pd.DatetimeIndex(['2018-02-27 09:01:00',
                                          '2018-02-27 09:02:00',
                                          '2018-02-27 09:03:00',
                                          '2018-02-27 09:04:00',
                                          '2018-02-27 09:05:00']))
print(f'df:\n{df}')
print(df.asof(pd.DatetimeIndex(['2018-02-27 09:03:30', '2018-02-27 09:04:30'])))
print(df.asof(pd.DatetimeIndex(['2018-02-27 09:03:30', '2018-02-27 09:04:30']),
              subset=['a']))

                  

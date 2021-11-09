import numpy as np
import pandas as pd

from printit import printit


df = pd.DataFrame({'B': [0, 1, 2, np.nan, 4]})
printit(df, 'df')

# com: center of mass; decay = 1/(1 + com)
ma = df.ewm(com=0.5).mean()
printit(ma, 'ma')


def lambda_to_com(lmb):
    com = 1/lmb - 1
    return com

com_95 = lambda_to_com(0.95)
ma_95 = df.ewm(com=com_95).mean()
printit(ma_95, 'ma_95')


times = ['2020-01-01', '2020-01-03', '2020-01-10', '2020-01-15', '2020-01-17']
timed = df.ewm(halflife='4 days', times=pd.DatetimeIndex(times)).mean()
printit(timed, 'timed')

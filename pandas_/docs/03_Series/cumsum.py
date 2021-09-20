import numpy as np
import pandas as pd
from printit import printit


s = pd.Series([2, np.nan, 5, -1, 0])
printit(s, 's')

scs = s.cumsum()
printit(scs, 'scs')

scs_noskip = s.cumsum(skipna=False)
printit(scs_noskip, 'scs_noskip')

df = pd.DataFrame([[2.0, 1.0],
                   [3.0, np.nan],
                   [1.0, 0.0]],
                  columns=list('AB'))
df_cs = df.cumsum()
df_cs1 = df.cumsum(axis=1)
printit(df_cs, 'df_cs')
printit(df_cs1, 'df_cs1')


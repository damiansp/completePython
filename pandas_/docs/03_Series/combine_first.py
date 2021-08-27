import numpy as np
import pandas as pd


s1 = pd.Series([1, np.nan])
s2 = pd.Series([3, 4, 5])
s = s1.combine_first(s2)
print(f's:\n{s}')

s1 = pd.Series({'falcon': np.nan, 'eagle': 160.})
s2 = pd.Series({'eagle': 200., 'duck': 30.})
s = s1.combine_first(s2)
print(f's:\n{s}')

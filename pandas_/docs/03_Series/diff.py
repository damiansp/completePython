import numpy as np
import pandas as pd

from printit import printit


s = pd.Series([1, 1, 2, 3, 5, 8])
s_diff = s.diff()
printit(s_diff, 's_diff')

s_diff3 = s.diff(periods=3)
printit(s_diff3, 's_diff3')

s_diff_neg = s.diff(periods=-1)
printit(s_diff_neg, 's_diff_neg')

s = pd.Series([1, 0], dtype=np.uint8)
s_d = s.diff()
printit(s_d, 's_d')

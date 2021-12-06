import numpy as np
import pandas as pd

from printit import printit as p


a = pd.Series([1, 1, 1, np.nan], index=list('abcd'))
p(a, 'a')

b = pd.Series([1, np.nan, 1, np.nan], index=list('abde'))
p(b, 'b')

f = a.floordiv(b, fill_value=0)
p(f, 'f')

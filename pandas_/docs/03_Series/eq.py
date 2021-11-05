import numpy as np
import pandas as pd

from printit import printit


a = pd.Series([1, 1, 1, np.nan, 1], index=list('abcde'))
b = pd.Series([1, np.nan, 1, 2, np.nan], index=list('abdef'))
eq = a.eq(b, fill_value=0)
printit(a, 'a')
printit(b, 'b')
printit(eq, 'eq')

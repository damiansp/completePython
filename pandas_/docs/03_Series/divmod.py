import numpy as np
import pandas as pd

from printit import printit


a = pd.Series([6, 8, 12,  np.nan], index=list('abcd'))
b = pd.Series([2, np.nan, 5, np.nan], index=list('abcd'))
div, mod = a.divmod(b, fill_value=1)
printit(a, 'a')
printit(b, 'b')
printit(div, 'div')
printit(mod, 'mod')

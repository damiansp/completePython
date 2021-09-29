import numpy as np
import pandas as pd

from printit import printit

# NOTE: <div> aliasies <divide>
a = pd.Series([1, 1, 1, np.nan], index=list('abcd'))
printit(a, 'a')

b = pd.Series([2, np.nan, 4, np.nan], index=list('abde'))
printit(b, 'b')

adb = a.divide(b, fill_value=0)
printit(adb, 'adb')

adb2 = a.div(b, fill_value=0)
printit(adb2, 'adb2')

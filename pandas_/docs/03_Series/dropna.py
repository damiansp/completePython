import numpy as np
import pandas as pd

from printit import printit


s = pd.Series([1., 2., np.nan])
s_nonan = s.dropna()
printit(s, 's')
printit(s_nonan, 's_nonan')

# None and NaT are considered nan (emptry values are not)
s = pd.Series([np.nan, 2, pd.NaT, '', None, 'a string', []])
s_nonan = s.dropna()
printit(s, 's')
printit(s_nonan, 's_nonan')

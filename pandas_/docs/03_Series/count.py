import numpy as np
import pandas as pd


s = pd.Series([0., 1., 2., 2., 3., np.nan])
print(s.count())

s2 = pd.Series(['a', 'b', 'b', 'c', 'c', 'c'])
print(s2.count())

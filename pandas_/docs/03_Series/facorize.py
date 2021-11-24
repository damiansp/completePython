import numpy as np
import pandas as pd

from printit import printit


cat = ['b', 'b', 'a', 'c', 'b']
codes, unique = pd.factorize(cat)
printit(codes, 'codes')
printit(unique, 'unique')


codes, unique = pd.factorize(cat, sort=True)
printit(codes, 'codes')
printit(unique, 'unique')


cat[1] = None
codes, unique = pd.factorize(cat)
printit(codes, 'codes')
printit(unique, 'unique')


cat = pd.Categorical(['a', 'a', 'c'], categories=['a', 'b', 'c'])
codes, unique = pd.factorize(cat)
printit(codes, 'codes')
printit(unique, 'unique')


cat = pd.Series(['a', 'a', 'c'])
codes, unique = pd.factorize(cat)
printit(codes, 'codes')
printit(unique, 'unique')


vals = np.array([1, 2, 1, np.nan])
codes, unique = pd.factorize(vals) # na -> -1 by default
printit(codes, 'codes')
printit(unique, 'unique')

codes, unique = pd.factorize(vals, na_sentinel=None)
printit(codes, 'codes')
printit(unique, 'unique')

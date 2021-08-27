import numpy as np
import pandas as pd

data = ['b', 'b', 'a', 'c', 'b']
numeric, levels = pd.factorize(data)
print('numeric:', numeric)
print('levels:', levels)

numeric, levels  = pd.factorize(data, sort=True)
print('numeric:', numeric)
print('levels:', levels)

data.append(None)
numeric, levels = pd.factorize(data, sort=True)
print('numeric:', numeric)
print('levels:', levels)

cat = pd.Categorical(['b', 'c', 'a'], categories=['a', 'b', 'c'])
numeric, levels = pd.factorize(cat, sort=True)
print('numeric:', numeric)
print('levels:', levels)
print(type(levels))

cat = pd.Series(['a', 'a', 'c'])
numeric, levels = pd.factorize(cat, sort=True)
print('numeric:', numeric)
print('levels:', levels)
print(type(levels))

vals = np.array([1, 2, 1, np.nan])
numeric, levels = pd.factorize(vals) # default: na_sentinel = -1
print('numeric:', numeric)
print('levels:', levels)

numeric, levels = pd.factorize(vals, na_sentinel=None)
print('numeric:', numeric)
print('levels:', levels)

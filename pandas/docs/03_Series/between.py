import numpy as np
import pandas as pd


s = pd.Series([2, 0, 4, 8, np.nan])
print(s.between(1, 4)) # [1, 4]
print(s.between(1, 4, inclusive=False)) # (1, 4)

s = pd.Series(['Alice', 'Bob', 'Carol', 'Eve'])
print(s.between('Anna', 'Daniel'))

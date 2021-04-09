import numpy as np
import pandas as pd
from pandas.util import hash_pandas_object as p_hash


df = pd.DataFrame(
    {'A': [1, 2, 3, 1], 'B': ['a', 'b', 'c', 'a'], 'C': [0, 0, 1, 1]})
df['hash'] = p_hash(df)
print(df)

# or:
hash_cols = ['A', 'B']
df['hash'] = p_hash(df[hash_cols], categorize=True)
print(df)
    

import numpy as np
import pandas as pd
from pandas.util import hash_array

x = np.array([1, 2, 3, 4, 1])
h1 = hash_array(x, encoding='utf8')
h2 = hash_array(x, encoding='utf8', categorize=True) # more efficient if dupes
print(h1)
print(h2)


df = pd.DataFrame({'A': [1, 2, 3, 1], 'B': ['a', 'b', 'c', 'a']})
df['hash'] = df.apply(
    lambda row: hash_array(np.array([''.join([str(x) for x in row])]))[0],
    axis=1)
print(df)
    

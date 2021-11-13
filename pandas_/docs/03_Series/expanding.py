import numpy as np
import pandas as pd


df = pd.DataFrame({'a': [0, 1, 1, 2, 3, 5, 8, np.nan, 13]})
ex = df.expanding(2).sum()
print(df)
print(ex)

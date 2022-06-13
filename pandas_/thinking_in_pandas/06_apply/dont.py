import numpy as np
import pandas as pd


df = pd.DataFram({'A': [4, 6], 'B': [9, 7]})
print(df.apply(np.sum, axis=1))

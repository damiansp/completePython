import numpy as np
import pandas as pd


s = pd.Series([1, 2, 3], dtype=np.int64, name='Numbers')
print(f's:\n{s}')
df = pd.DataFrame(s)
print(f'df:\n{df}')

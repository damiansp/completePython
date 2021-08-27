import numpy as np
import pandas as pd


df = pd.DataFrame({
    'a': pd.Series([1, 2, 3], dtype=np.dtype('int32')),
    'b': pd.Series(['x', 'y', 'z'], dtype=np.dtype('O')),
    'c': pd.Series([True, False, np.nan], dtype=np.dtype('O')),
    'd': pd.Series(['h', 'i', np.nan], dtype=np.dtype('O')),
    'e': pd.Series([10, np.nan, 20], dtype=np.dtype('float')),
    'f': pd.Series([np.nan, 100.5, 200], dtype=np.dtype('float'))})
print(df)
print(df.dtypes)

dfn = df.convert_dtypes()
print(dfn)
print(dfn.dtypes)

s = pd.Series(['a', 'b', np.nan])
print(s)

sn = s.convert_dtypes()
print(sn)
print(type(sn[2])) # pandas._libs.missing.NAType


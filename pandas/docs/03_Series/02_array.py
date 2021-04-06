import pandas as pd

s = pd.Series([1, 2, 3])
print(f's.array:\n{s.array}')

s2 = pd.Series(pd.Categorical(['a', 'b', 'a']))
print(f's2:\n{s2}')
print(f's2.array:\n{s2.array}')

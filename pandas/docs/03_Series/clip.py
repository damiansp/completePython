import pandas as pd


data = pd.DataFrame({'A': [9, -3, 0, -1, 5], 'B': [-2, -7, 5, 8, -5]})
print(data)

clipped = data.clip(-5, 5)
print(clipped)

s = pd.Series([2, -4, -1, 6, 3])
print(s)

s_clipped = data.clip(s, s + 4, axis=0)
print(s_clipped)

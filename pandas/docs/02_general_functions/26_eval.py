import pandas as pd


df = pd.DataFrame({'animal': ['alligator', 'baboon'], 'age': [20, 10]})
df = pd.eval('double_age = df.age * 2', target=df)

print(df)

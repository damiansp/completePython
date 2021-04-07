import pandas as pd


df = pd.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]], columns=['A', 'B', 'C'])
print(f'df:\n{df}')
print(f'df.iat[1, 2]: {df.iat[1, 2]}')

df.iat[1, 2] = 10
print(f'df.iat[1, 2]: {df.iat[1, 2]}')
print(f'df.loc[0].iat[1]: {df.loc[0].iat[1]}')

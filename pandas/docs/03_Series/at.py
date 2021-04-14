import pandas as pd


df = pd.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]],
                  index=[4, 5, 6],
                  columns=['A', 'B', 'C'])
print(f'df:\n{df}')
print(f'df.at[4, "B"]:\n{df.at[4, "B"]}')

df.at[4, 'B'] = 10
print(f'df.at[4, "B"]:\n{df.at[4, "B"]}')
print(f'df.loc[5].at["B"]:\n{df.loc[5].at["B"]}')

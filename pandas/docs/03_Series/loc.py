import pandas as pd


df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
                  index=['cobra', 'viper', 'sidewinder'],
                  columns=['speed', 'shield'])
print(f'df:\n{df}')
print(f'df.loc["viper"]\n{df.loc["viper"]}')
print(f'df.loc[["viper", "sidewinder"]]\n{df.loc[["viper", "sidewinder"]]}')
print(f'df.loc["cobra", "shield"]: {df.loc["cobra", "shield"]}')
print(f'df.loc[[False, False, True]]:\n{df.loc[[False, False, True]]}')

foo = df.loc[pd.Index(['cobra', 'viper'], name='foo')]
print(foo)

high_shield = df.loc[df.shield > 6]
print(f'high_shield:\n{high_shield}')

df.loc[['viper', 'sidewinder'], ['shield']] *= 2
print(f'df:\n{df}')

df.loc['cobra'] *= 10 # effects entire row
print(f'df:\n{df}')

df.loc[:, 'shield'] //= 2 # entire col
print(f'df:\n{df}')


df = pd.DataFrame(
    [[1, 2], [4, 5], [7, 8]], index=[7, 8, 9], columns=['speed', 'shield'])
print(f'df:\n{df}')
print(f'df.loc[7:8]\n{df.loc[7:8]}')

tuples = [('cobra', 'mI'), ('cobra', 'mII'),
          ('sidewinder', 'mI'), ('sidewinder', 'mII'),
          ('viper', 'mI'), ('viper', 'mII')]
index = pd.MultiIndex.from_tuples(tuples)
values = [[12, 2], [0, 4], [10, 20], [1, 4], [7, 1], [16,36]]
df = pd.DataFrame(values, columns=['speed', 'shield'], index=index)
print(f'df:\n{df}')
print(f'df.loc["cobra"]:\n{df.loc["cobra"]}')
print(f'df.loc["cobra", "mI"]:\n{df.loc["cobra", "mI"]}') # Series
print(f'df.loc[[("cobra", "mI")]]:\n{df.loc[[("cobra", "mI")]]}') # DF

cmIIshield = df.loc[('cobra', 'mII'), 'shield']
print(f'cmIIshield: {cmIIshield}')




import pandas as pd

from printit import printit


df = pd.DataFrame(
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
).set_index([0, 1]).rename_axis(['a', 'b'])
printit(df, 'df')


df.columns = pd.MultiIndex.from_tuples([('c', 'e'), ('d', 'f')],
                                       names=['level1', 'level2'])
printit(df, 'df')

df_drop_a = df.droplevel('a')
df_drop_l2 = df.droplevel('level2', axis=1)
printit(df_drop_a, 'drop a')
printit(df_drop_l2, 'drop l2')


import numpy as np
import pandas as pd

# pivot
df = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two', 'two'],
                   'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'baz': [1, 2, 3, 4, 5, 6],
                   'zoo': ['u', 'v', 'w', 'x', 'y', 'z']})
print(df)
print('\npivot')
print(df.pivot(index='foo', columns='bar', values='baz'))
print(df.pivot(index='foo', columns='bar')['baz'])
print(df.pivot(index='foo', columns='bar', values=['baz', 'zoo']))


df = pd.DataFrame({'lev1': [1, 1, 1, 2, 2, 2],
                   'lev2': [1, 1, 2, 1, 1, 2],
                   'lev3': [1, 2, 1, 2, 1, 2],
                   'lev4': [1, 2, 3, 4, 5, 6],
                   'values': [0, 1, 2, 3, 4, 5]})
print('\ndf')
print(df)
print(df.pivot(index='lev1', columns=['lev2', 'lev3'], values='values'))
print(df.pivot(index=['lev1', 'lev2'], columns=['lev3'], values='values'))


df = pd.DataFrame({'foo': ['one', 'one', 'two', 'two'],
                   'bar': ['A', 'A', 'B', 'C'],
                   'baz': [1, 2, 3, 4]})
try:
    p = df.pivot(index='foo', columns='bar', values='baz')
except ValueError as e:
    print(e) # Index contains duplicate entries, cannot reshape



# pivot_table
df = pd.DataFrame({'A': 5*['foo'] + 4*['bar'],
                   'B': 3*['one'] + 2*['two'] + 2*['one'] + 2*['two'],
                   'C': ['S', 'L', 'L', 'S', 'S', 'L', 'S', 'S', 'L'],
                   'D': [1, 2, 2, 3, 3, 4, 5, 6, 7],
                   'E': [2, 4, 5, 5, 6, 6, 8, 9, 9]})
print('\n\ndf')
print(df)
table = pd.pivot_table(
    df, values='D', index=['A', 'B'], columns=['C'], aggfunc=sum)
print('\npivot_table')
print(table)

table = pd.pivot_table(
    df, values='D', index=['A', 'B'], columns=['C'], aggfunc=sum, fill_value=0)
print(table)

table = pd.pivot_table(df,
                       values=['D', 'E'],
                       index=['A', 'C'],
                       aggfunc={'D': np.mean, 'E': np.median})
print(table)

table = pd.pivot_table(df,
                       values=['D', 'E'],
                       index=['A', 'C'],
                       aggfunc={'D': np.mean, 'E': [min, max, np.mean]})
print(table)

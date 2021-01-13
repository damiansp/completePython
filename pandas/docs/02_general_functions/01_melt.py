import pandas as pd



# melt
df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
                   'B': {0: 1,   1: 3,   2: 5},
                   'C': {0: 2,   1: 4,   2: 6}})
print(df)
print('\nmelt...')
print(pd.melt(df, id_vars=['A'], value_vars=['B']))
print(pd.melt(df, id_vars=['A'], value_vars=['B', 'C']))
print(
    pd.melt(df,
            id_vars=['A'],
            value_vars=['B'],
            var_name='varname',
            value_name='valname'))
print(pd.melt(df, id_vars=['A'], value_vars=['B', 'C'], ignore_index=False))

# w/ multi-index cols
df.columns = [list('ABC'), list('DEF')]
print('\nmulti-index col')
print(df)
print(pd.melt(df, col_level=0, id_vars=['A'], value_vars=['B']))
print(pd.melt(df, id_vars=[('A', 'D')], value_vars=[('B', 'E')]))




      

import pandas as pd


# Series
s1 = pd.Series(['a', 'b'])
s2 = pd.Series(['c', 'd'])
sc = pd.concat([s1, s2])
sc_reindex = pd.concat([s1, s2], ignore_index=True)
sc_multi = pd.concat([s1, s2], keys=['s1', 's2'])
sc_multi_named = pd.concat([s1, s2], keys=['s1', 's2'], names=['Series', 'Row'])
print(sc)
print(sc_reindex)
print(sc_multi)
print(sc_multi_named)



# DFs
df1 = pd.DataFrame([['a', 1], ['b', 2]], columns=['letter', 'number'])
df2 = pd.DataFrame([['c', 3], ['d', 4]], columns=['letter', 'number'])
dfc = pd.concat([df1, df2]) # vertical stack by default
print(dfc)

df3 = pd.DataFrame([['c', 3, 'cat'], ['d', 4, 'dog']],
                   columns=['letter', 'number', 'animal'])
dfc2 = pd.concat([df1, df3], sort=True) # sort colnames
dfc3 = pd.concat([df1, df3], sort=False)
print(dfc2)
print(dfc3)

df_inner = pd.concat([df1, df3], join='inner')
print(df_inner)

df4 = pd.DataFrame([['bird', 'polly'], ['monkey', 'george']],
                   columns=['animal', 'name'])
df_wide = pd.concat([df1, df4], axis=1)
print(df_wide)

df5 = pd.DataFrame([1], index=['a'])
df6 = pd.DataFrame([2], index=['a'])
try:
    bad_concat = pd.concat([df5, df6], verify_integrity=True)
except ValueError as e:
    print(e)

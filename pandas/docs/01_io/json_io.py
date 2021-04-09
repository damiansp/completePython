import os

import pandas as pd


# read_json
df = pd.DataFrame(
    [['a', 'b'], ['c', 'd']], index=['r1', 'r2'], columns=['c1', 'c2'])
dfj = df.to_json(orient='split')
print(dfj)

df2 = pd.read_json(dfj, orient='split')
print(df2)


dfj = df.to_json(orient='records')
print(dfj)

df2 = pd.read_json(dfj, orient='records')
print(df2)

dfj = df.to_json(orient='table')
print(dfj)

df2 = pd.read_json(dfj, orient='table')
print(df2)


# json_normalize
data = [{'id': 1, 'name': {'first': 'Coleen', 'last': 'Volk'}},
        {'name': {'given': 'Mose', 'family': 'Regner'}},
        {'id': 2, 'name': 'Faye Raker'}]
dfd = pd.json_normalize(data)
print(dfd)

data = [{'id': 1, 'name': 'Cal Volk', 'fit': {'h': 130, 'w': 60}},
        {'name': 'Mose Reg', 'fit': {'h': 130, 'w': 62}},
        {'id': 2, 'name': 'Fay Ray', 'fit': {'h': 127, 'w': 58}}]
dfd = pd.json_normalize(data, max_level=0)
print(dfd)

dfd = pd.json_normalize(data, max_level=1)
print(dfd)

data = [{'state': 'Florida',
         'abbr': 'FL',
         'info': {'gov': 'R. Scott'},
         'counties': [{'name': 'Dade', 'pop': 12345},
                      {'name': 'Broward', 'pop': 40000},
                      {'name': 'Palm Beach', 'pop': 60000}]},
        {'state': 'Ohio',
         'abbr': 'OH',
         'info': {'gov': 'J. Kasich'},
         'counties': [{'name': 'Summit', 'pop': 54321},
                      {'name': 'Cuyahoga', 'pop': 7117}]}]
res = pd.json_normalize(data, 'counties', ['state', 'abbr', ['info', 'gov']])
print(res)

data = {'A': [1, 2]}
dfd = pd.json_normalize(data, 'A', record_prefix='pref_')
print(dfd)


# build table schema
df = pd.DataFrame({'A': [1, 2, 3],
                   'B': ['a', 'b', 'c'],
                   'C': pd.date_range('2016-01-01', freq='d', periods=3)},
                  index=pd.Index(range(3), name='idx'))
schema = pd.io.json.build_table_schema(df)
print(schema)

import pandas as pd


d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)
print(df.dtypes)

print(df.astype('int32').dtypes)
print(df.astype({'col1': 'int32'}).dtypes)

s = pd.Series([1, 2], dtype='int32')
print(s)
print(s.astype('int64'))
print(s.astype('category'))

cat_dtype = pd.api.types.CategoricalDtype(categories=[2, 1], ordered=True)
print(s.astype(cat_dtype))

s1 = pd.Series([1, 2])
s2 = s1.astype('int64', copy=False)
s2[0] = 10
print(s1) # [10 2]

s_date = pd.Series(pd.date_range('20200101', periods=3))
print(s_date)

print(s_date.astype('datetime64[ns, US/Pacific]'))

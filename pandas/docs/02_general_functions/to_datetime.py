import pandas as pd


df = pd.DataFrame({'year': [2015, 2016], 'month': [2, 3], 'day': [4, 5]})
print(df)
print(pd.to_datetime(df))

print(pd.to_datetime('13000101', format='%Y%m%d', errors='ignore'))
# "out of bounds"
print(pd.to_datetime('13000101', format='%Y%m%d', errors='coerce')) 

s = pd.Series(['3/11/2000', '3/12/2000', '3/13/2000'] * 1000)
print(s.head())
print(pd.to_datetime(s, infer_datetime_format=True).head())
print(pd.to_datetime(s, infer_datetime_format=False).head())

# epoch time
print(pd.to_datetime(1490195805, unit='s'))
print(pd.to_datetime(1490195805433502912, unit='ns'))
      
print(pd.to_datetime([1, 2, 3], unit='D', origin=pd.Timestamp('1960-01-01')))

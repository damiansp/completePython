import pandas as pd


d = {'a': 1, 'b': 2, 'c': 3}
ser = pd.Series(data=d, index=d.keys())
print('ser:\n', ser)

ser2 = pd.Series(data=d, index=['c', 'd', 'e'])
print(f'ser2:\n{ser2}')

print('transpose:', ser.T)
print('array:', ser.array)
print('hasnans:', ser2.hasnans)
print('at["b"]:', ser.at['b'])
print('iat[1]:', ser.iat[1])
print('values:', ser.values)
print('add_prefix:\n', ser.add_prefix('not_')) # add_suffix
print('align:\n', ser.align(ser2))
print('align (inner):\n', ser.align(ser2, join='inner'))
print('all < 4:', (ser < 4).all())

ts = pd.Series([1, 2, 3, 4, 5, 6, 8, 10, 14])
print('AC:', ts.autocorr(lag=1))




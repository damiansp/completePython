import pandas as pd


us = pd.unique(pd.Series([2, 1, 3, 3]))
print('us:', us)

us2 = pd.unique(pd.Series([2] + [1] * 5))
print('us2:', us2)

uts = pd.unique(pd.Series([pd.Timestamp('19761103'), pd.Timestamp('19761103')]))
print('uts:', uts)

uts2 = pd.unique(
    pd.Series([pd.Timestamp('19761103', tz='US/Central'),
               pd.Timestamp('19761103', tz='US/Central')]))
print('uts2:', uts2)

utsi = pd.unique(
    pd.Index([pd.Timestamp('19761103', tz='US/Central'),
              pd.Timestamp('19761103', tz='US/Central')]))
print('utsi:', utsi)

uc = pd.unique(list('baabc'))
print('uc:', uc)

ucat = pd.unique(pd.Series(pd.Categorical(list('baabbc'))))
print('ucat:', ucat)

ucat2 = pd.unique(
    pd.Series(pd.Categorical(list('baabbc'), categories=list('abc'))))
print('ucat2:', ucat2)

ucato = pd.unique(
    pd.Series(
        pd.Categorical(list('baabbc'), categories=list('abc'), ordered=True)))
print('ucato:', ucato)

ut = pd.unique([('a', 'b'), ('b', 'a'), ('c', 'a'), ('b', 'a')])
print('ut:', ut)







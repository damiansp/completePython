import pandas as pd


print(pd.timedelta_range(start='1 day', periods=4))
print(pd.timedelta_range(start='1 day', periods=4, closed='right'))
print(pd.timedelta_range(start='1 day', end='2 days',  freq='6H'))
print(pd.timedelta_range(start='1 day', end='5 days',  periods=4))



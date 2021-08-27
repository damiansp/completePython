import pandas as pd


s = pd.Series({'falcon': 330., 'eagle': 160.})
print(f's:\n{s}')

s2 = pd.Series({'falcon': 345, 'eagle': 200, 'duck': 30})
print(f's2:\n{s2}')

c = s.combine(s2, max)
print(f'c:\n{c}')

c2 = s.combine(s2, max, fill_value=0)
print(f'c2:\n{c2}')

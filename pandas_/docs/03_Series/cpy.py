import pandas as pd


s = pd.Series([1, 2], index=['a', 'b'])
print(s)

sc = s.copy()
print(sc)

deep = s.copy()
shallow = s.copy(deep=False)
print(s is shallow) # False (diff obj in memory)
print(s.values is shallow.values and s.index is shallow.index) # True
print(s is deep) # False
print(s.values is deep.values and s.index is deep.index) # False

s[0] = 999
shallow[1] = -1
print(s)       # 999 -1
print(shallow) # 999 -1
print(deep)    #   1  2

s = pd.Series([[1, 2], [3, 4]])
deep = s.copy()
s[0][0] = 999
print(s)    # [[999 2][3 4]]
print(deep) # [[999 2][3 4]]!

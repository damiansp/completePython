import pandas as pd


s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])
s3 = pd.Series([4, 5, 6], index=[3, 4, 5])

s13 = s1.append(s3)
print(f's13\n{s13}')

s12 = s1.append(s2, ignore_index=True)
print(f's12\n{s12}')

s1.append(s2, verify_integrity=True) # ValueError (overlapping indices)

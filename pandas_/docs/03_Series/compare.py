import pandas as pd


s1 = pd.Series(['a', 'b', 'c', 'd', 'e'])
s2 = pd.Series(['a', 'a', 'c', 'b', 'e'])
print(s1.compare(s1, align_axis=0))
print(s1.compare(s2))
print(s1.compare(s2, align_axis=0))

print(s1.compare(s2, keep_shape=True))
print(s1.compare(s2, keep_shape=True, keep_equal=True))



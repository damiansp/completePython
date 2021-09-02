import pandas as pd


s1 = pd.Series([0.9001, 0.1348, 0.6204])
s2 = pd.Series([0.1253, 0.2696, 0.5111])
print(s1.cov(s2))

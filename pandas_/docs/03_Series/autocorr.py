import pandas as pd


s = pd.Series([0.25, 0.5, 0.2, -0.05])
print(s.autocorr())
print(s.autocorr(lag=2))

import pandas as pd


x = pd.qcut(range(5), 4) # 4 quantile bins
print(x)

x_lab = pd.cut(range(5), 3, labels=['low', 'med', 'high'])
print(x_lab)

x_bin = pd.cut(range(5), 3, labels=False)
print(x_bin)

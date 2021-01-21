import numpy as np
import pandas as pd


x = np.array([1, 7, 5, 4, 6, 3])
xcut3 = pd.cut(x, 3) # 3 bins of equal size
print(xcut3)

xcut3, bindivs = pd.cut(x, 3, retbins=True)
print()
print(xcut3)
print()
print(bindivs)

xcut3_labeled = pd.cut(x, 3, labels=['low', 'med', 'high'])
print(xcut3_labeled)

xcut3_labeled2 = pd.cut(x, 3, labels=['B', 'A', 'B'], ordered=False)
print(xcut3_labeled2)

y = [0, 1, 1, 2]
ybins = pd.cut(y, bins=4, labels=False)
print(ybins)

s = pd.Series(np.array([2, 4, 6, 8, 10]), index=['a', 'b', 'c', 'd', 'e'])
print(s)
scut3 = pd.cut(s, 3)
print(scut3)

scut_bins = pd.cut(
    s, [0, 2, 4, 6, 8, 10], labels=False, retbins=True, right=False)
print(scut_bins)

scut_bins2 = pd.cut(s,
                    [0, 2, 4, 6, 10, 10],
                    labels=False,
                    retbins=True,
                    right=False,
                    duplicates='drop')
print(scut_bins2)


bins = pd.IntervalIndex.from_tuples([(0, 1), (2, 3), (4, 5)])
z = [0, 0.5, 1.5, 2.5, 4.5]
z_binned = pd.cut(z, bins)
print(z_binned)

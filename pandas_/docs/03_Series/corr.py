import numpy as np
import pandas as pd


def histogram_intersection(a, b):
    v = np.minimum(a, b).sum().round(1)
    return v


s1 = pd.Series([0.2, 0., 0.6, 0.2])
s2 = pd.Series([0.3, 0.6, 0., 0.1])
print(s1.corr(s2, method=histogram_intersection))

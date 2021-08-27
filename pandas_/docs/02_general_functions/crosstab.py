import numpy as np
import pandas as pd


a = np.array(["foo", "foo", "foo", "foo", "bar", "bar", "bar", "bar", "foo",
              "foo", "foo"],
             dtype=object)
b = np.array(["one", "one", "one", "two", "one", "one", "one", "two", "two",
              "two", "one"],
             dtype=object)
c = np.array(["dull", "dull", "shiny", "dull", "dull", "shiny", "shiny", "dull",
              "shiny", "shiny", "shiny"],
             dtype=object)

xtab = pd.crosstab(a, [b, c], rownames=['a'], colnames=['b', 'c'])
print(xtab)


foo = pd.Categorical(['a', 'b'], categories=['a', 'b', 'c'])
bar = pd.Categorical(['d', 'e'], categories=['d', 'e', 'f'])
xtab2 = pd.crosstab(foo, bar)
print(xtab2)

xtab3 = pd.crosstab(foo, bar, dropna=False)
print(xtab3)

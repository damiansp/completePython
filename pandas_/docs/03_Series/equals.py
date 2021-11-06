import pandas as pd

from printit import printit


df = pd.DataFrame({1: [10], 2: [2]})
printit(df, 'df')

same = pd.DataFrame({1: [10], 2: [2]})
print(df.equals(same)) # True

similar = pd.DataFrame({1.0: [10], 2.0: [2]})
print(df.equals(similar)) # True

similarish = pd.DataFrame({1: [10.], 2: [20.]})
print(df.equals(similarish)) # False

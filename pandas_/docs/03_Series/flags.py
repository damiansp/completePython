import pandas as pd


df = pd.DataFrame({'A': [1, 2]})
print(f'df.flags: {df.flags}')
print(f'df.flags.allows_duplicate_labels: {df.flags.allows_duplicate_labels}')

df.flags.allows_duplicate_labels = False
print(f'df.flags.allows_duplicate_labels: {df.flags.allows_duplicate_labels}')

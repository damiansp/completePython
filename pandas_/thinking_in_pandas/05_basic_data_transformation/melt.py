import pandas as pd


df = pd.DataFrame({
    'restaurant': ['Diner', 'Pandas'],
    'location': [(4, 2), (5, 4)],
    0: [90, 55],
    1: [100, 76]})
dfm = df.melt(
    id_vars=['restaurant', 'location'],
    value_vars=[0, 1],
    value_name='score'
).drop(columns='variable')  # variable: [0, 0, 1, 1]
print(dfm)
    

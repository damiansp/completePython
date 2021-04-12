import pandas as pd


dicts = [{'a': 1,   'b': 2,   'c': 3,   'd': 4},
         {'a': 10,  'b': 20,  'c': 30,  'd': 40},
         {'a': 100, 'b': 200, 'c': 300, 'd': 400}]
df = pd.DataFrame(dicts)
print(f'df:\n{df}')
print('type(df.iloc[0]):', type(df.iloc[0])) # Series
print(f'df.iloc[0]:\n{df.iloc[0]}')
print('type(df.iloc[[0]]):', type(df.iloc[[0]])) # DF
print(f'df.iloc[[0]]:\n{df.iloc[[0]]}')
print(f'df.iloc[[0, 1]]:\n{df.iloc[[0, 1]]}')
print(f'df.iloc[:3]:\n{df.iloc[:3]}')
print(f'df.iloc[[True, False, True]]:\n{df.iloc[[True, False, True]]}')
print('df.iloc[1, 2]:', df.iloc[1, 2]) # 30
print(f'df.iloc[[0, 2], [1, 3]]:\n{df.iloc[[0, 2], [1, 3]]}')


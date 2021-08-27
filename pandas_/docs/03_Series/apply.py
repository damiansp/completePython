import pandas as pd


s = pd.Series([20, 21, 12], index=['London', 'New York', 'Helsinki'])
print(f's:\n{s}')

def sq(x):
    return x * x

ssq = s.apply(sq)
ssq2 = s.apply(lambda x: x ** 2)
print(f'ssq:\n{ssq}\nssq2:\n{ssq2}')

def subtract_val(x, val):
    return x - val

sless = s.apply(subtract_val, args=(10,))
print(f'sless:\n{sless}')

def add_vals(x, **kwargs):
    for _, v in kwargs.items():
        x += v
    return x

smore = s.apply(add_vals, me=10, you=11, her=22)
print(f'smore:\n{smore}')

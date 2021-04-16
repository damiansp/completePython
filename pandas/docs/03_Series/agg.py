import pandas as pd


s = pd.Series([1, 2, 3, 4, 5, 6])
mn = s.agg('min')
print('mn:', mn)

mn_mx = s.agg(['min', 'max'])
print('mn_mx:', mn_mx)

def count_if_even(a):
    return sum([1 for x in a if x % 2 == 0])

n_even = s.agg(count_if_even)
print('n_even:', n_even)

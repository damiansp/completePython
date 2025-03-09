a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

common_keys = a.keys() & b.keys()
print(common_keys)  # x, y

a_only_keys = a.keys() - b.keys()
print(a_only_keys)  # z

common_kv_pairs = a.items() & b.items()
print(common_kv_pairs)  # y, 2

c = {k: a[k] for k in a.keys() - {'z', 'w'}}
print(c)

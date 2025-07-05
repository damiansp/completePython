from collections import ChainMap


a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)
print(c['x'])  # 1 from a
print(c['y'])  # 2 from b
print(c['z'])  # 3 from a

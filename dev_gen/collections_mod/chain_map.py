from collections import ChainMap


d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
c = ChainMap(d1, d2, d3)
print(c)
print(c['a'])
print(c['e'])
print(c.keys())
for k in c.keys():
    print(k)
print(c.values())
for k, v in c.items():
    print(f'{k}: {v}')

d4 = {'g': 7, 'h': 8}
c = c.new_child(d4)
print(c)

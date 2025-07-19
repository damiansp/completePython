from collections import ChainMap


a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)
print(c['x'])  # 1 from a
print(c['y'])  # 2 from b
print(c['z'])  # 3 from a


values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3
print(values)
print(values['x'])  # 3
values = values.parents
print(values['x'])  # 2

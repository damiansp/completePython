from collections import defaultdict


s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

print(sorted(d.items()))  # blue [2, 4], yellow [1, 3], red [1]


d = {}
for k, v in s:
    d.setdefault(k, []).append(v)

print(sorted(d.items()))  # blue [2, 4], red [1], yellow [1, 3]


def constant_factory(val):
    return lambda: val


d = defaultdict(constant_factory('<missing>'))
d.update(name='John', action='ran to')
print('%(name)s %(action)s %(location)s' % d)

# pretty sure that since py3, all dicttionaries default to ordered....
from collections import OrderedDict

d = {}
od = OrderedDict()

for k, v in zip(list('abcd'), [1, 2, 3,4]):
    d[k] = v
    od[k] = v

    
def print_dict(d):
    for k, v in d.items():
        print(f'{k}: {v}')

        
print('Dict:')
print_dict(d)
print('Ordered:')
print_dict(od)

od.pop('a')
od['a'] = 1

del d['a']
d['a'] = 1

print('\nDict:')
print_dict(d)
print('Ordered:')
print_dict(od)

# ...yep, looks like behavior is identical

import argparse
import builtins
from collections import ChainMap
import os


baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
print(list(ChainMap(adjustments, baseline)))

combined = baseline.copy()
combined.update(adjustments)
print(list(combined))  # same

pylookup = ChainMap(locals(), globals(), vars(builtins))

defaults = {'color': 'red', 'user': 'guest'}
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v is not None}
combined = ChainMap(command_line_args, os.environ, defaults)
print(combined['color'])
print(combined['user'])

c = ChainMap()
d = c.new_child()
e = c.new_child()
print(e.maps[0])
print(e.maps[-1])
print(e.parents)
d['x'] = 1
print(d['x'])
del d['x']
print(list(d))
print(len(d))
print(d.items())
print(dict(d))


class DeepChainMap(ChainMap):
    def __setitem__(self, k, v):
        for mapping in self.maps:
            if k in mapping:
                mapping[k] = v
                return
        self.maps[0][k] = v

    def __delitem__(self, k):
        for mapping in self.maps:
            if k in mapping:
                del mapping[k]
                return
        raise KeyError(k)


d = DeepChainMap({'zebra': 'black'}, {'elephant': 'blue'}, {'lion': 'yellow'})
d['lion'] = 'orange'
d['snake'] = 'red'
del d['elephant']
print(d)

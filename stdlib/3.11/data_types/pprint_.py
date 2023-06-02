import json
import pprint
from urllib.request import urlopen


stuff = ['spam', 'eggs', 'lumberjacks', 'knights', 'ni']
stuff.insert(0, stuff[:])
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(stuff)

pp = pprint.PrettyPrinter(width=41, compact=True)
pp.pprint(stuff)

tup = (
    'spam',
    ('eggs',
     ('lumberjack', ('knights', ('ni', ('dead', ('parrot', ('fresh fruit',))))))))
pp = pprint.PrettyPrinter(depth=6)
pp.pprint(tup)


stuff = ['spam', 'eggs', 'lumberjacks', 'knights', 'ni']
stuff.insert(0, stuff)
pprint.pprint(stuff)

print(pprint.isreadable(stuff))
print(pprint.saferepr(stuff))


with urlopen('https://pypi.org/pypi/sampleproject/json') as resp:
    project_info = json.load(resp)['info']


pprint.pprint(project_info, depth=1, width=70)
pprint.pprint(project_info)

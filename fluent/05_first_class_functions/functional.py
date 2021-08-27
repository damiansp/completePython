from collections import namedtuple
from functools import partial, reduce
from operator import attrgetter, itemgetter, methodcaller, mul
from unicodedata import normalize

def fact(n):
    return reduce(lambda a, b: a*b, range(1, n + 1))

def fac2(n):
    return reduce(mul, range(1, n + 1))


metro_data = [('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
              ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
              ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
              ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
              ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))]

for city in sorted(metro_data, key=itemgetter(1)):
    print(city)

cc_name = itemgetter(1, 0)
for city in metro_data:
    print(cc_name(city))

LatLon = namedtuple('LatLon', 'lat lon')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [Metropolis(name, cc, pop, LatLon(lat, lon))
               for name, cc, pop, (lat, lon) in metro_data]
print(metro_areas[0])
print(metro_areas[0].coord.lat)

name_lat = attrgetter('name', 'coord.lat')
for city in sorted(metro_areas, key=attrgetter('coord.lat')):
    print(name_lat(city))

#print([name for name in dir(operator) if not name.startswith('_')])

s = 'The time has come'
upcase = methodcaller('upper')
print(upcase(s))

hyphenate = methodcaller('replace', ' ', '-')
print(hyphenate(s))

triple = partial(mul, 3)
print(triple(7))
print(list(map(triple, range(10))))

nfc = partial(normalize, 'NFC')
s1 = 'café'
s2 = 'cafe\u0301'
print(s1 == s2)           # False
print(nfc(s1) == nfc(s2)) # True


def tag(name, *content, cls=None, **attributes):
    '''Genearate one or more HTML tags'''
    if cls is not None:
        attributes['class'] = cls
    if attributes:
        attribute_str = ''.join(' %s="%s"' % (attr, value)
                                for attr, value in sorted(attributes.items()))
    else:
        attribute_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attribute_str, c, name)
                         for c in content)
    else:
        return '<%s%s />' % (name, attribute_str)


picture = partial(tag, 'img', cls='pic-frame')
print(picture(src='wumpus.jpg'))
print(picture)
print(picture.func)
print(picture.args)
print(picture.keywords)

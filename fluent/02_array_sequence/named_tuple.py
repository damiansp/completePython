from collections import namedtuple

Coordinates = namedtuple('Coordinates', ['lat', 'lon']) # same as:
#Coordinates = namedtuple('Coordinates', 'lat lon')
City = namedtuple('City', ['name', 'country', 'population', 'coordinates'])

tokyo = City('Tokyo', 'JP', 36.933, Coordinates(35.6897, 139.6917))
print(tokyo)
print(tokyo.population)
print(tokyo[1])
print(tokyo.coordinates.lat)
print(City._fields)

delhi_data = ('Delhi', 'IN', 21.935, Coordinates(28.6139, 77.2089))
delhi = City._make(delhi_data)
print(delhi._asdict())

for k, v in delhi._asdict().items():
    print('%s: %s' % (k, v))

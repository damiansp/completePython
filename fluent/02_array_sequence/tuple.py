import os

# tuples as records
lax_coords = (33.9425, -118.408056)
city, year, pop, chg, area = 'Tokyo', 2003, 32450, 0.66, 8104
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)


# Unpacking
lat, lon = lax_coords

print(divmod(20, 8))

t = (20, 8)
print(divmod(*t))

quotient, remainder = divmod(*t)

path = 'some/long/path/and/a/file.ext'
_, filename = os.path.split(path)
print(filename)

a, b, *rest = range(10)
print(a, b, rest)

metro_areas = [('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
               ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
               ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
               ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
               ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))]
print('{:15} | {:^9} | {:^9}'.format('', 'lat', 'lon'))
fmt = '{:15} | {:9.4f} | {:9.4f}'

for name, cc, pop, (lat, lon) in metro_areas:
    if lon <= 0: # W hemisphere
        print(fmt.format(name, lat, lon))
      

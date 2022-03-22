import datetime
from string import Template


# Format string syntax
class Person:
    def __init__(self, name):
        self.name = name

worker = Person('Bob Dobolina')
fruits = ['tangerine', 'durian', 'kiwi']

print('First, thou shalt count to {0}'.format('three'))
print('Bring out {}'.format('Rodrick'))
print('From {} to {}'.format('here', 'there'))
print('My quest is {name}'.format(name='the grail'))
print('The worker is named: {0.name}'.format(worker))
print('My favorite fruit is {fruits[2]}'.format(fruits=fruits))
print('{0!s} is right out!'.format(5))
print('{}, {}, {}'.format('b', 'a', 't'))
print('{2}, {1}, {0}'.format('b', 'a', 't'))
print('{1}{2} {0}{1}{2}'.format('b', 'a', 't'))
print('{2}, {1}, {0}'.format(*'bat'))
print('Coords: {lat}, {lon}'.format(lat='37.24N', lon='-115.86W'))

coords = {'lat': '32.24N', 'lon': '-115.86W'}
print('Coords: {lat}, {lon}'.format(**coords))

c = 3-5j
print('The complex number {0} is formed from a real part {0.real}, and an '
      'imaginary par {0.imag}'.format(c))


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return 'Point({self.x}, {self.y})'.format(self=self)

print(Point(3, 4))

coords = (3, 5)
print('X: {0[0]}, Y: {0[1]}'.format(coords))
print("repr() shows quotes: {!r}, str() doesn't: {!s}".format('test1', 'test2'))
print('{:<30}.'.format('left aligned'))
print('{:^30}.'.format('centered'))
print('{:~^30}.'.format('centered'))
print('{:>30}.'.format('right aligned'))
print('{:+f}; {:+f}'.format(3.14, -3.14))
print('{: f}; {: f}'.format(3.14, -3.14))
print('{:-f}; {:-f}'.format(3.14, -3.14))  # same as just {:f}
print('dec: {0:d}; hex: {0:x}; oct: {0:o}; bin: {0:b}'.format(1976))
print('dec: {0:d}; hex: {0:#x}; oct: {0:#o}; bin: {0:#b}'.format(45))
print('{:,}'.format(1234567890))

points = 19
total = 20
print('Score: {:.2%}'.format(points / total))

d = datetime.datetime(2010, 7, 4, 12, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))

for align, text in zip('<^>', ['left', 'center', 'right']):
    '{0:{fill}{align}16}'.format(text, fill=align, align=align)

octets = [192, 168, 0, 1]
print('{:02X}{:02X}{:02X}{:02X}'.format(*octets))

width = 5
for n in range(5, 12):
    for base in 'dXob':
        print('{0:{width}{base}}'.format(n, base=base, width=width), end=' ')
    print()


# Templates
s = Template('$who likes $what')
print(s.substitute(who='Tim', what='Gongbao ji ding'))
d = {'who': 'Tim'}
t = Template('Give $who $100')
try:
    print(t.substitute(d))
except ValueError:
    print(t.safe_substitute(d))

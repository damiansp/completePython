from collections import namedtuple


Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
print(p[0] + p[1])
x, y = p
print(x, y)
print(p.x + p.y)
print(p)

t = [11, 22]
print(Point._make(t))
print(p._asdict())
q = p._replace(x=33)
print(p)
print(q)

print(p._fields)
Color = namedtuple('Color', 'red green blue')
Pixel = namedtuple('Pixel', Point._fields + Color._fields)
px = Pixel(11, 22, 128, 255, 0)
print(px)

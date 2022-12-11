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

Account = namedtuple('Account', ['type', 'balance'], defaults=[0])
print(Account._field_defaults)
print(Account('premium'))

print(getattr(p, 'x'))

d = {'x': 11, 'y': 22}
print(Point(**d))


class Point(namedtuple('Point', ['x', 'y'])):
    __slots__ = ()

    @property
    def hypot(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return f'Point ({self.x:.4f}, {self.y:.4f})'


for p in Point(3, 4), Point(14, 5/7):
    print(f'{p}, {p.hypot:.4f}')


Point3D = namedtuple('Point3D', Point._fields + ('z',))


Book = namedtuple('Book', ['id', 'title', 'authors'])
Book.__doc__ += ': Hardcover book in active collection'
Book.id.__doc__ = '13-digit ISBN'
Book.title.__doc__ = 'Title of first printing'
Book.authors.__doc__ = 'List of authors sorted by last name'

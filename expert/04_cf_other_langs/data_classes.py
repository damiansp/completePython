from dataclasses import dataclass, field


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        '''Add two vectors'''
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        '''Subtract one vector from another'''
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f'[{self.x}, {self.y}]'

    def __repr__(self):
        return f'<Vector: x={self.x}, y={self.y}>'

    def __eq__(self, other):
        '''Test for equality between two vectors'''
        return self.x == other.x and self.y == other.y


# Ex
v = Vector(2, 3)
w = Vector(1, 2)
print(v)
print(v + w)
print(v - w)
print(v == w)


@dataclass
class Vec:
    x: int
    y: int

    def __add__(self, other):
        '''Add two vectors'''
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        '''Subtract one vector from another'''
        return Vec(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f'[{self.x}, {self.y}]'

    def __eq__(self, other):
        '''Test for equality between two vectors'''
        return self.x == other.x and self.y == other.y

v = Vec(2, 3)
w = Vec(1, 2)
print(v)
print(v + w)
print(v - w)
print(v == w)


@dataclass(frozen=True) # now immutable
class FrozenVec:
    x: int
    y: int
    # ...


@dataclass
class DataClassWithDefaults:
    immutable: str = field(default='this is the static default value')
    mutable: list = field(default_factory=list)

print(DataClassWithDefaults())
print(DataClassWithDefaults('This is immutable'))
print(DataClassWithDefaults(None, ['this', 'is', 'a', 'list']))

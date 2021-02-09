from math import sqrt

from .util import format_number


class Vector2:
    __slots__ = ('_v',)
    _gameobjects_vector = 2
    
    def __init__(self, x=0., y=0.):
        '''
        Initialize a vector
        Args:
          - x (number): x-component
          - y (number): y-component
        '''
        if hasattr(x, '__getitem__'):
            x, y = x
            self._v = [float(x), float(y)]
        else:
            self._v = [float(x), float(y)]
        #self._magnitude = self._get_length()

    def _get_length(self):
        x, y = self._v
        return sqrt(x**2 + y**2)

    def _set_length(self, length):
        v = self._v
        try:
            x, y = v
            l = length / sqrt(x**2 + y**2)
        except ZeroDivisionError:
            v[0] = 0.
            v[1] = 0.
            return self
        v[0] *= l
        v[1] *= l

    length = property(_get_length, _set_length, None, 'Length of the vector')

    @classmethod
    def from_floats(cls, x, y):
        vec = cls.__new__(cls, object)
        vec._v = [x, y]
        return vec
    

    def __getitem__(self, index):
        return self._v[index]

    def __setitem__(self, index, val):
        self._v[index] = 1. * val
        
    @property
    def magnitude(self):
        return self._magnitude

    def __str__(self):
        return f'({self.x}, {self.y})'

    def from_points(p1, p2):
        return Vector2(p2[0] - p1[0], p2[1] - p1[1])

    def normalize(self):
        self.x /= self._magnitude
        self.y /= self._magnitude
        self._magnitude = self._calculate_magnitude()

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __mul__(self, scalar):
        return Vector2(scalar * self.x, scalar * self.y)

    def __truediv__(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)


if __name__ == '__main__':
    A = (10., 20.)
    B = (30., 35.)
    C = (15., 45.)

    def test_from_points():
        AB = Vector2.from_points(A, B)
        print(AB)
        print('Magnitude:', AB.magnitude)

    def test_normalize():
        AB = Vector2.from_points(A, B)
        print(AB)
        print('Magnitude:', AB.magnitude)
        AB.normalize()
        print(AB)
        print('Magnitude:', AB.magnitude)

    def test_add():
        AB = Vector2.from_points(A, B)
        BC = Vector2.from_points(B, C)
        AC = Vector2.from_points(A, C)
        print('AC:', AC)
        AC = AB + BC
        print('AB + BC =', AC)
        
    def run_tests():
        #test_from_points()
        #test_normalize()
        test_add()

    run_tests()

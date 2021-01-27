import math


class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self._magnitude = self._calculate_magnitude()

    @property
    def magnitude(self):
        return self._magnitude

    def _calculate_magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

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

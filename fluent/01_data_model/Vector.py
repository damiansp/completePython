from math import hypot


def main():
    test()


def test():
    add_test()
    abs_test()
    mul_test()
    print('All tests passed!')
    

def add_test():
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    assert(v1 + v2 == Vector(4, 5))
    print('addition_test passed')


def abs_test():
    v = Vector(3, 4)
    assert(abs(v) == 5.)
    print('abs_test passed')


def mul_test():
    v = Vector(3, 4)
    assert(v * 3 == Vector(9, 12))
    print('mul_test passed')


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        #return bool(abs(self))       # clearer
        return bool(self.x or self.y) # faster

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
    

if __name__ == '__main__':
    main()

import sys


match sys.platform:
    case 'windows':
        print('Running on Windows')
    case 'darwin':
        print('Running on OSX')
    case 'linux':
        print('Running on Linux')
    case _:
        raise NotImplementedError(f'{sys.platform} not supported')


for i in range(100):
    match (i % 3, i % 5):
        case (0, 0): print('FizzBuzz')
        case (0, _): print('Fizz')
        case (_, 0): print('Buzz')
        case _: print(i, end=' ')


class Point:
    x: int
    y: int
    
    def __init__(self, x, y):
        self.x = x
        self.y = y


def where_is(point):
    match point:
        case Point(x=0, y=0):
            print('Origin')
        case Point(x=0, y=y):
            print(f'y-axis at {y}')
        case Point(x=x, y=0):
            print(f'x-axis at {x}')
        case Point():
            print('In the great expanse')
        case _:
            print('Not a Point')


class LePoint:
    x: int
    y: int
    __match_args__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y


def ou_est(point):
    match point:
        case LePoint(0, 0):
            print("L'origine")
        case Point(0, y):
            print(f"l'axis y a {y}")
        case Point(x, 0):
            print(f"l'axis x a {x}")
        case Point():
            print('Sur le grand expanse')
        case _:
            print("C'est pas un point")

from enum import Enum


def http_error(status):
    match status:
        case 400:
            return 'Bad Request'
        case 404:
            return 'Not Found'
        case 418:
            return "I'm a little teapot (short and stout)"
        case 200 | 202:
            return  "Well that's somethin'"
        case _:
            return 'Strange things are afoot on the internets'


# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

    
class Point:
    x: int
    y: int

    
def location(point):
    match point: # where point is a tuple (x, y)
        case Point(0, 0):
            print('Origin')
        case Point(0, y):
            print(f'y={y}')
        case Point(x, 0):
            print(f'x={x}')
        case Point():
            print(f'x={x}, y={y}')
        case _:
            raise ValueError('Not a point')


match points: # where points is a list of Points
    case []:
        print('No points in the list.')
    case [Point(0, 0)]:
        print('The origin is the only point in the list.')
    case [Point(x, y)]:
        print(f'A single point {x}, {y} is in the list.')
    case [Point(0, y1), Point(0, y2)]:
        print(f'Two points on the y-axis at {y1}, {y2} are in the list.')
    case _:
        print('Something else is found in the list.')


match test_variable:
    case ('warning', code, 40):
        print("A warning has been received.")
    case ('error', code, _):
        print(f"An error {code} occurred.")


match point:
    case Point(x, y) if x == y:
        print(f'The point is located on the diagonal y=x at {x}.')
    case Point(x, y):
        print(f'Point is not on the diagonal.')


# case (Point(x1, y1), Point(x2, y2) as p2): ...


class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2


match color:
    case Color.BLUE:
        print('I see skies of blue')
    case Color.RED:
        print('Red roses too')
    case Color.GREEN:
        print('And I think to myself, "what a wonderful world"')


# Type Union
def square(n: Union[int, float]) -> Union[int, float]:
    return n ** 2

# Same as:
def sq(n: int | float) -> int | float:
    return n **2

print(isinstance(1, int | str))


# Type alias
StrCache: TypeAlias = 'Cache[str]' # type alias
LOG_PREFIX = 'LOG[DEBUG]'

import math


def get_circle_area(r):
    return math.pi * r**2


R = 42
print(get_circle_area(R))
print(get_circle_area)
print(get_circle_area.__class__)
print(get_circle_area.__name__)

get_c_area = lambda r: math.pi * r**2
print()
print(get_c_area(R))
print(get_c_area)
print(get_c_area.__class__)
print(get_c_area.__name__)



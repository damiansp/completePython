from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(type(Color.RED))  # <enum 'Color'>
print(isinstance(Color.RED, Color))  # True
print(Color.RED.name)   # RED
print(Color.RED.value)  # 1
print(Color.RED in Color)  # True
print(Color.RED == 1)      # False
print(Color.RED is 1)      # False

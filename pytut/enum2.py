from enum import Enum
from pprint import pprint


class Color(Enum):
    RED = 1
    CRIMSON = 1
    SCARLET = 1
    GREEN = 2
    BLUE = 3


print(Color.RED is Color.CRIMSON)  # True
print(Color(1))  # RED
for color in Color:
    print(color)  # RED, GREEN, BLuE
pprint(Color.__members__)  # shows all

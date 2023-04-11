from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

MyColors = Enum('MyColors', ['RED', 'GREEN', 'BLUE'])


c = Color
print(c.RED)

print(MyColors.GREEN)

from datetime import date
from enum import auto, Enum, Flag, IntEnum  #, StrEnum (3.11)


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

MyColors = Enum('MyColors', ['RED', 'GREEN', 'BLUE'])


c = Color
print(c.RED)

print(MyColors.GREEN)

some_var = Color.RED
print(some_var in Color)

print(Color.GREEN)
print(Color['BLUE'])
print(list(Color))
print(len(Color))
print(Color.BLUE.name)
print(Color.BLUE.value)


class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    @classmethod
    def today(cls):
        print(f'Today is {cls(date.today().isoweekday()).name}')

Weekday.today()


class PowersOfThree(Enum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return 3 ** (count + 1)
    FIRST = auto()
    SECOND = auto()
    THIRD = auto()

print(PowersOfThree.THIRD.value)


'''  # 3.11+
class Build(StrEnum):
    DEBUG = auto()
    OPTIMIZED = auto()

    @classmethod
    def _missing_(cls, value):
        value = value.lower()
        for member in cls:
            if member.value == value:
                return member
        return None

print(Build.DEBUG.value)
print(Build('deBuG'))
'''


class OtherStyle(Enum):
    ALTERNATE = auto()
    OTHER = auto() 
    SOMETHING_ELSE = auto()

    def __repr__(self):
        cls_name = self.__class__.__name__
        return f'{cls_name}.{self.name}'

    def __str__(self):
        return f'{self.name}'

    def __format__(self, spec):
        return f'{self.name}'
    

print(
    OtherStyle.ALTERNATE, str(OtherStyle.ALTERNATE), f'{OtherStyle.ALTERNATE}')
print(
    repr(OtherStyle.ALTERNATE),
    repr(str(OtherStyle.ALTERNATE)),
    repr(f'{OtherStyle.ALTERNATE}'))


class Numbers(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3


print(Numbers.THREE)
print(Numbers.ONE + Numbers.TWO)
print(Numbers.TREE + 5)
print(Numbers.TWO == 2)


class Color(Flag):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

purple = Color.RED | Color.BLUE
white = Color.RED | Color.BLUE | Color.GREEN
print(Color.GREEN in purple)
print(purple in white)
print(white in purple)
print(list(purple))
print(len(Color.GREEN), len(white))




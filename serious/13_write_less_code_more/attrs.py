import attr


class OldCar:
    def __init__(self, color, speed=0):
        self.color = color
        self.speed = speed


@attr.s
class Car:
    color = attr.ib(converter=str)
    speed = attr.ib(default=0)

    @speed.validator
    def validate_speed(self, attribute, val):
        if val < 0:
            raise ValueError('Value cannot be negative')

        
c = Car('blue')
print(c)

try:
    d = Car('red', -5)
except ValueError as e:
    print(e)


@attr.s(frozen=True)
class CoolCar:
    color = attr.ib(converter=str)
    speed = attr.ib(default=0)

    @speed.validator
    def validate_speed(self, attribute, val):
        if val < 0:
            raise ValueError('Value cannot be negative')


cc = CoolCar('blue')
try:
    cc.color = 'red'
except BaseException as e:
    print('Cannot change color')
    print(e)
print(cc.color)

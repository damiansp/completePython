from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.w = width
        self.h = height

    def area(self):
        return self.w * self.h


class Circle(Shape):
    def __init__(self, radius):
        self.r = radius

    def area(self):
        return pi * self.r**2


def print_area(shape: Shape):
    print(f'The area is {shape.area()}')


rect = Rectangle(5, 10)
circ = Circle(3.75)

print_area(rect)
print_area(circ)

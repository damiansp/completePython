from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def n_sides(self):
        pass


class Triangle(Polygon):
    def n_sides(self):
        return 3


class Rectangle(Polygon):
    def n_sides(self):
        return 4


class BadPoly(Polygon):
    def __init__(self, n_sides):
        self.n_sides = n_sides


tdog = Triangle()
rex = Rectangle()
try:
    baddie = BadPoly()
except TypeError as e:
    print(e)


class Parent:
    def geek_out(self):
        print('Hardy har har')


class Child(Parent):
    def geek_out(self):
        print('Like father, like son: hardy har har')


print(issubclass(Child, Parent))    # True
print(isinstance(Child(), Parent))  # True


class Elder(ABC):
    def tell_it(self):
        print('Abstract Base Class')


class Minor(Elder):
    def tell_it(self):
        super().tell_it()
        print('subclass')


pliny = Minor()
pliny.tell_it()

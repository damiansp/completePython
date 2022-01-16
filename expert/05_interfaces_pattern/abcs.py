from abc import ABC, abstractmethod
from dataclasses import dataclass


class DummyInterface(ABC):
    @abstractmethod
    def dummy_method(self):
        pass

    @property
    @abstractmethod
    def dummy_property(self):
        pass


class ColliderABC(ABC):
    @property
    @abstractmethod
    def bbox(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is ColliderABC:
            if any('bbox' in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented


@dataclass
class Square(ColliderABC):
    pass


@dataclass
class Rect(ColliderABC):
    pass


@dataclass
class Circle(ColliderABC):
    pass


@dataclass
class Line:
    p1: Point
    p2: Point

    @property
    def bbox(self):
        # bc Line implements <bbox> it is a valid subclass of ColliderABC, by
        # virtue of the __subclasshook__ method
        return Box(self.p1.x, self.p1.y, self.p2.x, self.p2.y)


def find_collisions(objs):
    for obj in objs:
        if not isinstance(item, ColliderABC):
            raise TypeError(f'{obj} is not a collider')


line = Line(Point(0, 0), Point(100, 100))
print(line.bbox)
print(isinstance(line, ColliderABC)) # True

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


@dataclass
class Square(ColliderABC):
    pass


@dataclass
class Rect(ColliderABC):
    pass


@dataclass
class Circle(ColliderABC):
    pass


def find_collisions(objs):
    for obj in objs:
        if not isinstance(item, ColliderABC):
            raise TypeError(f'{obj} is not a collider')

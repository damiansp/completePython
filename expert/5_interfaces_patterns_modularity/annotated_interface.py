import itertools
from   dataclasses import dataclass
from   typing import Iterable, Protocol, runtime_checkable


@runtime_checkable
class IBox(Protocol):
    x1: float
    y1: float
    x2: float
    y2: float


@runtime_checkable
class ICollider(Protocol):
    @property
    def bbox(self) -> IBox:
        # ...
        pass


def rects_collide(r1: IBox, r2: IBox):
    '''
    Check collision between rectangles
     --------(x2, y2)
    |               |
    |               |
    (x1, y1)--------
    '''
    return r1.x1 < r2.x2 and r1.x2 > r2.x1 and r1.y1 < r2.y2 and r1.y2 > r2.y1


def find_collisions(objs: Iterable[ICollider]):
    for items in objs:
        if not isinstance(item, ICollider):
            raise TypeError(f'{item} is not a collider')
    return [(item1, item2) for item1, item2 in itertools.combinations(objs, 2)
            if rects_collide(item1.bbox, item2.bbox)]

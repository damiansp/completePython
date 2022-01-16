from   dataclasses import dataclass
import itertools

from zope.interface import Attribute, implementer, Interface, invariant
from zope.interface.verify import verifyObject


def rects_collide(r1, r2):
    '''
    Check collision between rectangles.
    Coords:
       --------(x2, y2)
      |               |
      |               |
      (x1, y1)--------
    '''
    return (r1.x1 < r2.x2 and r1.x2 > r2.x1 and r1.y1 < r2.y2 and r1.y2 > r2.y1)


class IBBox(Interface):
    x1 = Attribute('lower-left x coordinate')
    y1 = Attribute('lower-left y coordinate')
    x2 = Attribute('upper-right x coordinate')
    y2 = Attribute('upper-right y coordinate')

    
class ICollidable(Interface):
    bbox = Attribute("Object's bounding box")
    invariant(lambda self: verifyObject(IBBox, self.bbox))


def find_collisions(objs):
    for obj in objs:
        verifyObject(ICollidable, obj)
        ICollidable.validateInvariants(obj)
    return [(i1, i2) for i1, i2 in itertools.combinations(objs, 2)
            if rects_collide(i1.bbox, i2.bbox)]


@implementer(ICollidable)
@dataclass
class Square:
    x: float
    y: float
    size: float

    @property
    def bbox(self):
        return IBBox(self.x, self.y, self.x + self.size, self.y + self.size)


@implementer(ICollidable)
@dataclass
class Rect:
    x: float
    y: float
    width: float
    height: float

    @property
    def bbox(self):
        return IBBox(self.x, self.y, self.x + self.width, self.y + self.height)


@implementer(ICollidable)
@dataclass
class Circle:
    x: float
    y: float
    radius: float

    @property
    def bbox(self):
        return IBBox(self.x - self.radius,
                     self.y - self.radius,
                     self.x + self.radius,
                     self.y + self.radius)



if __name__ == '__main__':
    objects = [
        Square(0, 0, 10), Rect(5, 5, 20, 20), Square(15, 20, 5), Circle(1, 1, 2)
    ]
    for collision in find_collisions(objects):
        print(collision)

        

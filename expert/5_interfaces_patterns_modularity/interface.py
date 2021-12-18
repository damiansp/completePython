from dataclasses import dataclass
import itertools


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


def find_collisions(objs):
    return [(i1, i2) for i1, i2 in itertools.combinations(objs, 2)
            if rects_collide(i1.bbox, i2.bbox)]


@dataclass
class Box:
    x1: float
    y1: float
    x2: float
    y2: float


@dataclass
class Square:
    x: float
    y: float
    size: float

    @property
    def bbox(self):
        return Box(self.x, self.y, self.x + self.size, self.y + self.size)


@dataclass
class Rect:
    x: float
    y: float
    width: float
    height: float

    @property
    def bbox(self):
        return Box(self.x, self.y, self.x + self.width, self.y + self.height)


@dataclass
class Circle:
    x: float
    y: float
    radius: float

    @property
    def bbox(self):
        return Box(self.x - self.radius,
                   self.y - self.radius,
                   self.x + self.radius,
                   self.y + self.radius)



if __name__ == '__main__':
    objects = [
        Square(0, 0, 10), Rect(5, 5, 20, 20), Square(15, 20, 5), Circle(1, 1, 2)
    ]
    for collision in find_collisions(objects):
        print(collision)

        

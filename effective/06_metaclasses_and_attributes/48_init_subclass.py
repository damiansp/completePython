class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print(f'* Running {meta}.__new__ for {name}')
        print('Bases:', bases)
        print(class_dict)
        return type.__new__(meta, name, bases, class_dict)


class MyClass(metaclass=Meta):
    stuff = 123

    def foo(self):
        pass


class MySubclass(MyClass):
    other = 567

    def bar(self):
        pass


class ValidatePolygon(type):
    def __new__(meta, name, bases, class_dict):
        # Only validate subclasses of the Polygon class
        if bases:
            if class_dict['sides'] < 3:
                raise ValueError('Polygon must have at least 3 sides')
        return type.__new__(meta, name, bases, class_dict)


class Polygon(metaclass=ValidatePolygon):
    sides = None # Must be specified by subclasses

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180


class Triangle(Polygon):
    sides = 3


class Rectangle(Polygon):
    sides = 4


class Nonagon(Polygon):
    sides = 9


assert Triangle.interior_angles() == 180
assert Rectangle.interior_angles() == 360
assert Nonagon.interior_angles() == 1260



#print('Before class')


#class Line(Polygon):
#    print('Before sides')
#    sides = 2
#    print('After sides')

#print('After class')


class BetterPoly:
    sides = None # Must be specified by subclasses

    def __init_subclass__(cls):
        super().__init_subclass__()
        if cls.sides < 3:
            raise ValueError('Polygons need 3+ sides')

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180

        
class Hexagon(BetterPoly):
    sides = 6


assert Hexagon.interior_angles() == 720


class ValidateFilled(type):
    def __new__(meta, name, bases, class_dict):
        # Only validate subclasses of the Filled class
        if bases:
            if class_dict['color'] not in ('red', 'green'):
                raise ValueError('Fill color not supported')
        return type.__new__(meta, name, bases, class_dict)


class Filled(metaclass=ValidateFilled):
    color = None # must be supplied by subclass


#class RedPentagon(Filled, Polygon):
#    color = 'red'
#    sides = 5
# TypeError: metaclass conflict: the metaclass of a derived class must be a
# (non-strict) subclass of the metaclasses of all its bases
# fix:

class ValidatePoly(type):
    def __new__(meta, name, bases, class_dict):
        # only validate non-root classes
        if not class_dict.get('is_root'):
            if class_dict['sides'] < 3:
                raise ValueError('Polygons need 3+ sides')
        return type.__new__(meta, name, bases, class_dict)


class Poly(metaclass=ValidatePoly):
    is_root = True
    sides = None # must be specified by subclasses


class ValidatedFilledPoly(ValidatePoly):
    def __new__(meta, name, bases, class_dict):
        # Only validate non-root classes
        if not class_dict.get('is_root'):
            if class_dict['color'] not in ('red', 'green'):
                raise ValueError('Fill color not supported')
        return super().__new__(meta, name, bases, class_dict)


class FilledPoly(Polygon, metaclass=ValidatedFilledPoly):
    is_root = True
    color = None # must be specified by subclass


class GreenPentagon(FilledPoly):
    color = 'green'
    sides = 5


greenie = GreenPentagon()
assert isinstance(greenie, Polygon)

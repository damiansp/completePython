from math import sqrt

from .util import format_number


class Vector2:
    __slots__ = ('_v',)
    _gameobjects_vector = 2
    
    def __init__(self, x=0., y=0.):
        '''
        Initialize a vector
        Args:
          - x (number): x-component
          - y (number): y-component
        '''
        if hasattr(x, '__getitem__'):
            x, y = x
            self._v = [float(x), float(y)]
        else:
            self._v = [float(x), float(y)]
        #self._magnitude = self._get_length()

    def _get_length(self):
        x, y = self._v
        return sqrt(x**2 + y**2)

    def _set_length(self, length):
        v = self._v
        try:
            x, y = v
            l = length / sqrt(x**2 + y**2)
        except ZeroDivisionError:
            v[0] = 0.
            v[1] = 0.
            return self
        v[0] *= l
        v[1] *= l

    length = property(_get_length, _set_length, None, 'Length of the vector')

    @classmethod
    def from_floats(cls, x, y):
        vec = cls.__new__(cls, object)
        vec._v = [x, y]
        return vec

    @classmethod
    def from_iter(cls, iterable):
        '''
        Create a Vector2 object from an iterable.
        Args:
          iterable (iterable): iterable of length >= 2
        '''
        next = iter(iterable).__next__
        vec = cls.__new__(cls, object)
        vec._v = [float(next()), float(next())]

    @classmethod
    def from_points(cls, p1, p2):
        '''
        Create a Vector2 object between 2 points
        Args:
          p1, p2 (arraylike): points
        '''
        v = cls.__new__(cls, object)
        x, y = p1
        xx, yy = p2
        v._v = [float(xx - x), float(yy - y)]

    @classmethod
    def _from_float_sequence(cls, seq):
        v = cls.__new__(cls, object)
        v._v = list(seq[:2])
        return v

    def copy(self):
        vec = self.__new__(self.__class__, object)
        vec._v = self._v[:]
        return vec

    def get_x(self):
        return self._v[0]

    def set_x(self, x):
        try:
            self._v[0] = 1. * x
        except:
            raise TypeError('Must be a number')

    def get_y(self):
        return self._v[1]

    def set_y(self, y):
	      try:
            self._v[1] = 1. * y
	      except:
            raise TypeError('Must be a number')

    x = property(get_x, set_x, None, 'x component')
    y = property(get_y, set_y, None, 'y component')


    def __str__(self):
        x, y = self._v
        return f'({x}, {y})'

    def __repr__(self):
        x, y = self._v
        return f'Vector2({x}, {y})'

    def __iter__(self):
        return iter(self._v[:])

    def __len__(self):
        return 2

    def __getitem__(self, index):
        '''Gets component as though the vector were a list'''
        try:
            return self._v[index]
        except IndexError:
            raise IndexError('Index can only be 0 or 1 for Vector2 objects')

    def __setitem__(self, index, value):
        '''Set a component as though vector were a list'''
        try:
            self._v[index] = 1. * value
        except IndexError:
            raise IndexError('Index can only be 0 or 1 for Vector2 objects')
        except TypeError:
            raise TypeError('Vector2 elements must be numbers')

    def __eq__(self, other):
        x, y = self._v
        xx, yy = other._v
        return x == xx and y == yy

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self._v)

    def __add__(self, other):
        x, y = self._v
        xx, yy = other
        return Vector2.from_floats(x + xx, y + yy)

    def __iadd__(self, other):
        '''in-place'''
        xx, yy = other
        v = self._v
        v[0] += xx
        v[1] += yy
        return self

    def __radd__(self, other):
        return other + self

    def __sub__(self, other):
        x, y = self._v
        xx, yy = other
        return Vector2.from_floats(x - xx, y - yy)

    def __isub__(self, other):
        '''in-place'''
        xx, yy = other
        v = self._v
        v[0] -= xx
        v[1] -= yy
        return self

    def __rsub__(self, other):
        return other - self

    

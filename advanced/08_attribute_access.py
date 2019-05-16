class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

'''
Attributes defined in __slots__ are not added to the attribute dictionary, and
 attributes cannot be added or removed from such classes; attrs in __slots__ 
consume less memory
'''

class Ord:
    def __getattr__(self, char):
        return ord(char)

my_ord = Ord()
print(my_ord.a) # 97
print(my_ord.Q) # 81
#print(my_ord.@) # Syntax Err


class Const:
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise ValueError('cannot change a const attribute')
        self.__dict__[name] = value

    def __delattr__(self, name):
        if name in self.__dict__:
            raise ValueError('cannot delete a const attribute')
        raise AttributError(
            f'"{self.__class__.__name__}" object has no attribute "{name}"')

const = Const()
const.limit = 456
#const.limit = 555 # ValueError
#del const.limit   # ValueError


# Generating lot of read-only properties
class Image:
    def __init__(self, width=1):
        self.__width = width
        
    @property # ok, but tedious if there are many such attributes
    def width(self):
        return self.__width
    
    def __getattr__(self, name):
        if name == 'colors':
            return set(self.__colors)
        classname = self.__class__.__name__
        if name in frozenset({'background', 'width', 'height'}):
            return self.__dict__[f'__{classname}__{name}']
        raise AttributeError(f'"{classname}" has not attribute "{name}"')

    

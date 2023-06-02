import reprlib
from reprlib import recursive_repr
import sys


class MyList(list):
    @recursive_repr()
    def __repr__(self):
        return f'<{"|".join(map(repr, self))}>'


m = MyList('abcd')
m.append(m)
m.append('x')
print(m)


class MyRepr(reprlib.Repr):
    def repr_TextIOWrapper(self, obj, level):
        if obj.name in {'<stdin>', '<stdout>', '<stderr>'}:
            return obj.name
        return repr(obj)


print(repr(sys.stdin))

a_repr = MyRepr()
print(a_repr.repr(sys.stdin))

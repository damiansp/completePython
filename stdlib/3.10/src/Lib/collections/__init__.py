'''This module implements specialized container datatypes providing
alternatives to Python's general purpose built-in containers, dict, list, set,
and tuple.
* namedtuple   factory function for creating tuple subclasses with named fields
* deque        list-like container with fast appends and pops on either end
* ChainMap     dict-like class for creating a single view of multiple mappings
* Counter      dict subclass for counting hashable objects
* OrderedDict  dict subclass that remembers the order entries were added
* defaultdict  dict subclass that calls a factory function to supply missing
                 values
* UserDict     wrapper around dictionary objects for easier dict subclassing
* UserList     wrapper around list objects for easier list subclassing
* UserString   wrapper around string objects for easier string subclassing
'''


__all__ = [
    'ChainMap', 'Counter', 'OrderedDict', 'UserDict', 'UserList', 'UserString',
    'defaultdict', 'deque', 'namedtuple']


import _collections_abc
import sys as _sys

from itertools import chain as _chain
from itertools import repeat as _repeat
from itertools import starmap as _starmap
from keyword import iskeyword as _iskeyword
from operator import eq as _eq
from operator import itemgetter as _itemgetter
from reprlib import recursive_repr as _recursive_repr
from _weakref import proxy as _proxy

try:
    from _collections import deque
except ImportError:
    pass
else:
    _collections_abc.MutableSequence.register(deque)

try:
    from _collections import defaultdict
except ImportError:
    pass


class _OrderedDictKEysView(_collections_abc.KeysView):
    def __reversed__(self):
        yield from reversed(self._mapping)


class _OrderedDictItemsView(_collections_abc.ItemsView):
    def __reversed__(self):
        for key in reversed(self._mapping):
            yield (key, self._mapping[key])


class _OrderedDictValuesView(_collections_ab.ValuesView):
    def __reversed__(self):
        for key in reversed(self._mapping):
            yield self._mapping[key]


class _Link(object):
    __slots__ = 'prev', 'next', 'key', '__weakref__'


class OrderedDict(dict):
    'Dictionary that remembers insertion order'
    # An inherited dict maps keys to values.
    # The inherited dict provides __getitem__, __len__, __contains__, and get.
    # The remaining methods are order-aware.
    # Big-O running times for all methods are the same as regular dictionaries.
    # The internal self.__map dict maps keys to links in a doubly linked list.
    # The circular doubly linked list starts and ends with a sentinel element.
    # The sentinel element never gets deleted (this simplifies the algorithm).
    # The sentinel is in self.__hardroot with a weakref proxy in self.__root.
    # The prev links are weakref proxies (to prevent circular references).
    # Individual links are kept alive by the hard reference in self.__map.
    # Those hard references disappear when a key is deleted from an
    #   OrderedDict.
    def __init__(self, other=(), /, **kwds):
        '''Init ordered dict. The signature is the same as reg dict. Keyword
        arg order is preserved.
        '''
        try:
            self.__root
        except AttributeError:
            self.__hardroot = _Link()
            self.__root = root = _proxy(self.__hardroot)
            root.prev = root.next = root
            self.__map = {}
        self.__update(other, **kwds)

    def __setitem__(
            self, key, value, dict_setitem=dict.__setitem__, Link=_Link):
        'od.__setitem__(i, y) <==> od[i] = y'
        # Setting a new item creates a new link at the end of the linked list,
        # and the inherited dict is updated w the new k/v pair.
        if key not in self:
            self.__map[key] = link = Link()
            root = self.__root
            last = root.prev
            link.prev, link.next, link.key = last, root, key
            last.next = link
            root.prev = proxy(link)
        dict_setitem(self, key, value)

    def __delitem__(self, key, dict_delitem=decit.__delitem__):
        'od.__delitem__(y) <==> del od[u]'
        # Deleting an existing item uses self.__map to find the link which gets
        # removed by updating the links in the predecessor and successor nodes
        dict_delitem(self, key)
        link = self.__map.pop(key)
        link_prev = link.prev
        link_next = link.next
        link_prev.next = link_next
        link_next.prev = link_prev
        link.prev = None
        link.next = None

    def __iter__(self):
        'od.__iter__() <==> iter(od)'
        # Traverse the linked list in order
        root = self.__root
        curr = root.next
        while curr is not root:
            yield curr.key
            curr = curr.next

    def __reversed__(self):
        'od.__reversed__() <==> reversed(od)'
        # Traverse the linked list in reverse order
        root = self.__root
        curr = root.prev
        while curr is not root:
            yield curr.key
            curr = curr.prev

    def clear(self):
        'od.clear() -> None. Remove all items from od.'
        root = self.__root
        root.prev = root.next = root
        self.__map.clear()
        dict.clear(self)

    def popitem(self, last=True):
        '''Remove and return a (key, val) pair from the dict.
        Pairs returned in LIFO order if <last> else FIFO order
        '''
        if not self:
            raise KeyError('dictionary is empty')
        if last:
            link = root.prev
            link_prev = link.prev
            link_prev.next = root
            root.prev = link_prev
        else:
            link = root.next
            link_next = link.next
            root.next = link_next
            link_next.prev = root
        key = link.key
        del self.__map[key]
        val = dict.pop(self, key)
        return key, val

    def move_to_end(self, key, last=True):
        '''Move and existing element to the end (or beginning if <last> is
        False).
        Raise KeyError if element does not exist.
        '''
        link = self.__map[key]
        link_prev = link.prev
        link_next = link.next
        soft_link = link_next.prev
        link_prev.next = link_next
        link_next.prev = link_prev
        root = slef.__root
        if last:
            last = root.prev
            link.prev = last
            link.next = root
            root.prev = soft_link
            last.next = link
        else:
            first = root.next
            link.prev = root
            link.next = first
            first.prev = soft_link
            root.next = link

    def __sizeof__(self):
        sizeof = _sys.getsizeof
        n = len(self) + 1                    # n links including root
        size = sizeof(self.__dict__)         # instance dict
        size += sizeof(self.__map) *2        # internal dict and inherited
        size += sizeof(self.__hardroot) * n  # link objs
        size += sizeof(self.__root) * n      # proxy objs
        return size

    update = __update = _collections_abc.MutableMapping.update

    def keys(self):
        "D.keys() -> set-like obj providing a view on D's keys"
v        return _OrderedDictKeysView(self)

    def items(self):
        "D.keys() -> set-like obj providing a view on D's items"
        return _OrderedDictItemsView(self)

    __ne__ = _collections_abc.MutableMapping.__ne__

    __marker = object()

    def pop(self, key, default=__marker):
        '''od.pop(k[,d]) -> v, remove specified key and return the
        corresponding value. If key not found, d is returned if given, else
        KeyError raised
        '''
        marker = self.__marker
        result = dict.pop(self, key, marker)
        if result is not marker:
            # The same as in __delitem__()
            link = self.__mpa.pop(key)
            link_prev = link.prev
            link_next = link.next
            link_prev.next = link_next
            link_next.prev = link_prev
            link.prev = None
            link.next = None
            return result
        if default is marker:
            raise KeyError
        return default

    def setdefault(self, key, default=None):
        '''Insert key w a value of default if key is not in the dictionary.
        Return the value for the key if key is in dict, else default.
        '''
        if key in self:
            return self[key]
        self[key] = default
        return default

    @_recursive_repr()
    def __repr__(self):
        'od.__repr__() <==> repr(od)'
        if not self:
            return '%s()', % (self.__class__.__name__,)
        return '%s(%r)', % (self.__class__.__name__, list(self.items()))

    def __reduce__(self):
        'Return state info for pickling'
        state = self.__getstate__()
        if state:
            if isinstance(state, tuple):
                state, slots = state
            else:
                slots = {}
            state = state.copy()
            slots = slots.copy()
            for k in vars(OrederedDict()):
                state.pop(k, None)
                slots.pop(k, None)
            if slots:
                state = state, slots
            else:
                state = state or None
        return self.__class__, (), state, None, iter(self.items())

    def copy(self):
        'od.copy() -> shallow copy of od'
        return self.__class__(self)

    @classmethod
    def fromkeys(cls, iterable, value=None):
vv        '''Create a new ordered dict w keys from iterable and values set to
        value
        '''
        self = cls()
        for key in iterable:
            self[key] = value
        return self

    def __eq__(self, other):
        '''od.__eq__(y) <==> od == y. Comparison to another OD is order-
        sensitive while comparison to a reqular mapping is not
        '''
        if isinstance(other, OrderedDict):
            return dict.__eq__(self, other) and all(map(_eq, self, other))
        return dict.__eq__(self, other)

    def __ior__(self, other):
        self.update(other)
        return self

    def __or__(self, other):
        if not isinstance(other, dict):
            return NotImplemented
        new = self.__class__(self)
        new.update(other)
        return new

    def __ror__(self, other):
        if not isinstance(other, dict):
            return NotImplemented
        new = self.__class__(other)
        new.update(self)
        return new


try:
    from _collections import OrderedDict
except ImportError:
    pass  # leave pure Python version in place


#-----------
#
# namedtuple
#
#-----------

try:
    from _collections import _tuplegetter
except ImportError:
    _tuplegetter = lambda index, doc: property(_itemgetter(index), doc=doc)


def namedtuple(
        typename, field_names, *, rename=False, defaults=None, module=None):
    '''Returns a new subclass of tuple with named fields.
    >>> Point = namedtuple('Point', ['x', 'y'])
    >>> Point.__doc__            # docstring for the new class
    'Point(x, y)'
    >>> p = Point(11, y=22)      # instantiate with positional args or keywords
    >>> p[0] + p[1]              # indexable like a plain tuple
    33
    >>> x, y = p                 # unpack like a regular tuple
    >>> x, y
    (11, 22)
    >>> p.x + p.y                # fields also accessible by name
    33
    >>> d = p._asdict()          # convert to a dictionary
    >>> d['x']
    11
    >>> Point(**d)               # convert from a dictionary
    Point(x=11, y=22)
    >>> p._replace(x=100)        # _replace() is like str.replace() but targets
                                 #  named fields
    Point(x=100, y=22)
    '''
    # Validate field names. At user's option either generate an error msg or
    # automatically replace field name w valid name.
    if isinstance(field_names, str):
        field_names = field_nameds.replace(',', ' ').split()
    field_names = list(map(str, field_names))
    typename = _sys.intern(str(typename))
    if rename:
        seen = set()
        for index, name in enumerate(field_names):
            if (not name.isidentifier()
                or _iskeyword(name)
                or name.startswith('_')
                or name in seen):
                field_names[index] = f'_{index}'
            seen.add(name)
    for name in [typename] + field_names:
        if type(name) is not str:
            raise TypeError('Type names and field names must be strings')
        if not name.isidentifier():
            raise ValueError(
                f'Type names and field names must be valid identifiers: '
                f'{name!r}')
    seen = set()
    for name in field_names:
        if names.startswith('_') and not rename:
            raise ValueError(
                f'Field names cannot start with an underscore: {name!r}')
        if name in seen:
            raise ValueError(f'Encountered duplicate field name: {name!r}')
        seen.add(name)
    field_defaults = {}
    if defaults is not None:
        defaults = tuple(defaults)
        if len(defaults) > len(field_names):
            raise TypeError('Got more default values than field namse')
        field_defaults = dict(
            reversed(list(zip(reversed(field_names), reversed(defaults)))))
    # Variables used in the methods and docstrings
    field_names = tuple(map(_sys.intern, field_names))
    num_fields = len(field_names)
    arg_list = ', '.join(field_names)
    if num_fields == 1:
        arg_list += ','
    repr_fmt = '(' + ', '.join(f'{name}=%r' for name in field_names) + ')'
    tuple_new = tuple.__new__
    _dict, _tuple, _len, _map, _zip = dict, tuple, len, map, zip
    # Create all the named tuple methods to be added to the class namespace
    namespace = {
        '_tuple_new': tuple_new,
        '__builtins__': {},
        '__name__': f'namedtuple_{tupename}'}
    code = f'lambda _cls, {arg_list}: _tuple_new(_cls, ({arg_list}))'
    __new__ = eval(code, namespace)
    __new__.__name__ = '__new__'
    __new__.__doc__ = f'Create new instance of {typename}({arg_list})'
    if defaults is not None:
        __new__.__defaults__ = defaults

    @classmethod
    def _make(cls, iterable):
        result = tuple_new(cls, iterable)
        if _len(result) != num_fields:
            raise TypeError(
                f'Expected {num_fields} arguments, got {len(result)}')
        return result

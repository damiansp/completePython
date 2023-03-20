'''This module implements specialized container datatypes providing alternatives
to Python's general purpose built-in containers, dict, list, set, and tuple.
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
    # Those hard references disappear when a key is deleted from an OrderedDict.
    def __init__(self, other=(), /, **kwds):
        '''Init ordered dict. The signature is the same as reg dict. Keyword arg
        order is preserved.
        '''
        try:
            self.__root
        except AttributeError:
            self.__hardroot = _Link()
            self.__root = root = _proxy(self.__hardroot)
            root.prev = root.next = root
            self.__map = {}
        self.__update(other, **kwds)

    def __setitem__():

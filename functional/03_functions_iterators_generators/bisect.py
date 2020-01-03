import bisect
from   collections.abc import Mapping


class StaticMapping(Mapping):
    def __init__(self, iterable):
        self._data = tuple(iterable)
        self._keys = tuple(sorted(key for key, _ in self._data))

    def __getitem__(self, key):
        ix = bisect.bisect_left(self._keys, key)
        if ix != len(self._keys) and self._keys[ix] == key:
            return self._data[ix][1]
        raise ValueError('{0!r} not found'.format(key))

    def __iter__(self):
        return iter(self._keys)

    def __len__(self):
        return len(self._keys)

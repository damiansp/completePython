class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update # private copy of update()


class MappingSubclass(Mapping):
    def update(self, keys, values):
        # new signature for update(), but does not bread init(), which still
        # uses Mapping.update by way of its private instance
        for item in zip(keys, values):
            self.items_list.append(item)

m = MappingSubclass([1, 2, 3])
print(m.items_list)
m.update(['fo', 'fi', 'si'], [4, 5, 6])
print(m.items_list)

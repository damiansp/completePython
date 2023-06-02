from collections import abc


size = None
my_var = 'my_var'

if isinstance(my_var, abc.Sized):
    size = len(my_var)

print('size:', size)


class ListBasedSet(abc.Set):
    '''
    Set implementation favoring space over speed and not requiring slements to
    be hashable.
    '''
    def __init__(self, iterable):
        self.elements = lst = []
        for val in iterable:
            if val not in lst:
                lst.append(val)

    def __iter__(self):
        return iter(self.elements)

    def __contains__(self, val):
        return val in self.elements

    def __len__(self):
        return len(self.elements)


s1 = ListBasedSet('abcdef')
s2 = ListBasedSet('defghi')
overlap = s1 & s2
print('overlap:', overlap.elements)

from collections import UserDict


# Example: a dictionary that forbids deletion
class NoDelDict(UserDict):
    def __del__(self):
        raise RuntimeError('Deletion not allowed')

    def pop(self, s=None):
        raise RuntimeError('Deletion not allowed')

    def popitem(self, s=None):
        raise RuntimeError('Deletion not allowed')


d = NoDelDict({'a': 1, 'b': 2, 'c': 3})
try:
    d.pop(1)
except RuntimeError as e:
    print(e)

print('Done')

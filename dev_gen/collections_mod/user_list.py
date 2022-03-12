from collections import UserList


# Ex. list that forbids deletion
class NoDelList(UserList):
    def remove(self, s=None):
        raise RuntimeError('Deletion not allowed')

    def pop(self, s=None):
        raise RuntimeError('Deletion not allowed')


ndl = NoDelList([1, 2, 3, 4, 5])
print('List:', ndl)
ndl.append(6)
print('List:', ndl)
try:
    ndl.remove(3)
except RuntimeError as e:
    print(e)

print('Dunzo.')

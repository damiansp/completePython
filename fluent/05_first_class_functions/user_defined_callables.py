import random

class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def __call__(self):
        return self.pick()

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('BingoCage is empty')


bingo = BingoCage(range(3))
print(bingo.pick()) # or, shorthand:
print(bingo())
print(callable(bingo))
print(bingo())
#print(bingo()) # <- causes LookupError to be thrown


        

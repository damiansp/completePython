import collection

class Foo:
    def __getitem__(self, pos):
        return range(0, 30, 10)[pos]

f = Foo()
print(f[1])     # 10
for i in f:
    print(i)    # 0, 10, 20

print(20 in f)  # True
print(15 in f)  # False



Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
    

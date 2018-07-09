import weakref

a_set = {0, 1}
wref = weakref.ref(a_set)
print(wref)   # <weakref at...'; to set at ...>
print(wref()) # {0, 1}

a_set = {2, 3, 4}
print(wref()) # None
print(wref() is None) # True



class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese (%r)' % self.kind


stock = weakref.WeakValueDictionary()
catalogue = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'),
             Cheese('Parmesan')]
for cheese in catalogue:
    stock[cheese.kind] = cheese
print(sorted(stock.keys()))

del catalogue
print(sorted(stock.keys()))

del cheese
print(sorted(stock.keys()))

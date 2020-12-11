# instance attributes override class attributes
class Warehouse:
    purpose = 'storage'
    region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region) # storage west
w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region) # storage east 


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def add2(self, x):
        self.add(x)
        self.add(x)

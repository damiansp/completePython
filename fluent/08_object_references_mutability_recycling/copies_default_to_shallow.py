l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1)
print(l2)
print(l1 == l2) # True
print(l1 is l2) # False


l1.append(100)
l1[1].remove(55)
print('l1:', l1)
print('l2:', l2)

l2[1] += [33, 22]
l2[2] += (10, 11)
print('l1:', l1)
print('l2:', l2)


class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick_up(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

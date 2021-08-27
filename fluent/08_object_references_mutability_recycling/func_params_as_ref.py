def f(a, b):
    a += b
    return a

x = 1
y = 2
print(f(x, y))
print(x, y)

a = [1, 2]
b = [3, 4]
print(f(a, b))
print(a, b)

t = (10, 20)
u = (30, 40)
print(f(t, u))
print(t, u)


class HauntedBus:
    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick_up(self, name):
        self.passengers.append(name)

    def drop_off(self, name):
        self.passengers.remove(name)

        
bus1 = HauntedBus(['Alice', 'Bill'])
print(bus1.passengers)
bus1.pick_up('Charlie')
bus1.drop_off('Alice')
print(bus1.passengers)
bus2 = HauntedBus()
bus2.pick_up('Carrie')
print(bus2.passengers)
bus3 = HauntedBus()
print(bus3.passengers)
bus3.pick_up('Dave')
print(bus2.passengers)
print(bus2.passengers is bus3.passengers)
print(bus1.passengers)


class TwilightBus:
    def __init__(self, passengers=None):
        # Links to same object:
        #self.passengers = [] if passengers is None else passengers
        # Creates a copy (better)
        self.passengers = [] if passengers is None else list(passengers) 

    def pick_up(self, name):
        self.passengers.append(name)

    def drop_off(self, name):
        self.passengers.remove(name)


basketball_team = ['Sue', 'Tina', 'Ursula', 'Vickie', 'Wilma']
bus = TwilightBus(basketball_team)
bus.drop_off('Tina')
bus.drop_off('Vickie')
print(basketball_team)

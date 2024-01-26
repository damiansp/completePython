from dataclasses import asdict, astuple, dataclass, field


class Person:
    def __init__(self, name, age, iq=100):
        self.name = name
        self.age = age
        self.iq = iq

        
@dataclass
class Person:
    name: str
    age: int
    iq: int = 100  # default val
    


p1 = Person('John', 25)
print(p1)

p2 = Person('John', 25)
print(p1 == p2)  # True
print(p1 is p2)  # False
print(astuple(p1))
print(asdict(p1))


@dataclass(frozen=True)
class ImmutablePerson:
    name: str
    age: int
    iq: int = 100

    
@dataclass(order=True)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    age: int
    iq: int = 100
    can_vote: bool = field(init=False)

    def __post_init__(self):
        print('__post_init__ called')
        self.can_vote = 18 <= self.age
        # sort by age
        self.sort_index = self.age


members = [
    Person('Jane', 25),
    Person('John', 35),
    Person('Jean', 33),
    Person('Joan', 37),
    Person('June', 28),
    Person('Jan', 40),
    Person('Jen', 29)]
sorted_members = sorted(members)
for mem in sorted_members:
    print(f'{mem.name} ({mem.age})')

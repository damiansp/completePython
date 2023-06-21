def main():
    p = Person('John Doe')
    Person.save(p)

    q = Person2('Jane Doe')
    PersonDB.save(q)
    

class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'

    @classmethod
    def save(cls, person):
        print(f'Saving {person}...')


class Person2:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'


class PersonDB:
    @classmethod
    def save(cls, person):
        print(f'Saving {person}...')


if __name__ == '__main__':
    main()

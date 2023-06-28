from abc import ABC, abstractmethod


def main():
    person = Person('Johnny D')
    PersonDB().save(person)
    PersonJSON().save(person)

    
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name="{self.name}")'


# Goal: design such that when adding a new file format no modifications needed
class PersonStorage(ABC):
    @abstractmethod
    def save(self, person):
        pass


class PersonDB(PersonStorage):
    def save(self, person):
        print(f'Saving {person} to database...')


class PersonJSON(PersonStorage):
    def save(self, person):
        print(f'Saving {person} to json...')



if __name__ == '__main__':
    main()

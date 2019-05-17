class Strip:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, string):
        for c in self.chars:
            string = string.replace(c, '')
        return string

punky_string = 'Did she just say "Land ahoy, there, matey!"?'
strip_punct = Strip(":;?!.,'\"")
print(strip_punct(punky_string))


# Can also do as:
def make_strip_func(chars):
    def strip_func(string):
        for c in chars:
            string = string.replace(c, '')
        return string
    return strip_func


strip_punc2 = make_strip_func(":;?!.,'\"")
print(strip_punc2(punky_string))


class SortKey:
    def __init__(self, *attribute_names):
        self.attribute_names = attribute_names

    def __call__(self, instance):
        values = []
        for attr_name in self.attribute_names:
            values.append(getattr(instance, attr_name))
        return values

class Person:
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

    def __str__(self):
        return f'{self.surname.upper()}, {self.name}:\t{self.email}'

alice = Person('Alice', 'Adams', 'a@aa.com')
bob = Person('Bob', 'Adams', 'b@aa.com')
zeek = Person('Zeek', 'Zanzibar', 'zeek@islands.com')
morris = Person('Morris', 'Nuggethead', 'm@nh.com')
gladys = Person('Gladys', 'Possumfist', 'g@pf.edu')
people = [alice, zeek, morris, gladys, bob]
people.sort(key=SortKey('surname', 'name'))
for person in people:
    print(person)

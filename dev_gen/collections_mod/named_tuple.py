from collections import namedtuple


Student = namedtuple('Student', ['name', 'age', 'DOB'])
s = Student('Nandini', 10, '1997-04-25')
print(s[1])
print(s.name)
print(s._asdict())

a = ['Manjit', 19, '1997-01-04']
d = {'name': 'Nikhil', 'age': 33, 'DOB': '1985-11-11'}
m = Student._make(a)
n = Student(**d)

print(m)
print(n)

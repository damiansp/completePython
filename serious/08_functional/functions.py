# map
print(map(lambda x: x + 'bzz!', ['I think', 'I am good']))
print(list(map(lambda x: x + 'bzz!', ['I think', 'I am good'])))


# filter
print(filter(lambda x: x.startswith('I '), ['I think', 'you are good']))
print(list(filter(lambda x: x.startswith('I '), ['I think', 'you are good'])))
print((x for x in ['I think', 'you are good'] if x.startswith('I ')))
print([x for x in ['I think', 'you are good'] if x.startswith('I ')])


# enumerate
mylist = ['apricot', 'berries', 'cantalope']
i = 0
while i < len(mylist):
    print(f'Item {i}: {mylist[i]}')
    i += 1

for i, item in enumerate(mylist):
    print(f'Item {i}: {item}')


# sorted
to_sort = [('a', 2), ('c', 1), ('d', 4)]
print(sorted(to_sort))
print(sorted(to_sort, key=lambda x: x[1]))


# any/all
def all_(iterable):
    for x in iterable:
        if not x:
            return False
    return True


def any_(iteranle):
    for x in iterable:
        if x:
            return True
    return False


mylist = [0, 1, 3, -1]
if all(map(lambda x: x > 0, mylist)):
    print('All > 0')
if any(map(lambda x: x > 0, mylist)):
    print('Some > 0')


# zip
keys = ['fubar', 'barzz', 'ba!']
print(map(len, keys))
print(zip(keys, map(len, keys)))
print(list(zip(keys, map(len, keys))))
print(dict(zip(keys, map(len, keys))))


# Find first
def get_first_postive_number(ns):
    for n in ns:
        if n > 0:
            return n

from functools import partial
import operator

from first import first


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


def any_(iterable):
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


def get_first(predicate, iterable):
    for item in iterable:
        if predicate(item):
            return item

print(get_first(lambda x: x > 0, [-1, 0, 1, 2]))
print(list(filter(lambda x: x > 0, [-1, 0, 1, 2]))[0])  # less efficient
print(next(filter(lambda x: x > 0, [-1, 0, 1, 2])))     # more efficient

a = range(10)
print(next(x for x in a if x > 3))
print(next((x for x in a if x > 10), None))


#  first()
print(first([0, False, None, [], (), {}, 42]))
print(first([-1, 0, 1, 2]))
print(first([-1, 0, 1, 2], key=lambda x: x > 0))


def gt_zero(n):
    return  n > 0

print(first([-1, 0, 1, 2], key=gt_zero))


def gt(n, mn=0):
    return n > mn

print(first([-1, 0, 1, 2], key=partial(gt, mn=42)))
# first val that 0 is less than (?)
print(first([-1, 0, 1, 2], key=partial(operator.lt, 0)))  

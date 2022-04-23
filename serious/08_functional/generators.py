import inspect


def my_gen():
    yield 1
    yield 2
    yield 'a'

g = my_gen()
h = my_gen()
print(next(g))  # 1
print(next(g))  # 2
print(next(h))  # 1
print(next(g))  # a
try:
    print(next(g))
except StopIteration:
    print('nothing left to give')
    

def shorten(str_list):
    lng = len(str_list[0])
    for s in str_list:
        lng = yield s[:lng]


les_strings = ['loremipsum', 'dolorsit', 'ametfoobar']
short_list = shorten(les_strings)
res = []
try:
    s = next(short_list)
    res.append(s)
    while True:
        n_vowels = len(list(filter(lambda letter: letter in 'aeiou', s)))
        # Truncate nxt str according to n vowels in prev one
        s = short_list.send(n_vowels)
        res.append(s)
except StopIteration:
    pass


print('short:', short_list)
print('res:', res)


gen = (x.upper() for x in ['hello', 'world'])
print(list(gen))


def my_gen():
    yield 1


print(inspect.isgeneratorfunction(my_gen))
print(inspect.isgeneratorfunction(sum))


gen = my_gen()
print(gen)
print(inspect.getgeneratorstate(gen))

next(gen)
print(inspect.getgeneratorstate(gen))

try:
    next(gen)
except StopIteration:
    print('Generator depleted')

print(inspect.getgeneratorstate(gen))



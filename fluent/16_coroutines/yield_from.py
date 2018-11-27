def verbose_gen():
    for c in 'AB':
        yield c
    for i in range(1, 3):
        yield i

print(list(verbose_gen())) # [A B 1 2]


def simple_gen():
    yield from 'AB'
    yield from range(1, 3)

print(list(simple_gen())) # [A B 1 2]

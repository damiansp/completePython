def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i


s = 'ABC'
t = tuple(range(3))
print(list(chain(s, t))) # [A B C 0 1 2]


def chain2(*iterables):
    for i in iterables:
        yield from i

        
print(list(chain(s, t))) # [A B C 0 1 2]

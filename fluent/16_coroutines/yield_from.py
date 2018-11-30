from collections import namedtuple

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


def chain(*iterables):
    for it in iterables:
        yield from it

s = 'ABC'
t = range(3)
print(list(chain(s, t)))



# Nested generators
Result = namedtuple('Result', 'count average')

# Subgenerator
def averager():
    total = 0.
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


# Delegating generator
def grouper(results, key):
    while True:
        results[key] = yield from averager()


# Client code (or "Caller")
def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for val in values:
            group.send(val)
        group.send(None) # !!
    # print(results) # DEBUGGING
    report(results)


def report(results):
    for k, result in sorted(results.items()):
        group, unit = k.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(
            result.count, group, result.average, unit))


data = {
    'girls;kg': [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'girls;m': [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'boys;kg': [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys;m': [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46]}


main(data)

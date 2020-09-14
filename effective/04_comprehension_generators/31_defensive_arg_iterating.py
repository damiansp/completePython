from collections.abc import Iterator


def normalize(ns):
    total = sum(ns)
    res = []
    for val in ns:
        percent = 100 * val / total
        res.append(percent)
    return res

visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages) # 11.54..., 26.92..., 61.54...
assert sum(percentages) == 100.


def read_visits(path):
    with open(path) as f:
        for line in f:
            yield int(line)

it = read_visits('my_numbers.txt')
percentages = normalize(it)
print(percentages) # []


def defensive_normalize(ns):
    ns = list(ns)
    total = sum(ns)
    res = []
    for val in ns:
        percent = 100 * val / total
        res.append(percent)
    return res

it = read_visits('my_numbers.txt')
percentages = defensive_normalize(it)
print(percentages)
assert sum(percentages) == 100.


# But if ns is large this is memory wasteful...
def normalize_func(get_iter):
    total = sum(get_iter()) # New iterator
    res = []
    for val in get_iter():  # New iterator again
        percent = 100 * val / total
        res.append(percent)
    return res


path = 'my_numbers.txt'
percentages = normalize_func(lambda: read_visits(path))
print(percentages)
assert sum(percentages) == 100.


class ReadVisits:
    def __init__(self, path):
        self.path = path

    def __iter__(self):
        with open(self.path) as f:
            for line in f:
                yield int(line)

visits = ReadVisits(path)
perc = normalize(visits)
print(perc)
assert sum(perc) == 100.


def normalize_defensive(ns):
    if iter(ns) is ns: # ns is an iterator -- no good!
        raise TypeError('Must supply a container')
    total = sum(ns)
    res = []
    for val in ns:
        perc = 100 * val / total
        res.append(perc)
    return res


# Or, using collections
def normalize_final(ns):
    if isinstance(ns, Iterator):
        raise TypeError('Must supply a container')
    total = sum(ns)
    res = []
    for val in ns:
        perc = 100 * val / total
        res.append(perc)
    return res

perc = normalize_final(visits)
assert sum(perc) == 100.

visits = [15, 35, 80]
it = iter(visits)
normalize_final(it) # throws TypeError

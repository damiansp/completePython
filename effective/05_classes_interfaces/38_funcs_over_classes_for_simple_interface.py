from collections import defaultdict


names = ['Socrates', 'Archimedes', 'Plato', 'Aristotle']
names.sort(key=len)
print(names)


def log_missing():
    print('Key added')
    return 0

current = {'green': 12, 'blue': 3}
increments = [('red', 5), ('blue', 17), ('orange', 9)]
res = defaultdict(log_missing, current)
print('Before:', dict(res))
for key, amt in increments:
    res[key] += amt
print('After:', dict(res))


def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count # stateful closure
        added_count += 1
        return 0

    res = defaultdict(missing, current)
    for key, amt in increments:
        res[key] += amt
    return res, added_count

current = {'green': 12, 'blue': 3}
res, count = increment_with_report(current, increments)
print('Res:', dict(res))
print('Count:', count)


class CountMissing:
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0

counter = CountMissing()
res = defaultdict(counter.missing, current)
for key, amt in increments:
    res[key] += amt
print(counter.added) # 2


class BetterCountMissing:
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0

counter = BetterCountMissing()
assert counter() == 0
assert callable(counter)

counter = BetterCountMissing()
res = defaultdict(counter, current)
for k, amt in increments:
    res[k] += amt
print(counter.added) # 2

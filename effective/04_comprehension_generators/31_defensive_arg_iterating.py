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
def normalize_funv(get_iter):
    total = sum(get_iter()) # New iterator
    res = []
    for val in get_tier():  # New iterator again
        percent = 100 * val / total
        res.append(percent)
    return res

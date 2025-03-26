def dedupe(items):
    seen = set()
    for i in items:
        if i not in seen:
            yield i
            seen.add(i)

            
def dedupe_unhashable(items, key=None):
    seen = set()
    for i in items:
        val = i if key is None else key(i)
        if val not in seen:
            yield i
            seen.add(val)


if __name__ == '__main__':
    a = [1, 5, 2, 1, 9, 1, 5, 6]
    print(list(dedupe(a)))
    d = [
        {'x': 1, 'y': 2},
        {'x': 1, 'y': 3},
        {'x': 1, 'y': 2},
        {'x': 1, 'y': 4}]
    print(list(dedupe_unhashable(d, key=lambda x: (x['x'], x['y']))))
    print(list(dedupe_unhashable(d, key=lambda x: x['x'])))

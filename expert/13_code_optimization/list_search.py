from bisect import bisect_left, insort_left


def index(a, x):
    'Locate the leftmost value equal to <x> in array <a>'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError


if __name__ == '__main__':
    items = [1, 5, 6, 11, 15, 17, 19, 20, 24, 29]
    items.insert(bisect_left(items, 16), 16)
    print(items)
    insort_left(items, 22)
    print(items)

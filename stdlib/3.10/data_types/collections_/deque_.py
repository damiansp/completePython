from collections import deque


d = deque()
d.append(2)
d.append(4)
print(d.count(4))  # 1
d.extend([6, 8, 2])
d.extendleft([-4, -2, 0])
print(d.index(0))  # 0
print(d)           # [0, -2, -4, 2, 4, 6, 8, 2]
e = d.copy()
d.clear()
e.insert(3, 0)
print(e.pop())      # 2
print(e.popleft())  # 0
e.remove(2)
print(e)            # [-2, -4, 0, 4, 6, 8]
e.reverse()
print(e)            # [8, 6, 4, 0, -4, -2]
e.rotate()
print(e)            # [-2, 8, 6, 4, 0, -4]


d = deque('ghi')
for elem in d:
    print(elem.upper())

d.append('j')
d.appendleft('f')
print(d)
print(d.pop())
print(d.popleft())
print(list(d))
print(d[0])
print(d[-1])
print(list(reversed(d)))
print('h' in d)
d.extend('jkl')
print(d)
d.rotate(-1)
print(deque(reversed(d)))
d.clear()
d.extendleft('abc')
print(d)
      

def tail(filename, n=10):
    '''Return the last n lines of a file'''
    with open(filename, 'r') as f:
        return deque(f, n)


def moving_avg(iterable, window=3):
    it = iter(iterable)
    d = deque(itertools.islice(it, window - 1))
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / n


def round_robing(*iterables):
    '''round_robing('ABC', 'D', 'EF') -> A D E B F C'''
    iterators = deque(map(iter, iterables))
    while iterators:
        try:
            while True:
                yield next(iterators[0])
                iterators.rotate(-1)
        except StopIteration:
            iterators.popleft()


def delete_nth(d, n):
    d.rotate(-n)
    d.popleft()
    d.rotate(n)



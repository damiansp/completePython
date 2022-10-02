from collections import defaultdict
import time


def test_dict(iters=1_000_000):
    start = time.time()
    for _ in range(iters):    
        d = {}
        d.setdefault('x', None)
    end = time.time() - start
    print('time:', end)


def test_ddict(iters=1_000_000):
    start = time.time()
    for _ in range(iters):    
        d = defaultdict(lambda: None)
        d['x']
    end = time.time() - start
    print('time:', end)


test_dict()
test_ddict()


s = 'mississippi'
d = defaultdict(int)
for char in s:
    d[char] += 1
print(list(d.items()))
print(d['k'])
print(list(d.items()))

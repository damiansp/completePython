# deque is a doubly-linked list, fast for inserting at head/tail but slower at
# accessing by index; good when doing a lot of pop/append/insert
from collections import deque
import time


REPS = 1_000_000


def test_list():
    start = time.time()
    seq = list(range(10))
    for _ in range(REPS):
        seq.append(0)
        seq.pop()
    elapsed = time.time() - start
    mean = elapsed / REPS
    print(f'Mean per list:  {mean:.9f}')


def test_deque():
    start = time.time()
    seq = deque(range(10))
    for _ in range(REPS):
        seq.append(0)
        seq.pop()
    elapsed = time.time() - start
    mean = elapsed / REPS
    print(f'Mean per deque: {mean:.9f}')


if __name__ == '__main__':
    test_list()
    test_deque()
    

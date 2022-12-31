# the heap is a binary tree
from dataclasses import dataclass, field
import heapq
import itertools
from typing import Any


x = [29, 100, 98, 5, 13, 59, 17, 73, 40, 16]
heapq.heapify(x)

heapq.heappush(x, 87)
print(heapq.heappop(x))
print(heapq.heappushpop(x, 100))
heapq.heapreplace(x, 12)  # replaces smallest with 12

y = [37, 62, 66, 1, 64]
z = heapq.merge(x, y)
print(list(z))
print(heapq.nlargest(3, x))
print(heapq.nsmallest(3, x))


def heapsort(iterable):
    h = []
    for val in iterable:
        heapq.heappush(h, val)
    return [heapq.heappop(h) for _ in range(len(h))]


x = [89, 29, 87, 56, 95, 43, 92, 61, 14, 58]
print(heapsort(x))


h = []
heapq.heappush(h, (5, 'write code'))
heapq.heappush(h, (7, 'release product'))
heapq.heappush(h, (1, 'write spec'))
heapq.heappush(h, (3, 'create tests'))
print(heapq.heappop(h))


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)


pq = []                      # list of entries arranged in a heap
entry_finder = {}            # mapping: task -> entry
REMOVED = '<removed-task>'   # placeholder for removed task
counter = itertools.count()  # unique seq count


def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heappush(pq, entry)


def remove_task(task):
    'Mark an existing task as REMOVED. Raise KeyError if not found'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED


def pop_task():
    'Remove and return the lowest-priority task. Raise KeyError if empty'
    while pq:
        priority, count, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')


                             

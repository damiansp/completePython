import heapq


class PriorityQueue:
    def __init__(self):
        self._q = []
        self._idx = 0

    def push(self, item, priority):
        heapq.heappush(self._q, (-priority, self._idx, item))
        self._idx += 1

    def pop(self):
        return heapq.heappop(self._q)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Item({self.name!r})'


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('ham'), 1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

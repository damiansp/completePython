from array import array
import bisect
from collections import deque
from heapq import heapify, heappop, heappush


a = array('H', [4000, 10, 700, 22222]) # H: store as unsigned 16-byte binary
print(a)
print(sum(a))
print(a[1:3])

d = deque(['task1', 'task2', 'task3'])
d.append('task4')
print('Handling:', d.popleft())

#unsearched = deque([starting_node])

def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)

scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores)

data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data) # rearrange list into heap order (sort)
print(data)
heappush(data, -5)
print([heappop(data) for _ in range(3)]) # [-5, 0, 1]

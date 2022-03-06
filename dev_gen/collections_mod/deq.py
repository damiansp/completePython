from collections import deque


d = deque(['name', 'age', 'DOB'])
print(d)

d.append('POB')
d.appendleft('id')
print(d)

last = d.pop()
print(last)
first = d.popleft()
print(first)
print(d)

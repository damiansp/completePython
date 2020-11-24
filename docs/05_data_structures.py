from collections import deque

# Lists
a = [1, 2]
a.append(3)
print(a) # 1 2 3

a.extend([4, 5])
print(a) # 1 2 3 4 5
a.extend((6, 7))
print(a) # 1 2 3 4 5 6 7

a.insert(2, 8)
print(a) # 1 2 8 3 4 5 6 7

a.remove(8)
print(a) # 1 2 3 4 5 6 7

print(a.pop()) # 7
print(a)       # 1 2 3 4 5 6
a.insert(2, 8)
print(a)       # 1 2 8 3 4 5 6
print(a.pop(3)) # 3
print(a)        # 1 2 8 4 5 6

a.clear()
print(a) # []

a = [3, 2, 1]
print(a.index(1)) # 2

a.append(3)
print(a.count(3)) # 2

a.reverse()
print(a) # 3 1 2 3

b = a.copy()
print(b == a[:]) # True

b.sort()
print(b) # 1 2 3 3

del b[0]
print(b) # 2 3 3
del b[:]
print(b) # []

queue = deque(['Eric', 'John', 'Michael'])
queue.append('Terry')
queue.append('Graham')
print(queue.popleft()) # Eric
print(queue.popleft()) # John
print(queue)           # Michael Terry Graham

vec = [[1, 2], [3, 4], [5, 6]]
flat = [n for elem in vec for n in elem]
print(flat) # 1 2 3 4 5 6



# Tuples, Sequences
empty = ()
single = 1,
print(len(empty), len(single)) # 0 1

# the heap is a binary tree
import heapq


x = [29, 100, 98, 5, 13, 59, 17, 73, 40, 16]
heapq.heapify(x)

heapq.heappush(x, 87)
print(heapq.heappop(x))
print(heapq.heappushpop(x, 100))
heapq.heapreplace(x, 12)  # replaces smallest with 12

y = [37, 62, 66, 1, 64]
z = heapq.merge(x, y)
print(list(z))


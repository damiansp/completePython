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



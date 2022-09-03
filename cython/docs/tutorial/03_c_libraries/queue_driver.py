import time

import queue


Q = queue.Queue()
Q.append(10)
Q.append(20)
print(Q.peek())
print(Q.pop())
print(Q.pop())
try:
    print(Q.pop())
except IndexError as e:
    print(e)


i = 10_000
vals = range(i)
start = time.time()
Q.extend(vals)
end = time.time() - start
print(f'Adding {i} items tood {end:1.3f} ms')

for i in range(42):
    Q.pop()

print('the answer is:')
print(Q.pop())

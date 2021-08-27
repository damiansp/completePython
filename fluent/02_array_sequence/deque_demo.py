from collections import deque

dq = deque(range(10), maxlen=10) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(dq)

dq.rotate(3)                     # [7, 8, 9, 0, 1, 2, 3, 4, 5, 6]
print(dq)

dq.rotate(-4)                    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(dq)

dq.appendleft(-1)                # [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9] # last lost
print(dq)

dq.extend([11, 22, 33])          # [3, 4, 5, 6, 7, 8, 9, 11, 22, 33] #first lost
print(dq)

dq.extendleft([10, 20, 30])      # [30, 20, 10, 3, 4, 5, 6, 7, 8, 9] 
print(dq)

      

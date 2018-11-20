'''
A coroutine for computing a running mean
'''

from inspect import getgeneratorstate

from coroutil import coroutine


@coroutine
def averager():
    total = 0.
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count

        
coro_avg = averager()
print(getgeneratorstate(coro_avg)) # 'GEN_SUSPENDED' (ready to go)
print(coro_avg.send(10)) # 10.
print(coro_avg.send(30)) # 20.
print(coro_avg.send(5))  # 15.

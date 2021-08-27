def averager():
    total = 0.
    count = 0
    avg = None
    while True:
        term = yield avg
        total += term
        count += 1
        avg = total / count


coro_avg = averager()
print(next(coro_avg))    # None (necessary "priming")
print(coro_avg.send(10)) # 10.0
print(coro_avg.send(30)) # 20.0
print(coro_avg.send(5))  # 15.0


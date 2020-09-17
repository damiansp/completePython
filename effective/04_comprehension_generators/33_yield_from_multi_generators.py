import timeit


def move(period, speed):
    for _ in range(period):
        yield speed

def pause(delay):
    for _ in range(delay):
        yield 0

def animate():
    for delta in move(4, 5.):
        yield delta
    for delta in pause(3):
        yield delta
    for delta in move(2, 3.):
        yield delta

def render(delta):
    print(f'Delta: {delta:.1f}')
    # move and image...

def run(func):
    for delta in func():
        render(delta)

run(animate) # 5 5 5 5 0 0 3 3


# cleaner version:
def animate_composed():
    yield from move(4, 5.)
    yield from pause(3)
    yield from move(2, 3.)

run(animate_composed) # same


def child():
    for i in range(1_000_000):
        yield i

def slow():
    for i in child():
        yield i

def fast():
    yield from child()


baseline = timeit.timeit(
    stmt='for _ in slow(): pass', globals=globals(), number=50)
print(f'Manual nesting: {baseline:.2f}s')
comparison = timeit.timeit(
    stmt='for _ in fast(): pass', globals=globals(), number=50)
print(f'Composed nesting: {comparison:.2f}s')
perc = -(comparison - baseline) / baseline
print(f'{perc:.1%} less time')

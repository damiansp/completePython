def next_(n, x):
    return (x + n/x) / 2

n = 2
f = lambda x: next_(n, x)
a0 = 1.
# successive approximations to sqrt(2) starting with 1 as initial guess
[print(round(x, 4)) for x in (a0, f(a0), f(f(a0)), f(f(f(a0))))]


def repeat(f, a):
    yield a
    for v in repeat(f, f(a)):
        yield v

        
def within(epsilon, iterable):
    def head_tail(epsilon, a, iterable):
        b = next(iterable)
        if abs(a - b) <= epsilon: return b
        return head_tail(epsilon, b, iterable)
    return head_tail(epsilon, next(iterable), iterable)


def sqrt(n, initial_estimate=1, tolerance=1e-07):
    return within(tolerance, repeat(lambda x: next_(n, x), initial_estimate))

print(sqrt(7))

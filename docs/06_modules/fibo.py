# Fibonacci numbers module


def fib(n):
    '''Return Fibonacci numbers <= n'''
    a, b = 0, 1
    while a <= n:
        print(a, end=' ')
        a, b = b, a + b
    print()


def fib2(n):
    res = []
    a, b = 0, 1
    while a <= n:
        res.append(a)
        a, b = b, a + b
    return res

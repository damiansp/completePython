import functools
import html

from simple_decorator import better_clock as clock


@clock
def fibonacci_old(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)




if __name__ == '__main__':
    print(fibonacci_old(6))
    print(fibonacci(6))
    print(htmlize({1, 2, 3}))
    print(htmlize(abs))
    print(htmlize(42))
    print(htmlize(['alpha', 66, {3, 2, 1}]))

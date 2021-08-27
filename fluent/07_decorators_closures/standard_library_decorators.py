import functools
import html
import numbers
from collections import abc
from functools import singledispatch

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


@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br\>\n')
    return '<p>{0}</p>'.format(content)


@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)


@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'



if __name__ == '__main__':
    print(fibonacci_old(6))
    print(fibonacci(6))
    print(htmlize({1, 2, 3}))
    print(htmlize(abs))
    print(htmlize(42))
    print(htmlize(['alpha', 66, {3, 2, 1}]))

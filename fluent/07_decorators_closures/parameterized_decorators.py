import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'
registry = set()

def register(active=True):
    def decorate(func):
        print('running register(active=%s) -> decorate(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
            return func
    return decorate


@register(active=False)
def f1():
    print('running f1()')

    
@register()
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        def clocked(*_args):
            t0 = time.time()
            _result = func(*_args)
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))
            return _result
        return clocked
    return decorate


if __name__ == '__main__':
    print('running main()')
    print(registry)
    print(register()(f3))
    print(registry)
    print(register(active=False)(f2))
    print(registry)

    @clock()
    def snooze(seconds):
        time.sleep(seconds)

    @clock('{name}: {elapsed}s')
    def snooze2(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze(0.123)
        snooze2(0.123)


from inspect import getgeneratorstate

class DemoException(Exception):
    '''An exception type for demonstration'''


def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled famously.  Carry on...')
        else:
            print('-> coroutine received: {!r}'.format(x))
    raise RuntimeError('Unreachable!')


exc_coro = demo_exc_handling()
next(exc_coro)    # -> coroutine started
exc_coro.send(11) # -> coroutine received: 11
exc_coro.send(22) # -> coroutine received: 22
exc_coro.close()
print(getgeneratorstate(exc_coro)) # GEN_CLOSED


exc_coro = demo_exc_handling()
next(exc_coro)                     # -> coroutine started
exc_coro.send(11)                  # -> coroutine received: 11
exc_coro.throw(DemoException)      # *** DemoException handled famously....
print(getgeneratorstate(exc_coro)) # GEN_SUSPENDED
#exc_coro.throw(ZeroDivisionError) # breaks (unhandled error)



def demo_finally():
    print('-> coroutine started')
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('*** DemoException handled.')
            else:
                print('-> coroutine received: {!r}'.format(x))
    finally:
        print('-> coroutine ending')


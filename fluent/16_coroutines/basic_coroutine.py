from inspect import getgeneratorstate


def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received')

my_coro = simple_coroutine()
print(my_coro) # <generator object... >
print(next(my_coro))
#my_coro.send(42) # prints then throws StopIteration

another_coro = simple_coroutine()
#another_coro.send(123)
# TypeError: can't send non-None value to just started generato


def coro3(a):
    print('-> Started: a =', a)
    b = yield a
    print('Received: b =', b)
    c = yield a + b
    print('Received: c =', c)

c3 = coro3(14)
print(getgeneratorstate(c3)) # GEN_CREATED
print(next(c3))              # -> Started: a = 14; 14
print(getgeneratorstate(c3)) # GEN_SUSPENDED
print(c3.send(-10))          # b = -10; 4
print(getgeneratorstate(c3)) # GEN_SUSPENDED
#print(c3.send(20))           # c = 20 then StopIteration
#print(getgeneratorstate(c3))# GEN_CLOSED


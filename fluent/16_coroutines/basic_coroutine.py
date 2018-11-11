def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received')

my_coro = simple_coroutine()
print(my_coro) # <generator object... >
print(next(my_coro))
my_coro.send(42)

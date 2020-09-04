from functools import wraps
import pickle


def trace(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) -> {res!r}')
        return res
    return wrapper


@trace
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)

# @trace equiv to: fibonacci = trace(fibonacci)


fibonacci(4)

# but the wrapped function doesn't think its name is "fibonacci"
print(fibonacci) # <function trace.<locals>.wrapper at 0x7fa2ed1285e0>

# Also cannot pickle:
#pickle.dumps(fibonacci) # AttributeError



# Using functools.wraps
def trc(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) -> {res!r}')
        return res
    return wrapper

@trc
def fib(n):
    if n in (0, 1):
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)

print(fib) # <function fib at 0x7fbba59f0040>
print(pickle.dumps(fib)) # b'\x80\x04\x95\x14\x00\x00...

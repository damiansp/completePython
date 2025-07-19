def uppercase_decorator(f):
    def wrapper(*args):
        orig_res = f(*args)
        return orig_res.upper()

    return wrapper


@uppercase_decorator
def greet(name):
    return f'hello, {name}'


print(greet('bob dobolina'))

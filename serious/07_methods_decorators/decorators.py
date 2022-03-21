_functions = {}


def register(f):
    global _functions
    _functions[f.__name__] = f
    return f


@register
def foo():
    return 'bar'


print(_functions)


class Storage:
    def __init__(self, items=None):
        self.items = items

    def get(item):
        self.items.pop(item)

    def put(item):
        self.items.append(item)

        
class Store:
    def __init__(self, items=None):
        self.storage = Storage(items)
        
    def get_food(self, username, food):
        if username != 'admin':
            raise Exception('User is not allowed to get food')
        return self.storage.get(food)

    def put_food(self, username, food):
        if username != 'admin':
            raise Exception('User is not allowed to put food')
        self.storage.put(foot)

    
def check_is_admin(username):
    if username != 'admin':
        raise Exception('User not allowed to access storage')


class Store:
    def __init__(self, items=None):
        self.storage = Storage(items)

    def get_food(self, username, food):
        check_is_admin(username)
        return self.storage.get(food)

    def put_food(self, username, food):
        check_is_admin(username)
        return self.storage.put(food)


def check_is_admin(f):
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception('User not allowed to access storage')
        return f(*args, **kwargs)
    return wrapper


class Store:
    def __init__(self, items=None):
        self.storage = Storage(items)

    @check_is_admin
    def get_food(self, username, food):
        return self.storage.get(food)

    @check_is_admin
    def putt_food(self, username, food):
        return self.storage.put(food)



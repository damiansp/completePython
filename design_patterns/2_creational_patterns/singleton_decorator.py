def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Singleton:
    def do_stuff(self):
        pass


s1 = Singleton()
s2 = Singleton()
print(s1 is s2)

from collections import UserList


class InstanceCountingClass:
    created = 0
    number: int

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.number = cls.created
        cls.created += 1
        return instance

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.number} of {self.created}>'


instances = [InstanceCountingClass() for _ in range(5)]
for i in instances:
    print(i)


class NonZero(int):
    def __new__(cls, value):
        return super().__new__(cls, value) if value != 0 else None

    def __init__(self, skipped_val):
        # implementation of __init__ could be skipped in this case, but it is
        # left to present how it may not be called
        print('__init__() called')  # unreachable if NonZero(0)
        super().__init__()


print(type(NonZero(12)))
print(type(NonZero(0)))
print(NonZero(-3.124))


# __new__ useful for subtyping immutables: int, str, float, frozenset, etc.
# Consider factory methods as alternative, e.g.:
class XList(UserList):
    @classmethod
    def double(cls, iterable):
        return cls(iterable) * 2

    @classmethod
    def triple(cls, iterable):
        return cls(iterable) * 3


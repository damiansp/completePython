from collections.abc import Sized


class HasLen:
    def __len__(self):
        return 10


print(issubclass(HasLen, Sized))  # True

# similarly:
# __contains__ < Container
# __hash__     < Hashable
# __iter__     < Iterable
# __call__     < Callable

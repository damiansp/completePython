from typing import Any, Iterable


UNSET = object()


def repr_instance(instance: object, attrs: Iterable[str]) -> str:
    attr_values: dict[str, Any] = {
        attr: getattr(instance, attr, UNSET) for attr in attrs}
    sub_repr = ', '.join(
        f'{attr}={repr(val) if val is not UNSET else "UNSET"}'
        for attr, val in attr_values.items())
    return f'<{instance.__class__.__qualname__}: {sub_repr}>'


print(repr_instance(1+10j, ['real', 'imag']))


def autorepr(cls):
    attrs = set.union(
        *(
            set(c.__annotations__.keys())
            for c in cls.mro() if hasattr(c, '__annotations__')))

    def __repr__(self):
        return repr_instance(self, sorted(attrs))

    cls.__repr__ = __repr__
    return cls


@autorepr
class MyClass:
    attr_a: Any
    attr_b: Any
    attr_c: Any

    def __init__(self, a, b):
        self.attr_a = a
        self.attr_b = b


print(MyClass('Ultimate answer', 42))
print(MyClass([1, 2, 3], ['a', 'b', 'c']))
inst = MyClass(None, None)
inst.attr_c = None
print(inst)
                         
# Don't do: overrides class __name__, __qualname__, __doc__, etc        
def autorepr(cls):
    attrs = cls.__annotations__.keys()

    class Klass(cls):
        def __repr__(self):
            return repr_instance(self, attrs)

    return Klass



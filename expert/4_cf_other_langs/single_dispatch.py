from datetime import datetime
from functools import singledispatch, singledispatchmethod
from numbers import Real


@singledispatch
def report(val):
    return f'raw: {val}'


@report.register
def _(val: datetime):
    return f'dt: {val.isoformat()}'


@report.register
def _(val: complex):
    return f'complex: {val.real}{val.imag:+}i'

# alternately
#@reprt.register(complex)
#def _(val):
#    return f'complex: {val.real}{val.imag:+}i'

@report.register
def _(val: Real):
    return f'real: {val:f}'


print(report(datetime.now()))
print(report(3-4j))
print(report(9001))
print(report('January'))

for k, v in report.registry.items():
    print(f'{k} -> {v}')

    
class Example:
    @singledispatchmethod
    def method(self, arg):
        pass

    @method.register
    def _(self, arg: float):
        pass

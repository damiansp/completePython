class LazyRecord:
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = f'Value for {name}'
        setattr(self, name, value)
        return value


data = LazyRecord()
print('Before:', data.__dict__)
print('foo:', data.foo)
print('After:', data.__dict__)


class LoggingLazyRecord(LazyRecord):
    def __getattr__(self, name):
        print(f'* Called __getattr__({name!r}), populating instance dictionary')
        result = super().__getattr__(name)
        print(f'* Returning {result!r}')
        return result


data = LoggingLazyRecord()
print('exists: ', data.exists)
print('First Foo: ', data.foo)
print('Second Foo: ', data.foo)


class ValidatingRecord:
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name):
        print(f'* Called __getattribute__({name!r})')
        try:
            value = super().__getattribute__(name)
            print(f'* Found {name!r}, returning {value!r}')
            return value
        except AttributeError:
            value = f'Value for {name}'
            print(f'* Setting {name!r} to {value!r}')
            setattr(self, name, value)
            return value


data = ValidatingRecord()
print('exists: ', data.exists)
print('First Foo: ', data.foo)
print('Second Foo: ', data.foo)


class MissingPropertyRecord:
    def __getattr__(self, name):
        if name == 'bad_name':
            raise AttributeError(f'{name} is missing')
        pass


data = MissingPropertyRecord()
#data.bad_name # AttributeError


data = LoggingLazyRecord()
print('Before:         ', data.__dict__)
print('Has first foo:  ', hasattr(data, 'foo'))
print('After:          ', data.__dict__)
print('Has second foo: ', hasattr(data, 'foo'))

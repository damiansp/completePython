from unittest import mock


m = mock.Mock()
m.some_attribute = 'hello'
m.some_method.return_value = 42
print(m.some_method())
print(m.some_method('with', 'args'))


def print_hello():
    print('hello, world!')
    return 43

m.some_method.side_effect = print_hello
m.some_method()
print(m.some_method.call_count)

m.some_method('foo', 'bar')
m.some_method.assert_called_once_with('foo', 'bar')
m.some_method.assert_called_once_with('foo', mock.ANY)
m.some_method.assert_called_once_with('foo', 'baz')  # assertion err
              

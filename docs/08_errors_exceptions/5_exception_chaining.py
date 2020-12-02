#raise RuntimeError from exc # where exc is Exception instance or None

def func():
    raise IOError

'''
try:
    func()
except IOError as e:
    raise RuntimeError('Failed to open database') from e
'''

'''
try:
    open('database.sqlite')
except IOError:
    raise RuntimeError from None
'''


import contextlib


class MyBasicContext:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, ecv_value, traceback):
        pass


@contextlib.contextmanager
def my_context():
    print('Do something first')
    yield
    print('Do something last')


with my_context():
    print('Hello, World!')


@contextlib.contextmanager
def meaningful_context():
    print('Do something first')
    yield 42
    print('Do something last')


with meaningful_context() as meaning:
    print(meaning)


@contextlib.contextmanager
def meaningful_context2():
    print('Do something first')
    try:
        yield 42
    finally:
        print('Do something last')


#with meaningful_context2() as meaning:
#    print('Raise da roof!')
#    raise ValueError('Raise it!')
#    print(meaning)


# multiple better combined... instead of:
'''
with open('f1', 'r') as infile:
    with open('f2', 'w') as outfile:
        outfile.write(infile.read())
'''
# do:
'''
with open('f1', 'r') as infile, open('f2', 'w') as outfile:
    outfile.write(infile.read())
'''

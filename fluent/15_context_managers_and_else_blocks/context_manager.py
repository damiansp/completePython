import contextlib


@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    yield 'Jabberwocky'
    sys.stdout.write = original_write


with looking_glass() as what:
    print('Oh, say can you see?')
    print(what)


# The above has a flaw: if exception raised in with block, interpreter will
# catch it and raise again in the yield expression in looking_glass, but
# currently no error handling; will abort without restoring sys.stdout.write

# Better:
@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write[::-1]

    sys.stdout.write = reverse_write
    msg = ''
    try:
        yield 'Jabberwocky'
    except ZeroDivisionError:
        msg = 'Please do not divide by 0!'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)



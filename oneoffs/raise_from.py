def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError('cannot divide by 0')


def div2(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('cannot divide by 0') from e


try:
    div2(5, 0)
except ValueError as e:
    print('Error:\n cause:', e.__cause__)
    print(' Exception:', e)


def div3(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError('cannot divide by 0') from None


try:
    div3(5, 0)
except ValueError as e:
    print('Error:\n cause:', e.__cause__)
    print(' Exception:', e)

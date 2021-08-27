# Prefer raising exceptions to returning None

def careful_divide(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None


def better_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError('Invalid inputs')


def alternate_divide(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError('Invalid inputs')


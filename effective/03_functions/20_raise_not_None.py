# Prefer raising exceptions to returning None
def careful_divide(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None


def safe_division(n, divisor, ingnore_overflow, ignore_zero_div):
    try:
        return n / divisor
    except OverflowError:
        return 0
    except ZeroDivisionError:
        if ignore_zero_div:
            return float('inf')
        else:
            raise

res = safe_division(1., 10**500, True, False)
print(res) # 0

res = safe_division(1., 0, False, True)
print(res) # inf

# ...but easy to confuse order of args
# Accept ONLY kwargs after div:
def safer_div(n, divisor, *, ignore_overflow=False, ignore_zero_div=False):
    try:
        return n / divisor
    except OverflowError:
        return 0
    except ZeroDivisionError:
        if ignore_zero_div:
            return float('inf')
        else:
            raise

#safer_div(1., 10**500, True, False) # TypeError
print(safer_div(1., 10**500, ignore_overflow=True)) # 0
# But...
print(safer_div(n=2, divisor=5)) # TypeError in some versions


def saferer_div(n, div, /, *, ignore_overflow=False, ignore_zero_div=False):
    try:
        return n / divisor
    except OverflowError:
        return 0
    except ZeroDivisionError:
        if ignore_zero_div:
            return float('inf')
        else:
            raise


#print(saferer_div(n=2, div=5)) # TypeError


def safest_div(
        n, div, /, ndigits=10, *, ignore_overflow=False, ignore_zero_div=False):
    try:
        frac = n / div
        return round(frac, ndigits)
    except OverflowError:
        if ignore_overflow:
            return 0
        raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        raise

print(safest_div(22, 7))
print(safest_div(22, 7, 5))
print(safest_div(22, 7, ndigits=4))

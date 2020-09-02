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


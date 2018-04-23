def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    def is_coprime(k, coprime):
        if k < coprime * coprime: # ??? 4 < 64, but 4 not comprime with 8
            return True
        if k % coprime == 0:
            return False
        return is_coprime(k, coprime + 2)

    return is_coprime(n, 3)


# Tail-call optimization (TCO)
def is_prime2(p):
    if p < 2:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    return not any(p == 0 for p in range(3, int(math.sqrt(p)) + 1, 2))

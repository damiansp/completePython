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



from decimal import Decimal, getcontext

print(round(0.7 * 1.05, 2))                        # 0.73
print(round(Decimal('0.70') * Decimal('1.05'), 2)) # 0.74

print(1. % 0.1)                       # 0.09999999999995
print(Decimal('1.') % Decimal('0.1')) # 0.0

print(sum([0.1] * 10) == 1.)                       # False
print(sum([Decimal('0.1')] * 10) == Decimal('1.')) # True

getcontext().prec = 36
print(Decimal(1) / Decimal(7))

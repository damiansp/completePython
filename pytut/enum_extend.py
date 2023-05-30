from enum import Enum


class PaymentStatus(Enum):
    PENDING = 1
    COMPLETED = 2
    REFUNDED = 3

    def __str__(self):
        return f'{self.name.lower()}({self.value})'

    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other
        if isinstance(other, PaymentStatus):
            return self is other
        return False

    def __lt__(self, other):
        if isinstance(other, int):
            return self.value < other
        if isinstance(other, PaymentStatus):
            return self.value < other.value
        return False

    def __gt__(self, other):
        if isinstance(other, int):
            return self.value > other
        if isinstance(other, PaymentStatus):
            return self.value > other.value
        return False

    def __le__(self, other):
        return self < other or self == other

    def __bool__(self):
        return self is self.COMPLETED


print(PaymentStatus.PENDING)
if PaymentStatus.PENDING == 1:
    print('Payment pending...')


status = 1
if PaymentStatus.COMPLETED > status:
    print('The payment has not completed.')

status = PaymentStatus.COMPLETED
if PaymentStatus.COMPLETED <= status:
    print('The payment is not pending.')
    
for member in PaymentStatus:
    print(member, bool(member))

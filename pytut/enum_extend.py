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
    


print(PaymentStatus.PENDING)
if PaymentStatus.PENDING == 1:
    print('Payment pending...')

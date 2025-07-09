class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amt):
        if amt > 0:
            self.__balance += amt
            return True
        return False

    def withdraw(self, amt):
        if amt > 0 and amt <= self.__balance:
            self.__balance -= amt
            return True
        return False

    @property
    def balance(self):
        return self.__balance

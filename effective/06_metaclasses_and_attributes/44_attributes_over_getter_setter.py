class OldResistor:
    def __init__(self, ohms):
        self._ohms = ohms

    def get_ohms(self):
        return self._ohms

    def set_ohms(self, ohms):
        self._ohms = ohms


r0 = OldResistor(50e3)
print('Before:', r0.get_ohms())
r0.set_ohms(10e3)
print('After:', r0.get_ohms())

# Clumsy:
r0.set_ohms(r0.get_ohms() - 4e3)


class Resistor:
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0

# Tidy
r1 = Resistor(50e3)
r1.ohms = 10e3
r1.ohms -= 5e3


class VoltageResistor(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms

r2 = VoltageResistor(1e3)
print(f'Before: {r2.current:.2f} amps')
r2.voltage = 10
print(f'After: {r2.current:.2f} amps')


class BoundedResistor(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError(f'ohms must be > 0 (got {ohms})')
        self._ohms = ohms

r3 = BoundedResistor(1e3)
#r3.ohms = 0 # ValueError
r3.ohms = 1e5 


# r4 = BoundedResistor(-7) # ValueError


class FixedResistor(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError('Ohms is immutable')
        self._ohms = ohms


r5 = FixedResistor(1e3)
#r5.ohms = (2e3) # AttributeError


# Don't do this
class MysteriousResistor(Resistor):
    @property
    def ohms(self):
        self.voltage = self._ohms * self.current # unexpected
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        self._ohms = ohms



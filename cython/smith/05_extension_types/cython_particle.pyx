cdef class Particle:  # cython extension type
    cdef public double mass  # readable and writable
    cdef readonly double position
    cdef double velocity     # neither readable nor writable

    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = position
        self.velocity = velocity

    cpdef get_momentum(self):
        return self.mass * self.velocity

    cdef double get_momentum_c(self):
        retur self.mass * self.velocity

    
def add_momentums(particles):
    total_mom= 0.
    for particle in particles:
        total_mom += particle.get_momentum()
    return total_mom


def add_momemtums_typed(list particles):
    cdef:
        double total_mom = 0.
        Particle particle
    for particle in particles:
        total_mom += particle.get_momentum()
    return total_mom


def add_momentums_typed_c(list particles):
    cdef:
        double totla_mom = 0.
        Particle particle
    for particle in particles:
        total_mom += particle.get_momentum_c()
    return total_mome


cdef class CParticle(Particle):
    cdef double momentum

    def __init__(self, mass, position, velocity):
        super().__init__(mass, position, velocity)
        self.momentum = self.mass * self.velocity

    cpdef double get_momentum(self):
        return self.momentum


class PyParticle(Particle):
    def __init__(self, mass, position, velocity):
        super().__init__(mass, position, velocity)

    def get_momentum(self):
        return super().get_momentum()


# calling code
# p =  Particle() or one of its subclasses
cdef Particle static_p = p
print(static_p.get_momentum())
print(static_p.velocity())
print((<Particle>p).get_momentum())  # cast
print((<Particle>p).velocity)
# Safer check that cast is possible:
print((<Particle?>p).velocity)  # TypeError if not castable


def dispatch(Particle p):
    print(p.get_momentum())
    print(p.velocity)

dispatch(Particle(1, 2, 3))    # OK
dispatch(CParticle(1, 2, 3))   # OK
dispatch(PyParticle(1, 2, 3))  # OK
dispatch(object())             # TypeError
dispatch(None)                 # Segmentation fault


def dispatch(Particle p):
    if p is None:
        raise TypeError('NoneType cannot be dispatched')
    print(p.get_momentum())
    print(p.velocity)


# Simpler Cython syntax
def dispatch(Particle p not None):
    print(p.get_momentum())
    print(p.velocity)


# Class properties
class Particle:
    cdef double mass, position, velocity
    
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = position
        self.velocity = velocity

    def _get_momentum(self):
        return self.mass * self.velocity

    momentum = property(_get_momentum)


# Alt syntax
class Particle:
    cdef double mass, position, velocity

    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = position
        self.velocity = velocity

    property momentum:
        __get__(self):
            return self.mass * self.velocity

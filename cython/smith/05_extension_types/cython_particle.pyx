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





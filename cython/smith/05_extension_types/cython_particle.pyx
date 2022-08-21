cdef class Particle:  # cython extension type
    cdef public double mass  # readable and writable
    cdef readonly double position
    cdef double velocity     # neither readable nor writable

    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = position
        self.velocity = velocity

    def get_momentum(self):
        return self.mass * self.velocity




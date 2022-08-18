cdef class Particle:  # cython extension type
    cdef double mass, position, velocity

    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = position
        self.velocity = velocity

    def get_momentum(self):
        return self.mass * self.velocity




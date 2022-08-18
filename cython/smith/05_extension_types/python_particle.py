class Particle:  # python class
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = position
        self.velocity = velocity

    def get_momentum(self):
        return self.mass * self.velocity

from util import Point

class Ball:
    def __init__(
        self, center, radius, velocity, energy, elasticity, color, outline):

        self.center = center
        self.radius = radius
        self.velocity = velocity
        self.energy = energy
        self.elasticity = elasticity
        self.color = color
        self.outline = outline

    def get_bb(self):
        p1 = self.center - Point(self.radius, self.radius)
        p2 = self.center + Point(self.radius, self.radius)
        return [p1.as_list(), p2.as_list()]

from ...core.object.object import SimObject
from pygame import Vector2

class Body(SimObject):
    def __init__(self, pos, radius, mass, color = 'yellow'):
        SimObject.__init__(self, pos, radius, color)
        self.mass = mass
        self.vel = Vector2()
        self.fx = 0
        self.fy = 0
        self.acc = Vector2()

    def update(self, dt):
        self.vel += dt * self.acc
        self.pos += dt * self.vel
        #print("ACC: " + str(self.acc) + ", VEL: " + str(self.vel))
        self.acc = Vector2()
        self.fx = 0
        self.fy = 0

    def draw(self, surface):
        super().draw(surface)
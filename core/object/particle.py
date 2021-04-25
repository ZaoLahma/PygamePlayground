from pygame import draw
from pygame import Vector2
from .object_storage import ObjectStorage

class Particle():
    def __init__(self, position, mass, radius, color = 'yellow'):
        self.pos = position
        self.mass = mass
        self.radius = radius
        self.color = color
        self.vel = Vector2()
        self.acc = Vector2()
        ObjectStorage.add_object(self)

    def update(self, dt):
        self.vel += dt * self.acc
        self.pos += dt * self.vel
        self.acc = Vector2()

    def draw(self, surface):
        draw.circle(surface, self.color, self.pos, self.radius)
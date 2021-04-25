from pygame import draw
from pygame import Vector2
from .object_storage import ObjectStorage

class SimObject():
    def __init__(self, position, radius, color = 'yellow'):
        #print("INIT CALLED")
        self.pos = position
        self.radius = radius
        self.color = color
        ObjectStorage.add_object(self)

    def draw(self, surface):
        draw.circle(surface, self.color, self.pos, self.radius)
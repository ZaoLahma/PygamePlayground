from ..core.body import Body
from ..core.physics import Physics

from pygame import Vector2
from random import randint

class SolarSystem():
    def __init__(self, sun_pos, sun_radius, sun_mass, num_bodies, max_radius):
        self.sun = Body(sun_pos, sun_radius, sun_mass, color = 'yellow')
        self.max_radius = max_radius

        for _ in range(0, num_bodies):
            self.create_body()

    def create_body(self):
        body = Body(Vector2(0, 0), 2, 5.9742 * 10 ** 24)
        radius = randint(12, self.max_radius)
        Physics.create_orbit(body, self.sun, radius)

        create_moon = randint(0, 100) > 50
        if True == create_moon:
            moon = Body(Vector2(0, 0), 2, 0.1742 * 10 ** 24)
            radius = randint(10, 15)
            Physics.create_orbit(moon, body, radius)
        
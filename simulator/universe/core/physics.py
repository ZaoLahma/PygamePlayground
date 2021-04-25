from ...core.object.object_storage import ObjectStorage

from pygame import Vector2
from math import sqrt
from math import atan2
from math import cos
from math import sin
from math import pi
from random import uniform

class Physics():
    G = 6.67428e-11
    AU = (149.6e6 * 1000)
    SCALE = 250 / AU

    def run(self, dt):
        objects = ObjectStorage.get_objects()
        sim_dt = 1
        self.apply_physics(objects, sim_dt)

    def apply_physics(self, objects, dt):
        for obj in objects:
            for other in objects:
                if obj is not other:
                    self.acc_forces(obj, other)

        for obj in objects:
            for other in objects:
                if obj is not other:
                    self.apply_gravity(obj, dt)

        for obj in objects:
            obj.update(dt)

    def acc_forces(self, obj, other):
        dx = other.pos[0] - obj.pos[0]
        dy = other.pos[1] - obj.pos[1]
        dx = dx / Physics.SCALE
        dy = dy / Physics.SCALE
        dist = sqrt(dx ** 2 + dy ** 2)
        f = Physics.G * obj.mass * other.mass / (dist ** 2)
        theta = atan2(dy, dx)
        fx = cos(theta) * f
        fy = sin(theta) * f
        obj.fx += fx
        obj.fy += fy

    def apply_gravity(self, obj, dt):
        obj.acc = Vector2(obj.fx / obj.mass * dt, obj.fy / obj.mass * dt)

    @staticmethod
    def create_orbit(obj, other, radius):
        theta = uniform( 0, 2 * pi )
        obj.pos = Vector2(radius * cos(theta), radius * sin(theta))
        obj.pos += other.pos
        v = sqrt(Physics.G * other.mass / radius) * Physics.SCALE
        obj.vel = Vector2(v * sin(theta), -v * cos(theta))
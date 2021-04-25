from simulator.core.window.window import Window
from simulator.universe.core.physics import Physics
from simulator.universe.core.body import Body
from pygame import Vector2

from random import randint

class Main:
    @staticmethod
    def run():
        print("Run called")
        window = Window("Particles", (1024, 768), 30)

        #body1 = Body(Vector2(100, 100), 2, 200)
        #body2 = Body(Vector2(200, 200), 2, 200)

        massive = Body(Vector2(612, 384), 10, 1.98892 * 10 ** 30)
        massive.vel = Vector2(0, -0.5)

        massive_2 = Body(Vector2(412, 384), 10, 1.98892 * 10 ** 30)
        massive_2.vel = Vector2(0, 0.5)

        num_particles = 10

        for _ in range(0, num_particles):
            x_pos = randint(0, 1024)
            y_pos = randint(0, 768)
            body = Body(Vector2(x_pos, y_pos), 2, 5.9742 * 10 ** 24)
            y_vel = 1
            if x_pos > 512:
                y_vel = -y_vel
            body.vel = Vector2(0, y_vel)

        physics = Physics()

        window.register_run_hook(physics.run)

        window.run()

if "__main__" == __name__:
    Main.run()
from simulator.core.window.window import Window
from simulator.universe.core.physics import Physics
from simulator.universe.core.body import Body
from simulator.universe.objects.solar_system import SolarSystem
from pygame import Vector2

class Main:
    @staticmethod
    def run():
        print("Run called")
        window = Window("Particles", (1024, 768), 30)

        solar_system = SolarSystem(Vector2(512, 384), 10, 1.98892 * 10 ** 30, 70, 70)

        solar_system_2 = SolarSystem(Vector2(200, 384), 10, 1.98892 * 10 ** 30, 70, 70)

        solar_system.sun.vel[1] = -0.5
        solar_system_2.sun.vel[1] = 0.5

        physics = Physics()

        window.register_run_hook(physics.run)

        window.run()

if "__main__" == __name__:
    Main.run()
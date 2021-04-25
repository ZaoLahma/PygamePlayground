from core.window.window import Window

class Main:
    @staticmethod
    def run():
        print("Run called")
        window = Window("Particles", (640, 480))
        window.run()

if "__main__" == __name__:
    Main.run()
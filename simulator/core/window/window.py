import pygame
from sys import exit
from ..object.object_storage import ObjectStorage

class Window():
    def __init__(self, title, resolution, fps):
        pygame.init()
        self.screen = pygame.display.set_mode(resolution)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.fps = fps

        self.run_hooks = []

    def register_run_hook(self, hook):
        self.run_hooks.append(hook)

    def run(self):
        while True:
            t_delta = self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            
            self.screen.fill(color = 'black')

            for run_hook in self.run_hooks:
                run_hook(t_delta)

            for obj in ObjectStorage.get_objects():
                obj.draw(self.screen)
            pygame.display.flip()
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

    def run(self):
        while True:
            t_delta = self.clock.tick(self.fps)
            s_delta = self.fps / 60
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            for obj in ObjectStorage.get_objects():
                obj.update(s_delta)
                obj.draw(self.screen)
            pygame.display.flip()
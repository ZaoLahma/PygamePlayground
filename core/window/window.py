import pygame
from sys import exit

class Window():
    def __init__(self, title, resolution):
        pygame.init()
        screen = pygame.display.set_mode(resolution)
        pygame.display.set_caption(title)


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            pygame.display.flip()
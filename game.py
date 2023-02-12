import pygame, sys, math
from pygame.locals import *

class Dashboard():
    def __init__(self):
        pass



class Game():
    def __init__(self, data):
        map_width = data["screen_dimensions"][0] 
        map_height = 7/8 * data["screen_dimensions"][1]
        self.map_surface = pygame.Surface((map_width, map_height))
        self.rect = self.map_surface.get_rect()

    def draw(self, screen):
        self.map_surface.fill((0,0,255))
        screen.blit(self.map_surface, self.rect)

    def loop(self, screen):
        self.draw(screen)

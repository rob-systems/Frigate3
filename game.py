import pygame, sys, math
from pygame.locals import *
import ast

pygame.init()
font_small = pygame.font.SysFont("Verdana", 20)

class Text_Overlay():
    def __init__(self, data):
        self.iter = 0
        self.cursor_iter = 0
        self.map = data
        self.dimensions = (data[0] * 11/12, data[1] / 7)
        self.text = ""

    def draw(self, screen):
        pygame.draw.rect(screen,
                         (255,255,255),
                         ((self.map[0] - self.dimensions[0]) / 2, 30, self.dimensions[0], self.dimensions[1]),  0, 3)
        if self.cursor_iter < 4:
            pygame.draw.rect(screen, (0,0,0), (self.iter * 10 + 62, 38, 15, 20), 0, 1)

        self.cursor_iter = self.cursor_iter + 1 if self.cursor_iter < 5 else 0
        text = font_small.render(self.text, True, (0,0,0))
        screen.blit(text, ((self.map[0] - self.dimensions[0]) / 2 + 5, 35))
        

    def update(self, screen):
        poop = open("overlay_data.txt", 'r').read()
        poop = poop.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
        poop2 = ast.literal_eval(poop)
        self.text = poop2["starting_message"][0:self.iter:1]
        self.iter += 1 if self.iter < len(poop2["starting_message"]) else 0
        print(self.iter)




class Dashboard():
    def __init__(self):
        pass



class Game():
    def __init__(self, data):
        map_width = data["screen_dimensions"][0] 
        map_height = 7/8 * data["screen_dimensions"][1]
        self.map_surface = pygame.Surface((map_width, map_height))
        self.rect = self.map_surface.get_rect()
        #self.dashboard = Dashboard((map_width, data["screen_dimensions"][1] / 8))
        self.text_overlay = Text_Overlay((map_width, map_height))
        self.text_overlay_showing = True

    def draw(self, screen):
        self.map_surface.fill((0,0,255))
        if self.text_overlay_showing:
            self.text_overlay.draw(self.map_surface)
        screen.blit(self.map_surface, self.rect)

    def loop(self, screen):
        self.draw(screen)
        self.text_overlay.update(screen)

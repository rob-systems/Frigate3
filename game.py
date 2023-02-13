import pygame, sys, math
from pygame.locals import *
from sprites import *
import ast

pygame.init()
font_small = pygame.font.SysFont("Verdana", 20)


# really basic way of showing text to the user
class Text_Overlay():
    def __init__(self, data):
        # iter means i can scroll through the text
        self.iter = 0
        # cursor needs an iter for flashing
        self.cursor_iter = 0
        self.map_dimensions = data["map"]
        self.text_to_be_displayed = data["text"]
        self.dimensions = (data["map"][0] * 11/12, data["map"][1] / 7)
        self.surface = pygame.Surface(self.dimensions)
        self.surface.fill((255,255,255))
        self.rect = self.surface.get_rect()
        #string will fill up with 
        self.text = ""

    def draw_cursor(self, surface):
        # adds flashing feature to the cursor in front of text
        if self.cursor_iter < 17:
            pygame.draw.rect(surface, (0,0,0), (self.iter * 10 + 27, 3, 15, 20), 0, 1)
        self.cursor_iter = self.cursor_iter + 1 if self.cursor_iter < 20 else 0

    def draw(self, screen):
        self.surface.fill((255,255,255))
        self.draw_cursor(self.surface)
        # renders self.text (which starts as an empty string and gradually is populated)
        text = font_small.render(self.text, True, (0,0,0))
        self.surface.blit(text, (3,0))
        screen.blit(self.surface, ((self.map_dimensions[0] - self.dimensions[0]) / 2, 35))

    def update(self, screen):
        # opens up dict file that will include all text prompts for user
        file = open("overlay_data.txt", 'r').read()
        # gets rid of quotations marks that python doesn't like
        file = file.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
        # changes format of file to a dict
        evaluated_file = ast.literal_eval(file)
        # get a substring of the text from file
        self.text = evaluated_file[self.text_to_be_displayed][0:self.iter:1]
        #increment iter so text gradually shows
        self.iter += 1 if self.iter < len(evaluated_file[self.text_to_be_displayed]) else 0


# going to show user health, reloading state, score
class Dashboard():
    def __init__(self, data):
        self.surface = pygame.Surface(data["dimensions"])
        self.position = data["position"]

    def draw(self, screen):
        self.surface.fill((150,150,150))
        screen.blit(self.surface, self.position)

class Game():
    def __init__(self, data):
        map_width = data["screen_dimensions"][0]
        map_height = 7/8 * data["screen_dimensions"][1]
        self.map_surface = pygame.Surface((map_width, map_height))
        self.rect = self.map_surface.get_rect()
        self.dashboard = Dashboard({ "dimensions": (map_width, data["screen_dimensions"][1] / 8),
                                     "position": (0, map_height)})
        self.text_overlay = Text_Overlay({ "map": (map_width, map_height), "text": "starting_message"})
        self.text_overlay_showing = True
        self.all_sprites = pygame.sprite.Group()
        self.User = Boat((200,200))
        self.all_sprites.add(self.User)


    def draw_sprites(self):
        for sprite in self.all_sprites:
            sprite.draw_hull(self.map_surface)

    def draw(self, screen):
        self.map_surface.fill((0,0,255))
        if self.text_overlay_showing:
            self.text_overlay.draw(self.map_surface)
        self.draw_sprites()
        screen.blit(self.map_surface, self.rect)
        self.dashboard.draw(screen)

    def update(self):
        for sprite in self.all_sprites:
            sprite.update()

    # called inside main loop
    def loop(self, screen):
        self.update()
        self.draw(screen)
        self.text_overlay.update(screen)

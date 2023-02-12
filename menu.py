import pygame
from pygame.locals import MOUSEBUTTONDOWN
from shapely.geometry import Point, Polygon

# need to repeeat this call because fonts don't work without it
pygame.init()

# FONTS
font = pygame.font.SysFont("Verdana", 60)
font_med = pygame.font.SysFont("Verdana", 30)

####################################################################
    #TO BE DISPLAYED BEFORE GAME STARTS
####################################################################

class Menu():
    def __init__(self):
        #List of menu items
        self.menu_items = [{ "text": "Play Game", "position": (200, 200)},
                           { "text": "High Scores", "position": (200, 250)}]
        self.selected = None

    def draw(self,screen):
        screen.fill((255,255,255))
        self.draw_title(screen)
        # loops over menu items list, creates a font var and blits it to the screen
        for i, item in enumerate(self.menu_items):
            # creates medium font object, black if menu item can be selected grey otherwise
            menu_item = font_med.render(item["text"], True, (0,0,0) if item["text"] == "Play Game" else (100,100,100))
            # adds font object to screen surface
            screen.blit(menu_item, (self.menu_items[i]["position"][0], self.menu_items[i]["position"][1]))

    def draw_title(self, screen):
        screen.blit(font.render("Frigate", True, (0,0,0)), (230, 120))

    def update(self, screen, mouse_pos):
        #below loops over menu items, creates a polygon, checks if mouse position is within polygon, if so draws line under selected menu item
        for i, item in enumerate(self.menu_items):
            # a box for each menu_item
            box = Polygon([item["position"],
                           (item["position"][0] + 200, item["position"][1]),
                           (item["position"][0] + 200, item["position"][1] + 35),
                           (item["position"][0], item["position"][1] + 35)])
            # need to create a point to be able to call Shapeley's within function
            mouse = Point(mouse_pos)
            if mouse.within(box):
                # only want to underline selectable items for the moment
                if i == 0:
                    pygame.draw.line(screen, (0,0,0), (item["position"][0], item["position"][1] + 35), (item["position"][0] + 200, item["position"][1] + 35), 3)
                    self.selected = self.menu_items[i]
            else:
                self.selected = None if self.selected == self.menu_items[i] else self.selected

    def select(self):
        # starts game if mouse position is within play game button box 
        play_game_pressed = False
        if self.selected != None:
            if self.selected["text"] == "Play Game":
                play_game_pressed = True
            else:
                play_game_pressed = False
        return play_game_pressed

    def loop(self, screen, mouse_pos):
        self.draw(screen)
        self.update(screen, mouse_pos)
        play_game_pressed = self.handle_mouse_click()
        return play_game_pressed

    def handle_mouse_click(self):
        play_game_pressed = False
        # basic mouse button event handling
        for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    play_game_pressed = self.select()
        return play_game_pressed

# Welcome to Frigate
import pygame, sys, math
from menu import Menu
from game import Game
from pygame.locals import *


#Allows pygame functions to be called
pygame.init()

# Declare Width and Height of Display
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600


# Loading screen to be displayed before game has been setup
class Loading():
    def __init__(self):
        self.iter = 0

    def iterate(self):
        if self.iter <= 360:
            self.iter += 1
        else:
            self.iter = 0

    def draw(self, screen):
        # rect object in center of screen
        rect = pygame.Rect(SCREEN_WIDTH / 2 - 25, SCREEN_HEIGHT / 2 - 25, 50, 50)
        # draws a diminishing arc starting at the top of the circle
        offset = math.radians(90)
        pygame.draw.arc(screen,
                        (255,255,255),
                        rect,
                        #start
                        0 + offset,
                        #stop
                        -math.radians(self.iter) + offset,
                        #width
                        5)
        # increase stop angle until it reaches FULL CIRCLE
        self.iterate()

def game_loading(displaysurf,loading):
    displaysurf.fill((0,0,0))
    loading.draw(displaysurf)
    return True



# Function handling Menu and Game
def main():
    # Create Display Surface
    displaysurf = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    play_game_pressed = False
    game_ready = False
    menu = Menu()
    loading = Loading()
    while True:
        ############ Quit Event Handling ###########
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        ############################################

        # loop through menu until play game has been clicked on
        if not play_game_pressed:
            play_game_pressed = menu.loop(displaysurf, pygame.mouse.get_pos())
        else:
            # show loading screen until game is ready
            if not game_ready:
                game = Game({"screen_dimensions": (SCREEN_WIDTH, SCREEN_HEIGHT)})
                game_ready = game_loading(displaysurf, loading)
            else:
               game.loop(displaysurf)
        
        # internally process pygame event handlers
        pygame.event.pump()
        # Update portions of the screen for software displays
        pygame.display.update()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()

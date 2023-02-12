# Welcome to Frigate
import pygame, sys, math
from menu import Menu
from pygame.locals import *


#Allows pygame functions to be called
pygame.init()

# Declare Width and Height of Display
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600


# Loading screen to be displayed before game has been setup
class Loading():
    def __init__(self):
        self.iter = 0

    def draw(self, screen):
        # rect object in center of screen
        rect = pygame.Rect(SCREEN_WIDTH / 2 - 25, SCREEN_HEIGHT / 2 - 25, 50, 50)
        # draws a diminishing arc starting at the top of the circle
        oofset = math.radians(90)
        pygame.draw.arc(screen, (255,255,255), rect, 0 + offset, -math.radians(self.iter) + offset, 5)
        # increase stop angle until it reaches FULL CIRCLE
        if self.iter <= 360:
            print(self.iter)
            self.iter += 1
        else:
            self.iter = 0


# Function handling Menu and Game
def main():
    # Create Display Surface
    displaysurf = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    play_game_pressed = False
    menu = Menu()
    loading = Loading()
    while True:
        ############ Quit Event Handling ###########
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        ############################################

        if not play_game_pressed:
            play_game_pressed = menu.loop(displaysurf, pygame.mouse.get_pos())
        else:
            game_ready = False
            if not game_ready:
                displaysurf.fill((0,0,0))
                loading.draw(displaysurf)
            else:
                
        
        # internally process pygame event handlers
        pygame.event.pump()
        # Update portions of the screen for software displays
        pygame.display.update()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()

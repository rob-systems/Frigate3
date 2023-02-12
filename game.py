# Welcome to Frigate
import pygame, sys
from menu import Menu
from pygame.locals import *


#Allows pygame functions to be called
pygame.init()

# Declare Width and Height of Display
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600


# Function handling Menu and Game
def main():
    # Create Display Surface
    displaysurf = pygame.display.set_mode((800, 600))
    play_game_pressed = False
    menu = Menu()
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
            displaysurf.fill((0,0,0))
        
        # internally process pygame event handlers
        pygame.event.pump()
        # Update portions of the screen for software displays
        pygame.display.update()

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()

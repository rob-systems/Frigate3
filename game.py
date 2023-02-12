import pygame, sys
from pygame.locals import *

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

displaysurf = pygame.display.set_mode((800, 600))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    
    pygame.event.pump()
    pygame.display.update()

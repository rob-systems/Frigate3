import pygame
from helper_functions import *
from shapely.geometry import Point, Polygon

pygame.init()



class Boat(pygame.sprite.Sprite):
    def __init__(self, data):
        super().__init__()
        self.hull = None
        self.create_hull(data)
        self.cur_turn = 0
        self.hull_poly_coords = []

    def create_hull(self, centre: (int,int)):
        boat_length, boat_width, stern_length = 50, 15, 13
        self.hull = Polygon([(centre[0] ,centre[1]-(boat_length / 2)),
                                 (centre[0] - (boat_width /2), centre[1] - (boat_length / 2) + stern_length),
                                 (centre[0] - (boat_width /2), centre[1] + (boat_length / 2)),
                                 (centre[0] + (boat_width /2), centre[1] + (boat_length / 2)),
                                 (centre[0] + (boat_width /2), centre[1] - (boat_length / 2) + stern_length)])

    def draw_hull(self, map_surface):
        pygame.draw.polygon(map_surface, (255, 255, 255), self.hull_poly_coords)

    def update(self):
        self.hull_poly_coords = rotate_polygon(self.hull, self.cur_turn)

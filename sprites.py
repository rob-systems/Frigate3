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
        # front is the pointy bit of the boat
        front = (centre[0] ,centre[1]-(boat_length / 2))
        front_left = (centre[0] - (boat_width /2),centre[1] - (boat_length / 2) + stern_length)
        back_left = (centre[0] - (boat_width /2), centre[1] + (boat_length / 2))
        back_right = (centre[0] + (boat_width /2), centre[1] + (boat_length / 2))
        front_right = (centre[0] + (boat_width /2), centre[1] - (boat_length / 2) + stern_length)
        self.hull = Polygon([front,front_left,back_left,back_right,front_right])

    def draw_hull(self, map_surface):
        pygame.draw.polygon(map_surface, (255, 255, 255), self.hull_poly_coords)

    def draw(self, map_surface):
        self.draw_hull(map_surface)

    def update(self):
        self.hull_poly_coords = rotate_polygon(self.hull, self.cur_turn)

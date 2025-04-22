import pygame as pg
import numpy as np
from settings import *

""""
    This draft retains the limitation of python being slow when rendering because of its dynamic type deduction of...
    its interpreter
"""

class Mode7:
    def __init__(self, app):
        self.app = app
        self.floor_texture = pg.image.load('resources/floor_0.png').convert()
        self.texture_size = self.floor_texture.get_size()
        self.floor_array = pg.surfarray.array3d(self.floor_texture)

        ##  Also a 3d array same size as screen resolution
        self.screen_array = pg.surfarray.array3d(pg.Surface(WIN_RES))
        ##  Makes screen yellow
        # self.screen_array[:] = (255, 255, 0)

    def update(self):
        self.screen_array = self.render_frame()

    def render_frame(self):
        #   Iterating over the screen array, over the x, y, and z coordinates to apply the mode7 theory
        for i in range(WIDTH):
            for j in range(HALF_HEIGHT, HEIGHT):
                #   x y z
                ##  A=the x-coordinate is adjusted so that the projected texture is at the screen's centre
                x=  HALF_WIDTH - i
                y = j + FOCAL_LENGTH
                z = j - HALF_HEIGHT + 0.01    ##  Small number prevents divide by zero error

                #   Projection
                px = x / z * SCALE
                py = y / z * SCALE

                ##  Define pixel position in texture
                #   First, define the floor pixel pos and color
                floor_pos = int(px % self.texture_size[0]), int(py % self.texture_size[1])
                floor_color = self.floor_array[floor_pos]

                #   Fill screen array
                self.screen_array[i, j] = floor_color


        return self.screen_array

    def draw(self):
        ##  Blitting the surfarray object on the screen
        pg.surfarray.blit_array(self.app.screen, self.screen_array)
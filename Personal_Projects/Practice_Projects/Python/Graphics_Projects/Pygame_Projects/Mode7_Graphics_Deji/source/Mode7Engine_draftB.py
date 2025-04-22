import pygame as pg
import numpy as np
from settings import *
from numba import njit, prange

"""
    This version gives the solution to the slow rendering by using numba
    It also adds the ceiling and shadow effect at the distance to remove the aliasing effect of far distance (z values)
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
        ##  Though the method is static, one still needs the self keyword. It is for every instance of the class
        self.screen_array = self.render_frame(self.floor_array, self.screen_array, self.texture_size)


    ##  Also, one cannot access the attributes and methods of the class inside this method.
    ##  A static method is like a regular function -- a non member function
    @staticmethod
    @njit(fastmath=True, parallel=True)
    def render_frame(floor_array, screen_array, texture_size):
        #   Iterating over the screen array, over the x, y, and z coordinates to apply the mode7 theory
        for i in prange(WIDTH):
            for j in prange(HALF_HEIGHT, HEIGHT):
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
                floor_pos = int(px % texture_size[0]), int(py % texture_size[1])
                floor_color = floor_array[floor_pos]

                ##  Shading is applied here to fix aliasing effect of distance
                attenuation = min(max(1.5 * (abs(z) / HALF_HEIGHT), 0), 1)

                floor_color = ( floor_color[0] * attenuation,
                                floor_color[1] * attenuation,
                                floor_color[2] * attenuation,)

                #   Fill screen array.
                ##  For floor
                screen_array[i, j] = floor_color
                ##  For ceiling, mirror the already calculated coordinates of the floor
                screen_array[i, -j] = floor_color


        return screen_array

    def draw(self):
        ##  Blitting the surfarray object on the screen
        pg.surfarray.blit_array(self.app.screen, self.screen_array)
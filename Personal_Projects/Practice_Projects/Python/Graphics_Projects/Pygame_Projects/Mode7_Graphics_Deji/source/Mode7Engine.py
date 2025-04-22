import pygame as pg
import numpy as np
from settings import *
from numba import njit, prange

"""
    This version adds controls and makes many changes to the render_frame method
"""

class Mode7:
    def __init__(self, app):
        self.app = app
        self.floor_texture = pg.image.load('resources/floor_1.png').convert()
        self.texture_size = self.floor_texture.get_size()
        self.floor_array = pg.surfarray.array3d(self.floor_texture)

        self.ceiling_texture = pg.image.load("resources/ceil_1.png").convert()
        ##  Scale this texture siz to be equal to the floor texture size to not need...
        ##  to create a new array to store the different sized texture values
        self.ceiling_texture = pg.transform.scale(self.ceiling_texture, self.texture_size)
        self.ceiling_array = pg.surfarray.array3d(self.ceiling_texture)

        ##  Also a 3d array same size as screen resolution
        self.screen_array = pg.surfarray.array3d(pg.Surface(WIN_RES))
        ##  Makes screen yellow
        # self.screen_array[:] = (255, 255, 0)
        ##  Alt stands for altitude
        self.alt = 1.0
        self.angle = 0.0
        self.pos = np.array([0.0, 0.0])

    def update(self):
        self.movement()
        ##  Though the method is static, one still needs the self keyword. It is for every instance of the class
        self.screen_array = self.render_frame(self.floor_array, self.ceiling_array, self.screen_array,
                                               self.texture_size, self.angle, self.pos, self.alt)

    def draw(self):
        ##  Blitting the surfarray object on the screen
        pg.surfarray.blit_array(self.app.screen, self.screen_array)

    ##  Also, one cannot access the attributes and methods of the class inside this method.
    ##  A static method is like a regular function -- a non member function
    @staticmethod
    @njit(fastmath=True, parallel=True)
    def render_frame(floor_array, ceiling_array, screen_array, texture_size, angle, player_pos, alt):

        sin, cos = np.sin(angle), np.cos(angle)

        #   Iterating over the screen array, over the x, y, and z coordinates to apply the mode7 theory
        for i in prange(WIDTH):
            new_alt = alt
            for j in prange(HALF_HEIGHT, HEIGHT):
                #   x y z
                ##  A=the x-coordinate is adjusted so that the projected texture is at the screen's centre
                x=  HALF_WIDTH - i
                y = j + FOCAL_LENGTH
                z = j - HALF_HEIGHT + new_alt    ##  Small number prevents divide by zero error

                #   2D rotation before the perspective division in the projection
                px = (x * cos - y * sin)
                py = (x * sin + y * cos)

                ##  Floor Projection and Transformation
                ##  The floor is not multiplied by alt like the ceiling is
                floor_x = px / z - player_pos[1]
                floor_y = py / z + player_pos[0]

                ##  Floor Pos and Color
                floor_pos = int(floor_x * SCALE % texture_size[0]), int(floor_y * SCALE % texture_size[1])
                floor_color = floor_array[floor_pos]


                ##  Ceiling Projection and Transformation
                ceiling_x = alt * px / z - player_pos[1] * 0.3
                ceiling_y = alt * py / z + player_pos[0] * 0.3

                ##  Ceiling Pos and COlor
                ceiling_pos = int(ceiling_x * SCALE % texture_size[0]), int(ceiling_y * SCALE % texture_size[1])
                ceiling_color = ceiling_array[ceiling_pos]


                ##  Shading is applied here to fix aliasing effect of distance
                depth = min(max(2.5 * (abs(z) / HALF_HEIGHT), 0), 1)
                fog = (1 - depth) * 230

                floor_color = ( floor_color[0] * depth + fog,
                                floor_color[1] * depth + fog,
                                floor_color[2] * depth + fog,)
                
                ceiling_color = ( ceiling_color[0] * depth + fog,
                                  ceiling_color[1] * depth + fog,
                                  ceiling_color[2] * depth + fog,)

                #   Fill screen array.
                ##  For floor
                screen_array[i, j] = floor_color
                ##  For ceiling, mirror the already calculated coordinates of the floor
                screen_array[i, -j] = ceiling_color

                #   Next depth
                new_alt += alt

        return screen_array

    def movement(self):
        sin_a = np.sin(self.angle)
        cos_a = np.cos(self.angle)
        dx, dy = 0, 0
        speed_sin = SPEED * sin_a
        speed_cos = SPEED * cos_a

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos
        self.pos[0] += dx
        self.pos[1] += dy

        if keys[pg.K_LEFT]:
            self.angle -= SPEED
        if keys[pg.K_RIGHT]:
            self.angle += SPEED

        if keys[pg.K_q]:
            self.alt += SPEED
        if keys[pg.K_e]:
            self.alt -= SPEED

        self.alt = min(max(self.alt, 0.3), 4.0)

    
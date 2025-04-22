import pygame as pg
from random import randint, randrange
from copy import deepcopy
import numpy as np
from numba import njit #    Just in time compiler :))

"""
   Added gliders

"""

RES = WIDTH, HEIGHT = 1200, 650
TILE = 2
W, H = WIDTH // TILE, HEIGHT // TILE
FPS = 10

pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()


next_field = np.array([[0 for i in range(W)] for j in range(H)])

current_field = np.array([[0 for i in range(W)] for j in range(H)])

def set_glider_SE(current_field, x, y):
    pos = [(x, y), (x + 1, y + 1), (x - 1, y + 2), (x, y + 2), (x + 1, y + 2)]
    for i, j in pos:
        current_field[j][i] = 1
    return current_field

def set_glider_NW(current_field, x, y):
    pos = [(x, y), (x - 2, y - 1), (x - 2, y), (x - 2, y + 1), (x - 1, y - 1)]
    for i, j in pos:
        current_field[j][i] = 1
    return current_field

for _ in range(500):
    i0, j0 = randrange(TILE, W // 2 + W // 4, TILE), randrange(TILE, H // 2)
    crrent_field = set_glider_SE(current_field, i0, j0)
    i1, j1 = randrange(W // 2- W // 4, W - TILE), randrange(H // 2, H - TILE)
    current_field =set_glider_NW(current_field, i1, j1)

def check_cell(current_field, x, y):
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if current_field[j][i]:
                count += 1
        
    if current_field[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0

@njit(fastmath=True)
def check_cell_njit(current_field, next_field):
    """
        The function checks all cells.

        It returns the generated next array as well as the list cells that need to be drawn.
        This is so because numba cannot work with instances of classes of non-standard libraries.
        In this case, the Pygame module
    """
    res = []
    for x in range(W):
        for y in range(H):
            count = 0
            for j in range(y - 1, y + 2):
                for i in range(x - 1, x + 2):
                    if current_field[j % H][i % W] == 1:    #   Also edited this
                        count += 1
            if current_field[y][x] == 1:
                count -= 1
                if count == 2 or count == 3:
                    next_field[y][x] = 1
                    res.append((x, y))
                else:
                    next_field[y][x] = 0
            else:
                if count == 3:
                    next_field[y][x] = 1
                    res.append((x, y))
                else:
                    next_field[y][x] = 0
    return next_field, res

while True:
    surface.fill(pg.Color('black'))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        

    #   Draw life
    next_field, res = check_cell_njit(current_field, next_field)
    [pg.draw.rect(surface, pg.Color("white"),
                    (x * TILE + 1, y * TILE + 1, TILE - 1, TILE - 1))
                    for x, y in res]
                    
    
    current_field = deepcopy(next_field)

    print(clock.get_fps())
    pg.display.flip()
    clock.tick(FPS)
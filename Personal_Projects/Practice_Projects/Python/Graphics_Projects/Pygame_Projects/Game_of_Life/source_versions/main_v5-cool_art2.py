import pygame as pg
from random import randint
from copy import deepcopy
import numpy as np
from numba import njit #    Just in time compiler :))

"""
    Added numba to increase the frame rate by almost 20 times.

    1.  Modified check_cell_njit -- this time, the full screen size is looped through
    2.  Filled the array with live cells in the form of square diagonals @#Latest


"""

RES = WIDTH, HEIGHT = 1200, 650
TILE = 2
W, H = WIDTH // TILE, HEIGHT // TILE
FPS = 10

pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()


next_field = np.array([[0 for i in range(W)] for j in range(H)])
#   first Style
# current_field = [[randint(0, 1) for i in range(W)] for j in range(H)]
#   Style 2
# current_field = [[1 if not i % 33 else 0 for i in range(W)] for j in range(H)]
#   Style 3
# current_field = [[1 if not (4 * i + j) % 4 else 0 for i in range(W)] for j in range(H)]
#   Style 4
# current_field = np.array([[1 if not (i * j) % 22 else 0 for i in range(W)] for j in range(H)])

#   Latest
current_field = np.array([[1 if i == W // 2 or j == H // 2 else 0 for i in range(W)] for j in range(H)])

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
""""
    This project imitates the matrix intro screen.
    The characters used for the intro screen are to those of the...
    Katakana symbols, which are really chinese symbols of some kind.

    This version shows the addition of several columns that move.
    However, they start at the same height
"""

import pygame as pg
import os
from random import choice, randrange

class Symbol:
    def __init__(self, x, y, speed):
        self.x, self.y = x, y
        self.speed = speed
        ##  the choice() method returns a random element from a non empty sequence...
        ##  It raises and IndexError if it is empty
        self.value = choice(green_katakana)
        self.interval = randrange(5, 30)
    
    def draw(self):
        frames = pg.time.get_ticks()
        ##  When the value of frames is a multiple of the time interval value...
        ##  change symbol displayed
        if not frames % self.interval:
            self.value = choice(green_katakana)
        self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE
        surface.blit(self.value, (self.x, self.y))

class SymbolColumn:
    def __init__(self, x, y):
        self.column_height = randrange(8, 18)
        self.speed = randrange(2, 6)
        ##  Makes a ,list of a symbols that make a column with one symbol on top...
        ##  of the other
        self.symbols = [Symbol(x, i, self.speed) for i in range(y, y - FONT_SIZE * self.column_height, -FONT_SIZE)]
    
    def draw(self):
        [symbol.draw() for symbol in self.symbols]



os.environ['SDL_VIDEO_CENTERED'] = '1'
RES = WIDTH, HEIGHT = 1200, 675
FONT_SIZE = 60
pg.init()
screen = pg.display.set_mode(RES)
surface = pg.Surface(RES)
clock = pg.time.Clock()


katakana = [chr(int('0x30a0', 16) + i) for i in range(96)]
FONT = pg.font.Font('font/MS Mincho.ttf', FONT_SIZE)

green_katakana = [FONT.render(str(char), True, pg.Color('green')) for char in katakana]
light_green_katakana = [FONT.render(str(char), True, pg.Color('lightgreen')) for char in katakana]


# symbol_column = SymbolColumn(WIDTH // 2 - FONT_SIZE // 2, HEIGHT // 2 - FONT_SIZE // 2)
symbol_columns = [SymbolColumn(x, 0) for x in range(0, WIDTH, FONT_SIZE)]

while True:
    screen.blit(surface, (0, 0))
    surface.fill(pg.Color('black'))

    [symbol_column.draw() for symbol_column in symbol_columns]

    [exit() for e in pg.event.get() if e.type == pg.QUIT]
    pg.display.flip()
    clock.tick(60)



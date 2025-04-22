""""
    This project imitates the matrix intro screen.
    The characters used for the intro screen are to those of the...
    Katakana symbols, which are really chinese symbols of some kind.

    This version adds a blur effect to the matrix character columns using...
    the alpha channels of the durface they are rendered on.
    In the tutorial, the screen was used as the main surface for rendering until this...
    feature was added.
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
    
    def draw(self, color):
        frames = pg.time.get_ticks()
        ##  When the value of frames is a multiple of the time interval value...
        ##  change symbol displayed
        if not frames % self.interval:
            self.value = choice(green_katakana if color == 'green' else lightgreen_katakana)
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
        ##  The green katakana symbols will be drawn if the symbol is not the first in the list...
        ##  The first one is to be displayed in lightgreen, so if i is not 0, then the green one, else, the light green one
        [symbol.draw('green') if i else symbol.draw('lightgreen') for i, symbol in enumerate(self.symbols)]



os.environ['SDL_VIDEO_CENTERED'] = '1'
RES = WIDTH, HEIGHT = 1200, 675
FONT_SIZE = 45
alpha_value = 120

pg.init()
screen = pg.display.set_mode(RES)
surface = pg.Surface(RES)
surface.set_alpha(alpha_value)
clock = pg.time.Clock()


katakana = [chr(int('0x30a0', 16) + i) for i in range(96)]
FONT = pg.font.Font('font/MS Mincho.ttf', FONT_SIZE)

##  Use the randrange to give a random number from range of values for the green channel only
green_katakana = [FONT.render(str(char), True, (0, randrange(160, 256), 0)) for char in katakana]
lightgreen_katakana = [FONT.render(str(char), True, pg.Color('lightgreen')) for char in katakana]

# symbol_column = SymbolColumn(WIDTH // 2 - FONT_SIZE // 2, HEIGHT // 2 - FONT_SIZE // 2)
##  Now random
symbol_columns = [SymbolColumn(x, randrange(-HEIGHT, 0)) for x in range(0, WIDTH, FONT_SIZE)]

while True:
    screen.blit(surface, (0, 0))
    surface.fill(pg.Color('black'))

    [symbol_column.draw() for symbol_column in symbol_columns]

    [exit() for e in pg.event.get() if e.type == pg.QUIT]
    pg.display.flip()
    clock.tick(60)



""""
    This project imitates the matrix intro screen.
    The characters used for the intro screen are to those of the...
    Katakana symbols, which are really chinese symbols of some kind.
    This version shows the implementation of the down movement of the characters
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



os.environ['SDL_VIDEO_CENTERED'] = '1'
RES = WIDTH, HEIGHT = 1200, 675
FONT_SIZE = 140
pg.init()
screen = pg.display.set_mode(RES)
surface = pg.Surface(RES)
clock = pg.time.Clock()


katakana = [chr(int('0x30a0', 16) + i) for i in range(96)]
FONT = pg.font.Font('font/MS Mincho.ttf', FONT_SIZE)

green_katakana = [FONT.render(str(char), True, pg.Color('green')) for char in katakana]

symbol = Symbol(WIDTH//2 - FONT_SIZE//2, HEIGHT//2-FONT_SIZE//2, speed=3)
# symbol_column = SymbolColumn(WIDTH // 2 - FONT_SIZE // 2, HEIGHT // 2 - FONT_SIZE // 2)

while True:
    screen.blit(surface, (0, 0))
    surface.fill(pg.Color('black'))

    symbol.draw()

    [exit() for e in pg.event.get() if e.type == pg.QUIT]
    pg.display.flip()
    clock.tick(60)



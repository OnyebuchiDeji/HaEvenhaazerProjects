""""
    This project imitates the matrix intro screen.
    The characters used for the intro screen are to those of the...
    Katakana symbols, which are really chinese symbols of some kind.

    This version just displays each character changing on the screen.
"""

import pygame as pg
import os
from random import choice, randrange

class Symbol:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.value = choice(green_katakana)
        self.interval = randrange(5, 30)
    
    def draw(self):
        frames = pg.time.get_ticks()
        if not frames % self.interval:
            self.value = choice(green_katakana)
        surface.blit(self.value, (self.x, self.y))


os.environ['SDL_VIDEO_CENTERED'] = '1'
RES = WIDTH, HEIGHT = 1200, 675
FONT_SIZE = 140

pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()


katakana = [chr(int('0x30a0', 16) + i) for i in range(96)]
font = pg.font.Font('font/MS Mincho.ttf', FONT_SIZE)
green_katakana = [font.render(char, True, pg.Color('green')) for char in katakana]

symbol = Symbol(WIDTH // 2 - FONT_SIZE // 2, HEIGHT // 2 - FONT_SIZE // 2)

while True:
    surface.fill(pg.Color('black'))

    symbol.draw()

    [exit() for e in pg.event.get() if e.type == pg.QUIT]
    pg.display.flip()
    clock.tick(60)



import os
import pygame as pg
import random as rndm
import sys


# os.environ['SDL_VIDEO_CENTERED'] = '1'
pg.init()
FONT_SIZE = 140
FONT = pg.font.Font('font/MS Mincho.ttf', FONT_SIZE)

class MatrixSymbol:
    def __init__(self, symbol, x, y, color: str):
        self.x, self.y = x, y
        self.symbol = symbol
        self.color = color

    def get_surface(self):
        ##  This returns the surface that has the rendered surface
        return FONT.render(self.symbol, True, pg.Color(self.color))
        
class MatrixSymbolColumn:
    def __init__(self, max_height):
        self.column_height = rndm.randrange(8, max_height)
        # self.


class App():
    def __init__(self):
        self.RES = self.WIDTH, self.HEIGHT = 1200, 675
        self.screen = pg.display.set_mode(self.RES)
        self.surface = pg.Surface(self.RES)
        self.clock = pg.time.Clock()
        self.symbols = [chr(int('0x30a0', 16) + i) for i in range(96)]
        self.font_x, self.font_y = self.WIDTH // 2-FONT_SIZE // 2, self.HEIGHT // 2 - FONT_SIZE // 2
        # self.font_surface = FONT.render(self.symbols[0], True, pg.Color('green'))
        self.matrix_symbols =  [MatrixSymbol(char, self.font_x, self.font_y, 'green') for char in self.symbols]

    def animate(self):
        # self.time = pg.time.get_ticks() * 0.01
        self.surface.blit(self.matrix_symbols[rndm.randrange(0, 95)].get_surface(), (self.matrix_symbols[0].x, self.matrix_symbols[0].y))
        pg.display.flip()
        pg.time.delay(250)


    def display(self):
        self.screen.blit(self.surface, (0, 0))
        self.surface.fill(pg.Color('black'))
        self.animate()

        
    
    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type==pg.KEYDOWN and e.key == pg.ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.display()
            self.clock.tick(60)




def main():
    for i in range(96):
        symbol = chr(int('0x30a0', 16) + i)
        print(symbol, end=' ')


if __name__ == "__main__":
    app = App()
    app.run()
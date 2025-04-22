import pygame as pg

pg.init()

RES = WIDTH, HEIGHT = 1200, 675
screen = pg.display.set_mode(RES)
surface = pg.Surface(RES)
FONT_SIZE = 140
FONT = pg.font.Font('font/MS Mincho.ttf', FONT_SIZE)
CLOCK = pg.time.Clock()
def main():
    symbols = []
    for i in range(96):
        symbol = chr(int('0x30a0', 16) + i)
        symbols.append(symbol)
        print(symbol, end=' ')
    while True:
        [exit() for e in pg.event.get() if e.type==pg.QUIT]
        screen.blit(surface, (0, 0))
        surface.fill('red')
        font = FONT.render(str(symbols[0]), True, pg.Color('blue'))
        surface.blit(font, (WIDTH//2 - FONT_SIZE//2, HEIGHT //2 + FONT_SIZE//2))
        pg.display.flip()
        CLOCK.tick(60)





if __name__ == "__main__":
    main()
import pygame as pg
import cv2
import sys
from settings import WIN_RES
from Mode7Engine import Mode7


class App:
    def __init__(self):
        self.screen = pg.display.set_mode(WIN_RES)
        self.clock = pg.time.Clock()
        self.mode7 = Mode7(self)
    
    def update(self):
        self.mode7.update()
        self.clock.tick()
        pg.display.set_caption(f'{self.clock.get_fps(): .1f}')
    
    def draw(self):
        self.mode7.draw()
        pg.display.flip()
    
    def update_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update_time()
            self.update()
            self.draw()
    
if __name__ =='__main__':
    app = App()
    app.run()

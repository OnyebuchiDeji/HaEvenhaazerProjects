import sys
import pygame as pg

from depracated_source.Boid_v2 import *
from Math_Structures import *

"""
    Created: Tue-30-Jan-2024

    The flocking simulation of alignment, cohesion, and separation.
    Just as birds fly in a flock
"""

class Engine:
    def __init__(self):
        self.resolution = self.screen_width, self.screen_height = 1200, 675
        self.screen = pg.display.set_mode(self.resolution)
        self.fps = 60
        self.clock = pg.time.Clock()

        self.flock: list[Boid] = []
        self.on_init()
    
    def on_init(self):
            # self.flock.append(Boid(self.screen, Vec2(self.width / 2, self.height / 2)))
        for num in range(100):
            self.flock.append(Boid(self.screen, Vec2(rnd.randrange(0, self.screen_width), rnd.randrange(0, self.screen_height))))


    def update_display(self):
        self.screen.fill('black')
        for boid in self.flock:
            boid.edge_detection(self.screen_width, self.screen_height)
            boid.flock(self.flock)
            boid.draw()
            boid.update()
        pg.display.flip()
    
    def listen_for_exit(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.type == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
    
    def run(self):
        while True:
            self.update_display()
            self.listen_for_exit()
            self.clock.tick(self.fps)


if __name__== "__main__":
    Engine().run()
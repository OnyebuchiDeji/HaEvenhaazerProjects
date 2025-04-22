from Core.ForwardKinematics_Deji import *
import pygame as pg
import sys


class Engine:
    def __init__(self):
        self.resolution = self.width, self.height = 1040, 585
        self.screen = pg.display.set_mode(self.resolution)
        self.fps = 60
        self.clock = pg.time.Clock()

        ##  Forward Kinematics
        # self.kinematicsApp1 = ForwardKinematics(self)
        self.kinematicsApp2 = ForwardKinematics(self)

    # def update(self):
    #     pg.display.flip()

    def display(self):
        self.screen.fill('darkslategray')
        self.kinematicsApp2.display()
        pg.display.flip()


    def listen_for_exit(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.display()
            self.listen_for_exit()
            self.clock.tick(self.fps)



if __name__ == "__main__":
    myApp = Engine()
    myApp.run()
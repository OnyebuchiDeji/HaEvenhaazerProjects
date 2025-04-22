import pygame as pg
from Object3D import *
from Camera import *
from Projection import *

class SoftwareRenderer:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1200, 675
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.create_objectsS2()

    # def create_objectsS1(self):
    #     self.camera = Camera(self, [0.5, 1, -4])
    #     self.projection = Projection(self)
    #     self.object = Object3D(self)
    #     self.object.translate([0.2, 0.4, 0.2])
    #
    #     self.axes = Axes(self)
    #     self.axes.translate([0.7, 0.9, 0.7])
    #     self.world_axes = Axes(self)
    #     self.world_axes.movement_flag = False
    #     self.world_axes.scale(2.5)
    #     self.world_axes.translate([0.0001, 0.0001, 0.0001])

    def create_objectsS2(self):
        self.camera = Camera(self, [-5, 5, -50])
        self.projection = Projection(self)
        self.object = self.get_object_from_file('resources/13216_Deinonychus_NEW.obj')

    def get_object_from_file(self, filename):
        vertices, faces = [], []
        with open(filename) as f:
            for line in f:
                if line.startswith('v '):
                    ##  One is added to the coordinates of the vrtices to convert them to...
                    ##  homogenous coordinates
                    vertices.append([float(i) for i in line.split()[1:]] + [1])
                elif line.startswith('f'):
                    ##  The numbering of faces starts from one...
                    faces_ = line.split()[1:]
                    ##  So subtract 1 from its number because it is being added to a list
                    faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
        return Object3D(self, vertices, faces)

    def draw(self):
        self.screen.fill(pg.Color('darkslategray'))
        self.object.draw()
        # self.world_axes.draw()
        # self.axes.draw()


    def run(self):
        while True:
            self.draw()
            self.camera.control()   ##  Adding the camera control in the main program loop
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)

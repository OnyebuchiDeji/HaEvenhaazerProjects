import pygame as pg
import moderngl as mgl
import sys

##from Model2D import *
from Model3D_og import *
from Camera import Camera
from Light import Light
from Mesh import Mesh
from Scene import Scene


class GraphicsEngine:
    def __init__(self, win_size = (1200, 675)):
        #   init pygame modules
        pg.init()
        #   window_size
        self.WIN_SIZE = win_size
        #   set opengl attr
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        #   create opengl context
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        #   Mouse Settings
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)
        #   Detect and use current opengl context
        self.ctx = mgl.create_context()
        ##  Clockwise
        # self.ctx.front_face = 'cw'
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)
        #   Create an object to help track time
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0
        #   Light:
        self.light = Light()
        #   Camera
        self.camera = Camera(self)
        #   Mesh
        self.mesh = Mesh(self)
        #   Scene
        self.scene = Scene(self)


    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.mesh.destroy()
                pg.quit()
                sys.exit()

    def render(self):
        #   Clear frame buffer
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        #   Render scene
        self.scene.render()
        #   Swap buffers
        pg.display.flip()

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.render()
            self.delta_time = self.clock.tick(60)

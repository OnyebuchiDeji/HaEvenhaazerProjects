import pygame as pg
import numpy as np
import moderngl as mgl


import taichi as ti
import taichi_glsl as tgl
from taichi_glsl import vec2, vec3

ti.init(arch=ti.cuda)  # ti.cpu ti.gpu ti.vulkan ti.opengl ti.metal(macOS)

RES = WIDTH, HEIGHT = 1280, 720

# load texture
texture = pg.image.load('img/rust.jpg')  # texture res - 2^n x 2^n (512 x 512, 1024 x 1024, ...)
texture_size = texture.get_size()[0]
# texture color normalization  0 - 255 --> 0.0 - 1.0
texture_array = pg.surfarray.array3d(texture).astype(np.float32) / 255





class PyShader:
    def __init__(self, app):
        self.app = app
        self.screen_array = np.full((WIDTH, HEIGHT, 3), [0, 0, 0], np.uint8)
        #   taichi fields   --  the data structures of taichi
        #   These data structures are stored and processed in the video memory of the graphics chips...
        self.screen_field = ti.Vector.field(3, ti.uint8, (WIDTH, HEIGHT))

        
    @ti.kernel
    def render(self, time: ti.float32):
        """fragment shader imitation"""
        ##  WHile iterating over the screen field
        for frag_coord in ti.grouped(self.screen_field):
            #   get normalized pixel coordinates
            uv = frag_coord / RES

            # Get colour and  invert the y-axis to fit the opengl coordinate system
            col = 0.5 + 0.5 * tgl.cos(time + tgl.vec3(uv.x, uv.y, uv.x) + tgl.vec3(0.0, 2.0, 4.0))

            #   Bring the color to the RGB format by multiplying the color by 255
            self.screen_field[frag_coord.x, RES.y - frag_coord.y] = col * 255

    
    def update(self):
        time = pg.time.get_ticks() * 1e-03
        self.render(time)
        self.screen_array = self.screen_field.to_numpy()
    
    def draw(self):
        pg.surfarray.blit_array(self.app.screen, self.screen_array)
    
    def run(self):
        self.update()
        self.draw()






class App:
    def __init__(self):
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.shader = PyShader(self)


    def run(self):
        while True:
            self.shader.run()
            pg.display.flip()

            [exit() for e in pg.event.get() if e.type == pg.QUIT]
            self.clock.tick(60)
            pg.display.set_caption(f'FPS: {self.clock.get_fps() : .2f}')


if __name__ == '__main__':
    app = App()
    app.run()
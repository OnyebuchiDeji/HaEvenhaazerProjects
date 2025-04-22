import pygame as pg
import moderngl as mgl
import numpy as np
from PIL import Image
import cv2
import sys
import struct

"""
    This is the complete app. It implements just saving a frame.
"""

class Engine:
    def __init__(self, app):
       self.app_ref = app
       self.ctx = mgl.create_context()
       self.shader_program = self.create_program()
       self.surface_vertices = [
           (-1, -1), (1, -1), (1, 1), (-1, 1)
       ]
       self.surface_indices = [
           (0, 1, 2), (0, 2, 3)
       ]
       self.vbo = self.get_vbo()
       self.vao = self.get_vao()
       
       self.set_uniform('u_resolution', self.app_ref.RES)


    def render(self):
        self.ctx.clear(1.0, 0.0, 0.0, 0.0)
        self.update_time()
        self.vao.render(mgl.TRIANGLES)


    def update_time(self):
        self.set_uniform('u_time', pg.time.get_ticks() * 0.001)
    
    def set_uniform(self, u_name, u_value):
        try:
            self.shader_program[u_name] = u_value
        except KeyError:
            pass

    def destroy(self):
        self.vbo.release()
        self.shader_program.release()
        self.vao.release()

    def load_shader(self, file_path):
        with open(file_path) as f:
            return f.read()
    
    def create_program(self):
        ##  The Shader Program
        program = self.ctx.program(
            vertex_shader=self.load_shader("source/shaders/vertex_shader.glsl"),
            fragment_shader=self.load_shader("source/shaders/fragment_shader.glsl")
            # varyings=["fragColor"]
        )
        return program
    
    def order_data(self, vertices, indices):
        data = [vertices[index] for triangle in indices for index in triangle]
        return np.array(data, dtype='f4')
    
    def get_vbo(self):
        vertices_data = self.order_data(self.surface_vertices, self.surface_indices)

        vbo = self.ctx.buffer(vertices_data)
        return vbo
    
    def get_vao(self):
        vao = self.ctx.vertex_array(self.shader_program, [(self.vbo, '2f',
                                    *['vertexPosition'])])
        return vao


class App:
    def __init__(self, win_size = (1200, 675)):
        self.RES = self.WIDTH, self.HEIGHT = win_size
        self.screen = pg.display.set_mode(self.RES, flags=pg.OPENGL | pg.DOUBLEBUF)
        self.shader_engine = Engine(self)
        self.clock = pg.time.Clock()


    def save_frame(self):
        ##  This accessed the moderngl context screen data, reading RGBA components in 8 bit integer datatype form...
        ##  that is, 0-255 for RGB
        raw = self.shader_engine.ctx.screen.read(components=4, dtype='f1')
        ##  With the use of numpy, this takes the buffer data and reshapes it so that it the color is read according to...
        ##  how the resolution is, that is, it is a 2d array, with the height as the first dimension and the...
        ##  width as the second, which is how it is meant to be... that is what self.RES[1::-1] does.
        ##  *self.RES[1::-1]. The * is to unpack the tuple, to return its data individually...
        ##  The [1::-1] makes the returned tuple to be reflected...
        ##  so since self.RES = (WIDTH, HEIGHT), self.RES[1::-1] will return HEIGHT, WIDTH...
        ##  and * returns HEIGHT and WIDTH individually
        image_data = np.frombuffer(raw, dtype='uint8').reshape(
            ((*self.RES[1::-1], 4))
        )
        ##  The array represents contains pixel's color starting from the top left to the bottom right
        print(image_data)
        ##  Give to cvt to change it to its format that it can work with and convert it to savable color format...
        ##  Also openCV is very...
        ##  Compatible with numpy and as you can see can receive a numpy array well
        image_data = cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)
        ##  Writes out the png file :)
        cv2.imwrite("output/fractal3.png", image_data)
        print("Saved!")


    def display(self):
        self.shader_engine.render()
    
    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                self.destroy()
                pg.quit()
                sys.exit()
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_s:
                    self.save_frame()

    def run(self):
        while True:
            self.display()
            self.check_events()
            self.clock.tick(0)
            pg.display.flip()

if __name__ == '__main__':
    app = App()
    app.run()

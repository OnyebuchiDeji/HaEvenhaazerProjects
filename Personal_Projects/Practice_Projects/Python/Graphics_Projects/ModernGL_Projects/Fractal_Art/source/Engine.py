import pygame as pg
import moderngl as mgl
import numpy as np
import cv2
import sys

"""
    This was the OG file that just rendered the fractal things. Didn't implement saving.
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
        self.update_time()
        self.ctx.clear()
        self.vao.render()

    def update_time(self):
        self.set_uniform('u_time', pg.time.get_ticks()*0.001)
    
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


    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                self.shader_engine.destroy()
                pg.quit()
                sys.exit()

    def display(self):
        self.shader_engine.render()

    def run(self):
        while True:
            pg.display.flip()
            self.check_events()
            self.display()
            self.clock.tick(0)

if __name__ == '__main__':
    app = App()
    app.run()

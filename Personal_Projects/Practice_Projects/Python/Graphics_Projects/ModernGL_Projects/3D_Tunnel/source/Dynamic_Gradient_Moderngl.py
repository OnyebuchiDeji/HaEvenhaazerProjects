import pygame as pg
import numpy as np
import moderngl as mgl
import sys


RESOLUTION = WIDTH, HEIGHT = (1200, 675)


class PyGlShader:
    def __init__(self):
        self.ctx = mgl.create_context()
        self.shader_program = self.create_program()
        self.surface_vertices = [
            (-1, -1), (1, -1), (1, 1), (-1, 1), (-1, -1), (1, 1)
            ]
        self.vbo = self.get_vbo()
        self.vao = self.get_vao()

        #______________________#
        self.set_uniform('u_resolution', RESOLUTION)
        
        #______________________#
    
    def update_time(self):
        self.set_uniform('u_time', pg.time.get_ticks() * 0.001)

    def render(self):
        self.update_time()
        self.ctx.clear()
        self.vao.render()

    def destroy(self):
        self.vbo.release()
        self.shader_program.release()
        self.vao.release()

    ####_______________________________________####    
    def set_uniform(self, u_name, u_value):
        try:
            self.shader_program[u_name] = u_value
        except KeyError:
            pass


    ####_______________________________________#### 


    def load_shader(self, file_path):
        with open(file_path) as f:
            return f.read()
        
    
    def create_program(self):
        ##  The SHader Program
        program = self.ctx.program(
            vertex_shader=self.load_shader("source/shaders/vertex_shader.glsl"),
            fragment_shader=self.load_shader("source/shaders/fragment_shader.glsl")
        )

        return program
    
    def get_vertex_data(self):
        return np.array(self.surface_vertices, dtype='f4')
    
    #   Vertex Buffer Object
    def get_vbo(self):
        self.vertex_data = self.get_vertex_data()
        #   The vertex buffer object:
        vbo = self.ctx.buffer(self.vertex_data)
        return vbo
    
    def get_vao(self):
        vao = self.ctx.vertex_array(self.shader_program, [(self.vbo, '2f', 'in_position')])
        return vao



    


class App:
    def __init__(self):
        self.screen = pg.display.set_mode(RESOLUTION, flags=pg.OPENGL | pg.DOUBLEBUF)
        self.shader_app = PyGlShader()
        self.clock =  pg.time.Clock()


    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                self.shader_app.destroy()
                pg.quit()
                sys.exit()

    def render(self):
        self.shader_app.render()

    def run(self):
        while True:
            pg.display.flip()
            self.check_events()
            self.render()
            self.clock.tick(0)

        
if __name__=='__main__':
    app = App()
    app.run()
            
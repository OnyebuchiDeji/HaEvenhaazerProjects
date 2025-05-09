import pygame as pg
import moderngl as mgl
import struct
import sys

class App:
    def __init__(self, win_size = (1360, 765)):
        #   opengl_context
        pg.display.set_mode(win_size, flags=pg.OPENGL | pg.DOUBLEBUF | pg.FULLSCREEN)
        self.ctx = mgl.create_context()

        #   time objects
        self.clock = pg.time.Clock()

        #   load shaders
        with open('shaders/vertex_shader.glsl') as f:
            vertex = f.read()
        with open('shaders/fragment_shader.glsl') as f:
            fragment = f.read()
        self.program = self.ctx.program(vertex_shader=vertex, fragment_shader=fragment)

        #   quad screen vertices
        #   The vertices for two triangles for the screen's plane
        vertices = [(-1, -1), (1, -1), (1, 1), (-1, 1), (-1, -1), (1, 1)]

        #   quad vbo
        vertex_data = struct.pack(f'{len(vertices) * len(vertices[0])}f', *sum(vertices, ()))
        self.vbo = self.ctx.buffer(vertex_data)
 
        #   quad vao
        self.vao = self.ctx.vertex_array(self.program, [(self.vbo, '2f', 'in_position')])

        #uniforms
        self.set_uniform('u_resolution', win_size)

    def render(self):
        #   The context is like the screen
        self.ctx.clear()
        self.vao.render()
        pg.display.flip()

    def update(self):
        self.set_uniform('u_time', pg.time.get_ticks() * 0.001)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.render()
            self.clock.tick(0)
    
    def set_uniform(self, u_name, u_value):
        try:
            self.program[u_name] = u_value
        except KeyError:
            pass

    def destroy(self):
        self.vbo.release()
        self.program.release()
        self.vao.release()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.destroy()
                pg.quit()
                sys.exit()


if __name__ == '__main__':
    app = App()
    app.run()
        
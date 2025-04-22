import pygame as pg
import moderngl as mgl
import numpy as np
from PIL import Image
import cv2
import sys
import struct

"""
    This is the complete app. It implements recording the fractal image renddered by moderngl.
    It has the implementation and explanation of how to save a frame.
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


        ##  To Record Screen as Video:
        self.rec_fps = 25
        self.record_start = False
        self.first_frame = 0
        self.recorder_obj = cv2.VideoWriter("output/fractal_vid3.mp4",
                                             cv2.VideoWriter_fourcc(*"mp4v"),
                                             self.rec_fps, self.RES)
        self.record_start = True

    def get_frame(self):
        raw = self.shader_engine.ctx.screen.read(components=4, dtype='f1')
        image_data = np.frombuffer(raw, dtype='uint8').reshape(
            ((*self.RES[1::-1], 4))
        )
        image_data = cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)
        return image_data

    def array_equality(arr1, arr2):
        ##  If not the same size, then no way are they equal
        if (arr1.size != arr2.size):
            False
        ##  Sort them
        arr1.sort()
        arr2.sort()
        ##  Check if their contents, match one by one
        for i in range(0, arr2.size):
            if (arr1[i] != arr2[i]):
                return False
        return True
        
    def record(self):
        """
        This algorithm is to make sure that if the current frame...
        is the same as the first frame that was saved...
        then it means it has looped, so stop.
        """
        if self.record_start:
            frame = self.get_frame()
            if type(self.first_frame) is int:
                self.first_frame = frame
            else:
                if (frame == self.first_frame).all():
                    self.record_start = False
                    cv2.destroyAllWindows()

            self.recorder_obj.write(frame)
            cv2.imshow('Frame', frame)



    def save_frame(self):
        raw = self.shader_engine.ctx.screen.read(components=4, dtype='f1')
        image_data = np.frombuffer(raw, dtype='uint8').reshape(
            ((*self.RES[1::-1], 4))
        )
        image_data = cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)
        cv2.imwrite("output/fractal2.png", image_data)
        print("Saved!")




    def display(self):
        self.shader_engine.render()
        
        self.record()

    
    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                self.destroy()
                pg.quit()
                sys.exit()
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_s:
                    self.save_frame()
                # if e.key == pg.K_r:
                #     self.record_start = not self.record_start

    def run(self):
        while True:
            self.display()
            self.check_events()
            self.clock.tick(0)
            pg.display.flip()

if __name__ == '__main__':
    app = App()
    app.run()

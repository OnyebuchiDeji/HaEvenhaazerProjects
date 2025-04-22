import pygame as pg
import moderngl as mgl
import numpy as np
from PIL import Image
import cv2
import sys

"""This draft is like draftB. In draftB I explain every issue.
    In this draft, I tried to use the PIL library to save the gl render as an image.
    But the issue is that I was trying to read from the framebuffer. It's not how it's meant to be.
    The frame buffer is only used when you add a texture, for example, via pygame.
    The methods to convert the read image into a gl texture, along with other methods are provided.
    Even the .use(index) method too is provided. Check other projects like the 3d engine one.
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
       self.fbo = self.ctx.framebuffer(
            color_attachments=[self.ctx.texture(
                self.app_ref.RES, components=4, dtype='f1'
            )]
        )



    # def get_fbo(self):
    #     frameBufferObject = self.ctx.framebuffer(
    #        color_attachments=[self.ctx.texture(self.app_ref.RES, components=3, dtype='f1')]
    #        )
    #     return frameBufferObject

    def render(self):
        self.update_time()
        self.ctx.clear()
        self.vao.render()


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


        ##  To Record Screen GIF:
        # self.recorder_obj = cv2.VideoWriter("output/fractal_vid1.gif", cv2.VideoWriter_fourcc(*"gi"))

    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                self.shader_engine.destroy()
                pg.quit()
                sys.exit()
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_s:
                    self.save_frame()

    def save_frame(self):

        raw_img_data= self.shader_engine.fbo.read(attachment=0, components=3, dtype='f1')
        # print(raw_img_buffer)
        # np_image_buffer = np.frombuffer(raw_img_buffer, dtype=np.uint8).reshape(
        #     (*currentFBO.size[1::-1], 3))
        # np_image_arr = np.array(np_image_buffer) *255
        # print("\n", np_image_arr)

        # pygame_image = pg.surfarray.array3d(self.frameBufferObject.read(components=1))
        # cv2_img = cv2.transpose(raw_img_buffer)
        image = Image.frombytes('RGB', self.shader_engine.fbo.size, raw_img_data)
        # cv2_img = cv2.cvtColor(np_image_arr, cv2.COLOR_BGR2RGB)
        # cv2.imwrite("output/fract1.jpg", cv2_img)
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
        image.save('output/fract1.png')
        print("Image Saved!")

    def record(self):
        pass

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

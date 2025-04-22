import sys
import pygame as pg
import moderngl
from array import array
import numpy as np
import cv2

from PIL import Image


"""
    Tutorial from DaFluffyPotato

    Tue-29-Nov-2023
    Changes:
    Successfully Implemented the Save Function!
    This one uses the PILLOW, python image library

    In this tutorial, I was able to turn a pygame surface into a texture I put on moderngl.
    Something about it affected the way the
"""




class App:
    def __init__(self):
        pg.init()
        self.RES = self.width, self.height = (800, 600)
        ##  .flip() flips the double buffers being used
        self.screen = pg.display.set_mode(self.RES, pg.OPENGL | pg.DOUBLEBUF)
        self.display_surface = pg.Surface(self.RES)
        self.clock = pg.time.Clock()

        self.ctx = moderngl.create_context()
        self.shader_program = self.create_program()

        self.image = pg.image.load("resources/car2.jpg")
        self.fps = 60
        
        """ 
          NOTE how I did not specify the indices for the order of how the triangles will be drawn!
          This is because, in the display() method, where the render_object is used...
          Notice how on render, a constant is passed in as a parameter:
          self.render_object.render(mode=moderngl.TRIANGLE_STRIP)
          This sorts out the order, not requiring me to add my own indices, like how CoderSpace does his in my...
          other projects I adapted from his.
        """
        self.quad_buffer = self.ctx.buffer(data=array(
            'f', [
                #   position (x, y), uv coords (x, y)
                -1.0, 1.0, 0.0, 0.0,    #   Top Left
                1.0, 1.0, 1.0, 0.0,     #   Top Right
                -1.0, -1.0, 0.0, 1.0,   #   Bottom Left
                1.0, - 1.0, 1.0, 1.0,   #   Bottom Right
            ]
        ))

        """
            Note how vertexPosition defers from texturePosition. VertexPosition id for the rendering surface by x and y...
            whereas texturePosition is the s and v values that determine the top, left, right, and down percentages that the...
            texture takes up in the VertexPosition surface 
        """
        self.render_object = self.ctx.vertex_array(self.shader_program, 
                                                   [(self.quad_buffer, '2f 2f',
                                                     'vertexPosition', 'texturePosition')])
        
        
        
        self.shader_program['textureSampler'] = 0

    def surf_to_texture(self, surface):
        """ takes pygame surface and returns an opengl texture
        """
        tex = self.ctx.texture(surface.get_size(), 4)
        tex.filter = (moderngl.NEAREST, moderngl.NEAREST)
        ##  Defines how the channels are mapped to each other because...
        ##  pygame uses a different color order than opengl so it...
        ##  puts it in the format for opengl
        tex.swizzle = 'BGRA'
        ##  This surface.get_view() generates the raw data for the surface...
        ##  It gives a lower level output for the surface. The one specifies what...
        ##  the format should be
        tex.write(surface.get_view('1'))
        return tex

    def load_shader(self, file_path):
        with open(file_path) as f:
            return f.read()
        
    def create_program(self):
        program = self.ctx.program(
            vertex_shader = self.load_shader("source/vertex_shader.glsl"),
            fragment_shader = self.load_shader("source/fragment_shader.glsl")
        )
        return program



    def display(self):
        self.display_surface.fill('black')
        self.display_surface.blit(self.image, pg.mouse.get_pos())

        ##  Setting texture uniform
        ##  Writing to the texture uniform in fragment shader the value 0
        self.frame_texture = self.surf_to_texture(self.display_surface)
        self.frame_texture.use(0)
        self.shader_program['utime'] = self.update_time()
        ##  This code makes the need of specifying indices for the triangle not needed!
        self.render_object.render(mode=moderngl.TRIANGLE_STRIP)

        self.check_events()
        pg.display.flip()
        self.frame_texture.release()
        self.clock.tick(self.fps)


    def update_time(self):
        return pg.time.get_ticks() * 0.001

    def release_gl_memory(self):
        self.quad_buffer.release()
        self.render_object.release()

        self.shader_program.release()

    #--------NOT RIGHT---------#
    # def save1(self, name):
    #     data = self.frame_texture.read()
    #     image = Image.frombytes('RGBA', self.frame_texture.size, data)
    #     # image = image.transpose()
    #     # image = image.convert
    #     image.save(f'output/{name}.png')
    #     print(f"picture {name} saved!")
    #___________________________#
    def save_frame1(self, name):
        data = self.ctx.screen.read(components=4, dtype='f1')
        image = Image.frombytes('RGBA', self.frame_texture.size, data)
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
        # image = image.convert()
        image.save(f'output/{name}.png')
        print(f"picture {name} saved!")

    def save_frame2(self, name):
        ##  This was implemented on Wed-3-Jan-2024 by the Father's Grace
        raw = self.ctx.screen.read(components=4, dtype='f1')
        ##  This creates a 2d array that reads every pixel row by row with as
        ##  many rows as the height is.
        ##  This is the reason for *self.RES[1::-1], as normally the resolution is...
        ##  (WIDTH, HEIGHT) but the code refelcts it and returns HEIGHT, WIDTH...
        ##  to make the 2D array of pixels' colors with dimensions: [HEIGHT, WIDTH]
        image_data = np.frombuffer(raw, dtype='uint8').reshape(
            ((*self.RES[1::-1], 4))
        )
        ##  Printing the image data will show you what I mean
        print(image_data)

        image_data = cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)
        """
            This change was made on 06-01-2024 to use this second way of saving the image with opencv...
            rather than PIL.
            Changed this:
            # transposed_image =cv2.transpose(image_data)
            To this:
                flipped_image =cv2.flip(image_data, 0)
            For reasons, cv2.transpose() was not working
        """
        # flipped_image =cv2.flip(image_data, 0)
        flipped_image =cv2.transpose(image_data, cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite(f'output/{name}.png', flipped_image)
        print(f"Image {name} has been saved!")
    
    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.release_gl_memory()
                pg.quit()
                sys.exit()
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_s:
                    self.save_frame2("carGL2Trnsps90Clw-06012024")


    def run(self):
        while True:
            self.display()



if __name__ == "__main__":
    myApp = App()
    myApp.run()
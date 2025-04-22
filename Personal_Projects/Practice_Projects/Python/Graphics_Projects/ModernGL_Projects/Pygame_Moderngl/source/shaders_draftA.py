import sys
import pygame as pg
import moderngl
import array


"""
    Tutorial from DaFluffyPotato
"""




class App:
    def __init__(self):
        pg.init()
        self.RES = self.width, self.height = (800, 600)
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()

        self.ctx = moderngl.create_context()
        self.shader_program = self.create_program()

        self.image = pg.image.load("resources/car.jpg")
        self.fps = 60
        
        self.quad_buffer = self.ctx.buffer(data=array(
            'f', [
                #   position (x, y), uv coords (x, y)
                -1.0, 1.0, 0.0, 0.0,    #   Top Left
                1.0, 1.0, 1.0, 0.0,     #   Top Right
                -1.0, -1.0, 0.0, 1.0,   #   Bottom Left
                1.0, - 1.0, 1.0, 0.0,   #   Bottom Right
            ]
        ))

        self.render_object = self.ctx.vertex_array(self.shader_program, 
                                                   [(self.quad_buffer, '2f 2f',
                                                     'vertexPosition', 'texturePosition')])


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
            vertex_shader = self.load_shader("vertex_shader.glsl"),
            fragment_shader = self.load_shader("fragment_shader.glsl")
        )
        return program



    def display(self):
        self.screen.fill('black')
        self.screen.blit(self.image, pg.mouse.get_pos())

        pg.display.flip()
        self.clock.tick(self.fps)

    def run(self):
        while True:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            self.display()







if __name__ == "__main__":
    myApp = App()
    myApp.run()
import pygame as pg
from OpenGL.GL import *
import numpy as np
import ctypes
import sys
from OpenGL.GL.shaders import compileProgram, compileShader

##  Read contents of each file as string and then compile into shader modules...
##  Then link them together and compile them together into a program which is...
##  loaded into the graphics card and then it works
""" 
    Date: Tuesday-10-Oct-2023, week 3 of resumption, Keele
    
    In Part2B, continuation form 2A, transparency was enabled for the transparent cat png picture.
    Part2B shows the implementation of code that enables opengl to add transparenct to what is rendered.

    Even after doing Change1, the transparency was not working in the rendering
    But after Change2, it worked.
    Though, both code are needed because if...
    glEnable(GL_BLEND) and setting the blend funciton, glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)...
    are not used, though the transparency of the image will show, the triangle will no longer have the colour on it
"""

class Triangle:

    def __init__(self):
        # #   x, y, z, r, g, b
        # self.vertices = (
        #     -0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
        #     0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
        #     0.0, 0.5, 00.0, 0.0, 0.0, 1.0
        # )

       ##  for s and t, for the first two points, s=0, t=1, for bottom left of triangle
       ##   for s=1, t=1, it is the bottom right of triangle
       #3   for s=0.5, t=0, its the top, but s is at the center

        #   x, y, z, r, g, b, s, t
        self.vertices = (
            -0.5, -0.5, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0,
            0.5, -0.5, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0,
            0.0, 0.5, 0.0, 0.0, 0.0, 1.0, 0.5, 0.0
        )

        self.vertex_data = np.array(self.vertices, dtype=np.float32)

        self.vertex_count = 3


        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertex_data.nbytes, self.vertex_data, GL_STATIC_DRAW)
        
        ##  Attribute 0
        glEnableVertexAttribArray(0)
        #   1st arg: attribute 0 is for position
        #   2nd arg: points in each attributes, 3 for xyz and rgb
        #   3rd arg: datatype: floating points
        #   4th arg: will opengl need to do work to normalize numbers FALSE because we have made sure nothing...
        ##  is outside the accpetable range
        #   5th: stride: number of bytes to next vertex. Each vertex has 8 numbers now of 4 bytes...
        ##  so stride is 32 bytes
        #   6th: offset: where does the data begin for the first point? position starts at front -- offset: 0
        ##  the first colour starts 3 numbers into buffer: offset 3*4 = 12 bytes
        ##  Likewise, the texture coordinates start 6 float numbers into the buffer, 6 * 4 = 24
        ##  the ctypes.c_void() is used because the function expects a void pointer, a special type of memory address...
        ##  so ctypes need to be used
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(0))
        #   Attribute index 1 for colour
        glEnableVertexAttribArray(1) 
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(12))
        #   Attribute index 2 for for texture coordinate
        glEnableVertexAttribArray(2) 
        #   since just s and t, the 2nd para is 2, for texture coordinates
        glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(24))
        
    def destroy(self):
        ##  The functions need a tuple, so a losing comma is used to make it look like a list or tuple
        glDeleteVertexArrays(1, (self.vao,))
        glDeleteBuffers(1, (self.vbo,))



class Material:

    def __init__(self, filepath):
        self.texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        ##  Texture coordinates in opengl are addressed with s, t coordinate pairs
        ##  each betwen zero and one
        ##  the top of the texutre is t=0, and the bottom, t=1
        ##  The left side is s=0, and the rightmost is s=1
        ##  2nd parameter is setting the address mode for s, t.
        ##  3rd para: What is the wrapping mode? What should happen when the texture is past s=1 or t=1...
        ##  one can do: clamp-to-edge, which causes the image to not be rendered pat a certain point.
        ##  But here, texture_wrap is chosen for both s and t to cause opengle to repeat the texture...
        ##  it repeats the image again.
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        ##-
        #   Minimizing and magnifying filter... it scales the texture by shrinking or enlarging...
        #   so the option for minimizing, using GL_NEAREST,  just shrinks it in a rough way, but is okay
        #   when magnifying, linear filtering is chosen to be used for smooth sampling
        # -##
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        ##  Load image in device-friendly pixel format.
        ###################-----CHANGE2------#######################
        #   CHANGE 2, use convert_alpha() instead of convert(), because...
        #   convert does not reflect the transparency of transparent objects
        ##image = pg.image.load(filepath).convert()
        image = pg.image.load(filepath).convert_alpha()
        #################################################
        ##  Get image's width and height
        image_width, image_height = image.get_rect().size
        ##  opengl does not unserstand pygame's image format...
        ##  so the image format is changed to a single large string, and specifying only RGBA channels gives that information
        image_data = pg.image.tostring(image, "RGBA")
        #-
        #   glTexImage2D sends the image data in 
        #   1st arg: texture location uplading to
        #   2nd arg: mipmap levels being loaded to = 0
        #   Mipmaps: progressively downsampling images to a series of smaller images...
        #   when a camera is nearer tot hte texrture, becaus eof mipmaps, a lower resolution texture is loaded...
        #   this reduces oversampling, to make the image nicer and more performant on the graphics card
        #   3rd: specify the format the image data would be stored in
        #   4th & #th: widht, height.
        #   6th : border... but because no border is used, it is zero.
        #   7th: format of data: RGBA channels
        #   8th: data format for each channel,0-255
        #   9th: actual image data
        # -#
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image_width, image_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)
        #3  Generates mipmap
        glGenerateMipmap(GL_TEXTURE_2D)

    def use(self):
        ##  Select the active texture. It is useful because opengl allows us to load...
        ##  more than one texture at a time. This is useful for batch rendering...
        ##  layering textures ontop of each other, on the same surface, or if one is to pass in other textures...
        ##  storing other data like light maps and gloss maps or height maps.
        ##  GL_TEXTURE0 is texture unit 0
        glActiveTexture(GL_TEXTURE0)
        ##  Bind the texture to location zero
        glBindTexture(GL_TEXTURE_2D, self.texture)

    def destroy(self):
        glDeleteTextures(1, (self.texture,))



class App:

    def __init__(self):
        #initialize pypy
        ##  Returns an integer that indicates the number of initialized modules
        pg.init()
        self.resolution = self.width, self.height = (1200, 675)
        pg.display.set_mode(self.resolution, pg.OPENGL | pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        ###################-----CHANGE2------#######################
        glEnable(GL_BLEND)
        ##  This is the standard function for alpha blending
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        ##################################
        self.shader_program = self.create_shader("source/shaders/vertex_shader.txt", "source/shaders/fragment_shader.txt")
        ##  Better to have a shader currently in use before making a mesh object, because the mesh object accesses or...
        ##  enables attributes like attribute 0 or 1, and it might not make sense unless the shader has been used...
        ##  and it knows there are attributes.
        glUseProgram(self.shader_program)
        ###################################
        ##  The below sets one integer parameter value to the uniform location and passing 0 to the sampler...
        ##  this indicates that texture index 0 is being sampled
        ##  it makes the sampler ready for this line where the texture at index 0 is made active...
        ##  in the use() method in the Material class glActiveTexture(GL_TEXTURE0)... t
        ##  This sets the uniform, imageTexture that is used as the sampler2D for the texture
        glUniform1i(glGetUniformLocation(self.shader_program, "imageTexture"), 0)
        ##################################
        self.triangle = Triangle()
        # self.wood_texture = Material("resources/wood.jpeg")
        self.current_texure = Material("resources/cat.png")

    def create_shader(self, vertexFilePath, fragmentFilePath):
        ##  The as keyword localises the lifetime of the resource; it automatically closes the file...
        ##  after the indneted block ends, which is why the read stream can be reused without closing explicitely.
        with open(vertexFilePath, 'r') as f:
            vertex_src = f.readlines()
        with open(fragmentFilePath, 'r') as f:
            fragment_src = f.readlines()
        
        shader = compileProgram(
            ##  2nd parameter to indicate type of shader being compiled
            compileShader(vertex_src, GL_VERTEX_SHADER),
            compileShader(fragment_src, GL_FRAGMENT_SHADER)
        )

        return shader

    def display(self):
        #   Refresh Screen
        glClear(GL_COLOR_BUFFER_BIT)
        #   initialize opengl
        glClearColor(0.1, 0.2, 0.2, 1) #    RGBA

        ##  Set shader to be used again
        glUseProgram(self.shader_program)

        self.current_texure.use()

        ##  Bind triangle vao, to get it ready as the current module to be drawn
        glBindVertexArray(self.triangle.vao)
        
        ##  OpenGl looks inside the above bound vao and takes the data
        #args:
        #   arg1: draw mode. Could be GL_LINES, GL_POINTS, and more
        #   arg2: starting point, vertex index 0
        #   arg3: vertex count, number of vertices
        glDrawArrays(GL_TRIANGLES, 0, self.triangle.vertex_count)


    def check_events(self):
        for e in pg.event.get():
            if (e.type == pg.QUIT) or (e.type==pg.KEYDOWN and e.key==pg.K_ESCAPE):
                self.free_memory()
                pg.quit()
                sys.exit()
    
    def free_memory(self):
        self.triangle.destroy()
        glDeleteProgram(self.shader_program)
        self.current_texure.destroy()

    def main_loop(self):

        while True:
            #   Check events
            self.check_events()
            self.display()
            pg.display.flip()   ##  Flip Buffers

            #   Timing
            self.clock.tick(60)

    


if __name__ == '__main__':
    myApp = App()
    myApp.main_loop()

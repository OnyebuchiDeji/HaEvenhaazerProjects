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
    The part1 of the opengl learning by GetIntoGameDev on Youtube.
    Date: Tuesday-3-ct-2023 week 2 of resumption, Keele

    This part includes the first and second video of the opengl in python...
    These were done:
    1.  Setting up pygame, the structure of the App class, and opengl, including clearing the screen;
    1A. Created the shader by parsing and compiling before using it
    2.  Making the Triangle class, specifying the vertices, making the vertex buffer and vertex array objects...
        and giving them the same ids, which was 1.
    4.  Then, still in the Triangle class, the vao was bound, making opengl know which vao to use...
        and the vertex buffer was bound likewise.
    5.  Sending the data to the vao:
        using glBufferData(GL_ARRAY_BUFFER, self.vertex_data.nbytes, self.vertex_data, GL_STATIC_DRAW)    
        gives the data to the vao via the function, where the data is stored in an ordered format...
        that opengl understands, ready to draw.
    6.  Specifying the order of the data:
            The data being used has vertices as in points, rgb values, and, in part2, texture values.
            using glEnableVetexAttribArray enables opengl to know the partitioning of the data.

            i) glEnableVertexAttribArray(index) specifies the index that identifies each vertex group in the...
            vbo that is bound to the vao.

            ii) glVertexAttribPointer(  index, num_of_values, GL_FLOAT(data type), GL_FALSE(to normalize),
              total_size_of_vertex_data, ctypes.c_void_p(0)(stride from position 0 of this data)    ) 
            glVertexAttribPointer() specifies what index each specific block of data belongs to...
            1. it takes the index
            2. how many values that data has (for example, vertices and rgb use 3 values, while...
            textures use 2)
            3. The data type (float)
            4. whether to normalize the data
            5. the size of the vertex data...
            6. the stride: where the particular data starts from the start of the buffer
            It uses all these to make pointers to the start of each data, represeted by the index...
            this data can now be input into the vertex shader, to define variables and the indexes are used to assign...
            the variables to the right data block. 

    7.  When the program is quit, memory of the Triangle, asn the shader_program is freed

"""

class Triangle:

    def __init__(self):
        #   x, y, z, r, g, b
        self.vertices = (
            -0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
            0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
            0.0, 0.5, 00.0, 0.0, 0.0, 1.0
        )

        self.vertex_data = np.array(self.vertices, dtype=np.float32)

        self.vertex_count = 3


        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        ## gives the data to opengl to give it to the vao, where the data is stored in an ordered format...
        ##  that opengl understands, ready to draw.
        glBufferData(GL_ARRAY_BUFFER, self.vertex_data.nbytes, self.vertex_data, GL_STATIC_DRAW)
        
        ##  The below enables opengl to know the partitioning of the data.
        ##  glEnableVertexAttribArray(index) specifies the index that identifies each vertex group in the...
        ##  vbo that is bound to the vao.
        glEnableVertexAttribArray(0)
        #   1st arg: attribute 0 is for position
        #   2nd arg: points in each attributes, 3 for xyz and rgb
        #   3rd arg: datatype: floating points
        #   4th arg: will opengl need to do work to normalize numbers FALSE because we have made sure nothing...
        ##  is outside the accpetable range
        #   5th: stride: number of bytes to next position. Each vertex has 6  numbers of 4 bytes...
        ##  so stride is 24 bytes
        #   6th: offset: where does the data begin for the first point? position starts at front -- offset: 0
        ##  the first colour starts 3 numbers into buffer: offset 3*4 = 12 bytes
        ##  the ctypes.c_void() is used because the function expects a void pointer, a special type of memory address...
        ##  so ctypes need to be used
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))

        #   1st arg: attribute 1 is for colour
        glEnableVertexAttribArray(1) 
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
        
    def destroy(self):
        ##  The functions need a tuple, so a losing comma is used to make it look like a list or tuple
        glDeleteVertexArrays(1, (self.vao,))
        glDeleteBuffers(1, (self.vbo,))



class App:

    def __init__(self):
        #initialize pypy
        ##  Returns an integer that indicates the number of initialized modules
        pg.init()
        self.resolution = self.width, self.height = (1200, 675)
        pg.display.set_mode(self.resolution, pg.OPENGL | pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        self.shader_program = self.create_shader("source/shaders/vertex_shader.txt", "source/shaders/fragment_shader.txt")
        ##  Better to have a shader currently in use before making a mesh object, because the mesh object accesses or...
        ##  enables attributes like attribute 0 or 1, and it might not make sense unless the shader has been used...
        ##  and it knows there are attributes.
        glUseProgram(self.shader_program)
        self.triangle = Triangle()
        

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

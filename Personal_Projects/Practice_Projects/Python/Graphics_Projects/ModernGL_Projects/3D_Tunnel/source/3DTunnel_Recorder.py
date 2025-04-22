import pygame as pg

import numpy as np
import moderngl as mgl
import sys
import cv2

""""
    This project was made by me, but got a lot of reference from CoderSpace...
    Tunnel-Shader-Imitation.
    He did his using pygame and taichi, but taichi was not working for me. So I used ModernGl

    Note how the rendered circular images have a small line through the side center.
    It has to do with the code in the fragment_shader.


    The recorder was added Mon-08-01-2024, so the videos in the output were at this time.
    The center line has not yet been fixed!

"""

RESOLUTION = WIDTH, HEIGHT = (1200, 675)

# class VAO:
#     def __init__(self, shader_app):
#         self.ctx = shader_app.ctx
#         self.shader_program = shader_app.shader_program
#         self.vbo_container = VBO(shader_app.ctx)
#         self.vao_dictionary = {}


#     def add_vao(self, vao_name, vbo_name):
#         self.vao_dictionary[vao_name] = self.get_vao(
#             program=self.shader_program, vbo=self.vbo_container[vbo_name]
#         )
    
#     def get_vao(self, program, vbo):
#         vao = self.ctx.vertex_array(program, [(
#             self.vbo.
#         )])

# class VBO:
#     def __init__(self, shader_app):
#         self.ctx = shader_app.ctx
#         self.vbo_dictionary = {}

#     def add_vbo(self, vbo_name, vertices):
#         vertex_data = self.get_vertex_data()
#         self.vbo_dictionary[vbo_name] = self.get_vbo(self, vertex_data)
    
#     #   Vertex Buffer Object
#     def get_vbo(self, vertex_data):
#         #   The vertex buffer object:
#         vbo = self.ctx.buffer(vertex_data)
#         return vbo
    
#     def get_vertex_data(self, vertices):
#         np.array(vertices, dtype='f4')

#     def release_vbos(self):
#         [vbo.release() for vbo in self.vbo_dictionarys.values()]


class Textures:
    def __init__(self, shader_app):
        self.ctx = shader_app.ctx
        self.textures = {}
        self.texture_size = {}

    def add_texture(self, tx_name, tx_path):
        # get_texture code:
        texture = pg.image.load(tx_path).convert()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=False)
        # texture = pg.transform.rotate(texture, 90)
        self.texture_size[tx_name] = texture.get_size()

        texture = self.ctx.texture(size=self.texture_size[tx_name], components=3,
                                   data=pg.image.tostring(texture, 'RGB'))
        
        texture.filter = (mgl.LINEAR_MIPMAP_LINEAR, mgl.LINEAR)
        texture.build_mipmaps()
        texture.anisotropy = 32.0
        self.textures[tx_name] = texture

    def destroy(self):
        [tex.release() for tex in self.textures.values()]
        

class PyGlShader:
    def __init__(self):
        self.ctx = mgl.create_context()
        self.shader_program = self.create_program()
        ##  Moderngl renders things using triangles.
        ##  So my vertices are for the points that make the triangles and indices shows the order of the points...
        #3  To form the trianlges
        self.surface_vertices = [
            (-1, -1), (1, -1), (1, 1), (-1, 1)
            ]
        ##  Follows an anticlockwise manner. The order of the indices tuples in the array doesn't matter
        ##  But it has to be the same with the texture indices. That is, in the way it goes from...
        ##  bottom left to bottom right to top right, and for the second triangle...
        ##  bottom left to top right to top left.
        ##  Apart from that, self.surface_indices and texture_indices can be:
        ##  [(0, 1, 2), (0, 2, 3)] or [(0, 2, 3), (0, 1, 2)] But both can only be one of either
        self.surface_indices = [(0, 1, 2), (0, 2, 3)]
        self.texture_vertices = [
            (0, 1), (1, 1), (1, 0), (0, 0)
        ]
        self.texture_indices = [
            (0, 1, 2), (0, 2, 3)
        ]
        self.vbo = self.get_vbo()
        self.vao = self.get_vao()

        self.texture_manager = Textures(self)

        #______________________#
        self.set_uniform('u_resolution', RESOLUTION)
        self.texture_init("beast_pic", "resources/beast_pic.jpg")
        print(self.texture_manager.texture_size["beast_pic"])
        self.set_uniform('u_texture_size', 
                            self.texture_manager.texture_size["beast_pic"])
        #______________________#
    


    def texture_init(self, textureName: str, path: str):
        self.texture_manager.add_texture(textureName, path)
        self.image_texture = self.texture_manager.textures[textureName]
        self.shader_program["u_image_texture"] = 0
        self.image_texture.use(location = 0)


    def update_time(self):
        self.set_uniform('u_time', pg.time.get_ticks() * 0.001)

    def render(self):
        self.update_time()
        self.image_texture.use(location = 0)
        self.ctx.clear()
        self.vao.render()
        # self.texture_vao.render()

    def destroy(self):
        self.vbo.release()
        self.shader_program.release()
        self.vao.release()
        self.texture_manager.destroy()
        

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
    
    def order_data(self, vertices, indices):
        """"This method returns the data in an ordered format representing the order in which the ...
        triangles that make up the vertexPos and texturePosition are to be drawn
        """
        data = [vertices[index] for triangle in indices for index in triangle]
        return np.array(data, dtype='f4')

    
    #   Vertex Buffer Object
    def get_vbo(self):
        vertices_data = self.order_data(self.surface_vertices, self.surface_indices)
        texture_vertices_data = self.order_data(self.texture_vertices, self.texture_indices)

        vertex_data = np.hstack([vertices_data, texture_vertices_data])
        #   The vertex buffer object:
        vbo = self.ctx.buffer(vertex_data)
        return vbo

    
    def get_vao(self):
        vao = self.ctx.vertex_array(self.shader_program, [(self.vbo, '2f 2f', *['vertexPosition', 'texturePosition'])])
        return vao
    



    


class App:
    def __init__(self):
        self.screen = pg.display.set_mode(RESOLUTION, flags=pg.OPENGL | pg.DOUBLEBUF)
        self.shader_app = PyGlShader()
        self.clock =  pg.time.Clock()

        ##  The Recorder
        self.rec_fps = 25
        self.first_time = 0
        self.record_start = True
        self.recorder_obj = cv2.VideoWriter("output/TunnlFixedLine.mp4",
                                            cv2.VideoWriter_fourcc(*"mp4v"),
                                            self.rec_fps, RESOLUTION)
    
    def record(self):
        """
        NOTE The mistake I made here. Because of this the video was not saving.
        This is because everytime I call this method, the self.recorder_obj is reinitialized!
        I put it so I can assign a name anytime I want it to be made, but there is no need since every new video...
        I have to record, I still have to change that name
        SOL: Remove it from the method
        self.recorder_obj = cv2.VideoWriter(f"output/{video_name}.mp4",
                                            cv2.VideoWriter_fourcc(*"mp4v"),
                                            self.rec_fps, RESOLUTION)
        """
        if self.record_start:
            frame = self.get_frame()

            self.recorder_obj.write(frame)
            cv2.imshow("Frame", frame)
            """
                if cv2.waitKey(1) & 0xFF == 27:
                the 0xFF==27 is to stop the video after only when the escape key is pressed.
                Just doing if cv2.waitKey(1) makes the recording stop immediately.
                This is the case of the RustTunnel_Vid1
            """
            ##  The escape key
            if cv2.waitKey(1) & 0xFF == 27:
                self.record_start = not self.record_start
                cv2.destroyAllWindows()
                print("Video Saved!")

    def get_frame(self):
        raw = self.shader_app.ctx.screen.read(components=4, dtype='f1')
        image_data = np.frombuffer(raw, dtype='uint8').reshape(
            ((*RESOLUTION[1::-1], 4))
        )
        image_data = cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)
        return cv2.flip(image_data, 0)

    def save_frame(self, image_name:str):
        raw = self.shader_app.ctx.screen.read(components=4, dtype='f1')
        image_data = np.frombuffer(raw, dtype='uint8').reshape(
            ((*RESOLUTION[1::-1], 4))
        )
        image_data = cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)
        cv2.imwrite(f"output/{image_name}.png", image_data)
        print(f"{image_name} has been saved!")
    


    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                self.shader_app.destroy()
                pg.quit()
                sys.exit()
            if e.type == pg.KEYDOWN and e.key == pg.K_s:
                self.save_frame("Rust_Tunnel_1")

    def render(self):
        self.shader_app.render()

    def run(self):
        while True:
            pg.display.flip()
            self.check_events()
            self.render()
            self.record()
            self.clock.tick(0)

        
if __name__=='__main__':
    app = App()
    app.run()
            
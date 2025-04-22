import moderngl as mgl
import numpy as np
import glm


class BaseModel:
    def __init__(self, app, vao_name, tex_id, model_path="", has_material=True, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        self.app = app
        self.pos = pos
        self.rot = glm.vec3([glm.radians(a) for a in rot])
        self.scale = scale
        self.m_model = self.get_model_matrix()
        self.tex_id = tex_id
        # self.model_init(vao_name, model_path, has_material)
        self.vao = app.mesh.vao.vaos[vao_name]
        self.program = self.vao.program
        self.camera = self.app.camera

    """
        Comment Date: Sun-14-01-2024
        This part of the code is to automate the creating of the vbo and vao for a model, to make it ready to be...
        rendered automatically when the Model is constructed in the Scene class
    """
    # def model_init(self, model_name, model_path, has_material):
    #     if not(model_name in self.app.mesh.vao.vaos):
    #         self.app.mesh.vao.vbo.addVbo(model_name, model_path, has_material)
    #         self.app.mesh.vao.addVao(model_name)


    def get_model_matrix(self):
        m_model = glm.mat4()
        #   Translate
        m_model = glm.translate(m_model, self.pos)
        #   Rotate
        m_model = glm.rotate(m_model, self.rot.x, glm.vec3(0, 0, 1))
        m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, self.rot.z, glm.vec3(1, 0, 0))
        #   Scale
        m_model = glm.scale(m_model, self.scale)

        return m_model

    def render(self):
        self.update()
        self.vao.render()

class Cube(BaseModel):
    def __init__(self, app, vao_name='cube', tex_id=0, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        self.texture.use()
        self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)

    def on_init(self):
        #   Texuture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_0'] = 0
        self.texture.use()
        #   Model View Projection Matrices
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)
        #   Light
        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)

class Cat(BaseModel):
    def __init__(self, app, vao_name='cat', tex_id='cat', pos=(0, 0, 0), rot=(-90, 20, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        self.texture.use()
        self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)

    def on_init(self):
        #   Texuture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_0'] = 0
        self.texture.use()
        #   Model View Projection Matrices
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)
        #   Light
        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)

class Model(BaseModel):
    def __init__(self, app, vao_name, tex_id,model_path, has_material=True, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, model_path, has_material, pos, rot, scale)
        self.on_init()

    def update(self):
        if self.app.mesh.texture.exists(self.tex_id):
            self.texture.use()
        self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)

    def on_init(self):
        #   Texture
        if self.app.mesh.texture.exists(self.tex_id):
            self.texture = self.app.mesh.texture.textures[self.tex_id]
            self.program['u_texture_0'] = 0
            self.texture.use()
        #   Model View Projection Matrices
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)
        #   Light
        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)




        
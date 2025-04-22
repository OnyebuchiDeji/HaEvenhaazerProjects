from VertexBufferObj import VBO
from Shader_program import ShaderProgram


class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}
        self.addVao('cube')
        # self.addVao('cat')
        self.addVao('ptero')
        #self.addVao('bary')

        # #   Cube VAO
        # self.vaos['cube'] = self.get_vao(
        #     program=self.program.programs['default'],
        #     vbo=self.vbo.vbos['cube']
        # )
        #
        # self.vaos['cat'] = self.get_vao(
        #     program=self.program.programs['default'],
        #     vbo=self.vbo.vbos['cat']
        # )

    def addVao(self, model_name):
        self.vaos[model_name] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos[model_name]
        )

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)])
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()
import numpy as np
import moderngl as mgl
import pywavefront as pwf

class VBO:
    def __init__(self, ctx):
        self.vbos = {}
        # self.ctx = ctx
        self.vbos['cube'] = CubeVBO(ctx)
        # self.vbos['cat'] = CatVBO(ctx)
        self.vbos['ptero'] = ModelVBO(ctx, model_path="Models/Pterodactylus/13625_Pterodactylus_v1_L1.obj")
        ##self.CatModel = CatVBO(ctx)
        ##self.addVBO(self.CatModel, 'cat')
        # self.ptero = ModelVBO(self.ctx, model_path="Models/Pterodactylus/13625_Pterodactylus_v1_L1.obj")
        # self.addVBO(self.ptero, 'ptero')

        #self.deino = ModelVBO_tOBJ(ctx, model_path="Models/Deinonychus/13216_Deinonychus_NEW.obj")
        #self.addVBO(self.deino, 'deino')
        #self.bary = ModelVBO(self.ctx, model_path="Models/16372_Baryonyx_v1_NEW.obj", has_material=False)
        #self.addVBO(self.bary, 'bary')
        # self.addVbo('ptero', model_path="Models/Pterodactylus/13625_Pterodactylus_v1_L1.obj")
        # self.addVbo('deino', model_path="Models/Deinonychus/13216_Deinonychus_NEW.obj")

    def addVbo(self, model_name, model_path, has_material):
        """
            Comment Date: Sun-14-01-2024
            As you can see, Pypy has switch statement. It is called Switch Case.
        # """
        # match model_name:
        #     case "cube":
        #         self.vbos[model_name] = CubeVBO(self.ctx)
        #     case "cat":
        #         self.vbos[model_name] = CatVBO(self.ctx)
        #     case _:
        #         self.vbos[model_name] = ModelVBO(self.ctx, model_path, has_material) 
        if model_name == "cube":
            self.vbos[model_name] = CubeVBO(self.ctx)
        elif model_name == "cat":
            self.vbos[model_name] = CatVBO(self.ctx)
        else:
            self.vbos[model_name] = ModelVBO(self.ctx, model_path, has_material) 

    def destroy(self):
        [vbo.destroy() for vbo in self.vbos.values()]



class BaseVBO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = self.get_vbo()
        self.format: str = None
        self.attribs: list = None

    def get_vertex_data(self): ...

    def get_vbo(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        return vbo

    def destroy(self):
        self.vbo.release()


class CubeVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')

    def get_vertex_data(self):
        ##  Cube's points' coordinates
        vertices = [(-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1),
                    (-1, 1, -1), (-1, -1, -1), (1, -1, -1), (1, 1, -1)]
        ##  Numbering the vertices from the front face of a cube in an anti-clockwise manner...
        ##  The vertices are numbered in 3s, forming right-angled triangles
        indices = [(0, 2, 3), (0, 1, 2),
                   (1, 7, 2), (1, 6, 7),
                   (6, 5, 4), (4, 7, 6),
                   (3, 4, 5), (3, 5, 0),
                   (3, 7, 4), (3, 2, 7),
                   (0, 6, 1), (0, 5, 6)]

        vertex_data = self.get_data(vertices, indices)
        #   Texture coordinates
        tex_coord_vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
        ##  All 12 triangles from which the cube model formed
        tex_coord_indices = [(0, 2, 3), (0, 1, 2),
                             (0, 2, 3), (0, 1, 2),
                             (0, 1, 2), (2, 3, 0),
                             (2, 3, 0), (2, 0, 1),
                             (0, 2, 3), (0, 1, 2),
                             (3, 1, 2), (3, 0, 1)]
        tex_coord_data = self.get_data(tex_coord_vertices, tex_coord_indices)

        ##  Because cubes have 6 faces, they have 6 normals:
        #   Because each face has 3 triangles, each triangle has 3 vertices
        #   so for every 6 vertices there is the same normal
        normals = [(0, 0, 1) * 6,
                   (1, 0, 0) * 6,
                   (0, 0, -1) * 6,
                   (-1, 0, 0) * 6,
                   (0, 1, 0) * 6,
                   (0, -1, 0) * 6]
        normals = np.array(normals, dtype='f4').reshape(36, 3)

        vertex_data = np.hstack([normals, vertex_data])
        ##  Combine vertex and texture coordinate data
        vertex_data = np.hstack([tex_coord_data, vertex_data])
        return vertex_data

class CatVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pwf.Wavefront('Models/Cat/20430_Cat_v1_NEW.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data

class ModelVBO(BaseVBO):
    def __init__(self, app, model_path, has_material=True):
        self.model_path = model_path
        self.create_materials = not has_material
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']



    def get_vertex_data(self):
        objs = pwf.Wavefront(self.model_path, create_materials=self.create_materials, collect_faces=True, parse=True, cache=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data


"""
    Comment Date: 14-01-2024
    This was me trying to tinker my way to make the Deinonychus model to display without adding any texture. But it just didn't work.
    So I settled with it using the texture of the pterodactyl model.
    Generally, pywavefront caches this by making a JSON file of the model's directory and uses the previous model's texture...
    for a model that doesn't have its own texture.
"""
# class ModelVBO_tOBJ(BaseVBO):
#     def __init__(self, app, model_path):
#         self.model_path = model_path
#         super().__init__(app)
#         self.format ='3f 3f'
#         self.attribs = ['in_normal', 'in_position']
#
#     def get_vertex_data(self):
#         wf = pwf.Wavefront(self.model_path, create_materials=True, collect_faces=True, cache=False, parse=True)
#         objs = pwf.ObjParser(wf, self.model_path, create_materials=True, collect_faces=True, cache=False, parse=True)
#
#         vertex_data = objs.wavefront.vertices
#         vertex_data = np.array(vertex_data, dtype='f4')
#
#         return vertex_data
from Model3D_og import *


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        add(Cube(app, 'cube'))
        add(Cube(app, 'cube', tex_id=1, pos=(0.5, 15.0, 0), rot=(45, 0, 0),scale=(1, 2, 1)))
        add(Cube(app, 'cube',tex_id=2, pos=(1.0, 0, 0), rot=(0, 0, 45), scale=(1, 1, 2)))
        # n, s = 30, 2
        # for x in range(-n, n, s):
        #     for z in range(-n, n, s):
        #         add(Cube(app,'cube', pos=(x, -s, z)))

        # add(Cat(app, vao_name="cat", tex_id="cat", pos=(0, -2, -10)))
        add(Model(app, 'ptero',
                  tex_id='ptero',
                  model_path='Models/Pterodactylus/13625_Pterodactylus_v1_L1.obj',
                  has_material=True,
                  pos=(0, 5, -10), rot=(-45, 0, 0), scale=(0.25, 0.25, 0.25)))
        # add(Model(app, 'bary',
        #           'Models/16372_Baryonyx_v1_NEW.obj',
        #           pos=(-7.5, 5, -10), rot=(90, 0, 0),scale=(0.25, 0.25, 0.25)))
        # add(Model(app, 'deino',
        #           model_path="Models/13216_Deinonychus_NEW.obj",
        #           pos=(9.0, 3.0, -10),
        #           rot=(0, 0, 0),
        #           scale=(0.25, 0.25, 0.25)))

    def render(self):
        for obj in self.objects:
            obj.render()

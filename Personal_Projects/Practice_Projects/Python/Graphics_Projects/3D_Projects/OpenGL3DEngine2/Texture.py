import pygame as pg
import moderngl as mgl


class Texture:
    def __init__(self, ctx):
        self.ctx = ctx
        self.textures = {}
        self.textures[0] = self.get_texture(path='textures/img.png')
        self.textures[1] = self.get_texture(path='textures/img_1.png')
        self.textures[2] = self.get_texture(path='textures/img_2.png')
        # self.textures['cat'] = self.get_texture(path='Models/Cat/20430_cat_diff_v1.jpg')
        ##self.textures['ptero'] = self.get_texture(path='Models/Pterodactylus/13625_Pterodactylus_diff.tif')
        self.addTexture('ptero', tx_path='Models/Pterodactylus/13625_Pterodactylus_diff.tif')

    def addTexture(self, tx_name, tx_path):
        self.textures[tx_name] = self.get_texture(path=tx_path)

    # def get(self, tx_name):
    #     if (self.exists(tx_name)):
    #         return self.textures[tx_name]
    #     else:
    #         print(f'Texture {tx_name} does not exist!!!')

    def exists(self, name):
        if self.textures.get(name) is None:
            return False
        return True

    def get_texture(self, path):
        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB'))
        #   mipmaps : to give textures of different sizes reducing by actor 1/(2^n)
        texture.filter = (mgl.LINEAR_MIPMAP_LINEAR, mgl.LINEAR)
        texture.build_mipmaps()
        #   To improve texture quality, using anisotropic filtering:
        texture.anisotropy = 32.0
        return texture

    def destroy(self):
        [tex.release() for tex in self.textures.values()]
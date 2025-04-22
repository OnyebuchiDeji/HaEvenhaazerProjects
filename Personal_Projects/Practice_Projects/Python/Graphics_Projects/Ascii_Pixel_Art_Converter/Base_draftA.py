import pygame as pg
import cv2

""""
    This draft shows an issue that comes with reading an image with opencv and then displaying it with pygame.
    The format the read image is in is in a way that make pygame rotate it, mirror it, and give a wrong color of it
    It is fixed in the main Base.py file.

        Learnt form CoderSpace Youtube
"""

class ArtConverter:
    def __init__(self, path="Resources/car.jpg"):
        pg.init()
        self.path = path
        ##  THis .imread() method returns a numpy array
        self.image = cv2.imread(self.path)
        self.RES = self.WIDTH, self.HEIGHT = self.image.shape[0], self.image.shape[1]
        ##  Surface for rendering based on resolution
        self.surface = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()


    def get_image(self):
        pass

    def draw(self):
        pg.surfarray.blit_array(self.surface, self.image)
        cv2.imshow("img", self.image)


    def run(self):
        while True:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    exit()
            self.draw()
            ##  Displays Frame Rate on Window's Header
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick()


if __name__ == '__main__':
    app = ArtConverter()
    app.run()
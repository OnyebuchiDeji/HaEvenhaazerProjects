import pygame as pg
import cv2

""""
    This file is called Base because these are the main things setup before finally making the different
    image converters.
    The main goal is to show that one can read an image with Opencv and display it successfully with Pygame

    Learnt form CoderSpace Youtube
"""

class ArtConverter:
    def __init__(self, path="Resources/car.jpg"):
        pg.init()
        self.path = path
        ##  Changed from cv2.imreas(self.path) to...
        self.image = self.get_image()
        self.RES = self.WIDTH, self.HEIGHT = self.image.shape[0], self.image.shape[1]
        print(self.RES)
        ##  Surface for rendering based on resolution
        self.surface = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()


    def get_image(self):
        ##  First, read image
        self.cv2_image = cv2.imread(self.path)
        ##  Then flip image back to its side
        transposed_image =cv2.transpose(self.cv2_image)
        ##  Get right rgb format of image
        rgb_image = cv2.cvtColor(transposed_image, cv2.COLOR_RGB2BGR)
        return rgb_image
    
    def draw_cv2_image(self):
        ##  This method is just to display the image through opencv in a smaller scale
        resized_cv2_image = cv2.resize(self.cv2_image, (640, 360), interpolation=cv2.INTER_AREA)
        cv2.imshow("img", resized_cv2_image)

    def draw(self):
        pg.surfarray.blit_array(self.surface, self.image)
        self.draw_cv2_image()


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
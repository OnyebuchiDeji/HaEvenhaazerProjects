import pygame as pg
import numpy as np
from numba import njit
import pygame.gfxdraw as pgGfxDraw
import cv2

""""
        This is Pixel Art! The Thrid One in the Episode

        The changes are clear. But here, video conversion is also implemented.
        In this version, numba is used to speed up the converting of the image to pixel image
        In this, the ability to record converted videos is also implemented
        
        Learnt form CoderSpace Youtube
"""

@njit(fastmath=True)
def accelerate_conversion(image, width, height, color_coeff, step):
    ##  Here, the array of the next frame is iterated over
    array_of_values = []
    for x in range(0, width, step):
        for y in range(0, height, step):
            ##  Divide by color coefficient and form tuples of colour keys
            r, g, b = image[x, y]   //  color_coeff
            if r + g + b:
                ##  Write their positions to the list of output values of the function
                array_of_values.append(((r, g, b),  (x, y)))

    return array_of_values



class ArtConverter:
    def __init__(self, path="Resources/test.mp4", pixel_size=7, color_lvl=8):
        pg.init()
        self.path = path
        self.capture = cv2.VideoCapture(path)
        self.PIXEL_SIZE = pixel_size
        ##  The COLOR_LVL parameter will determine the number of colors in th palette.
        ##  The values chosen for it should be numbers in the power if 2: 4, 8, 16, 32.
        ##  The number of colors will be defines as COLO_LVL^3. For example, with COLOR_LVL = 4, the number....
        ##  of colors will be 4^3 = 64(6 bit), 8 8 = 512(9bit), 16 = 4096(12 bit)
        self.COLOR_LVL = color_lvl

        ##  Just normal coloured image needed
        self.image = self.get_image()
        self.RES = self.WIDTH, self.HEIGHT = self.image.shape[0], self.image.shape[1]
        print(self.RES)
        self.surface = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.PALETTE, self.COLOR_COEFF = self.create_palette()

        self.rec_fps = 25
        self.record = False
        self.recorder = cv2.VideoWriter("Output/PixelArtConvertedVideo2.mp4", cv2.VideoWriter_fourcc(*"mp4v"),
                                        self.rec_fps, self.RES)

    def get_frame(self):
        ##  Convert surface to 3d array
        frame = pg.surfarray.array3d(self.surface)
        ##  Convert color
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        ##  Convert orientation and return
        return cv2.transpose(frame)

    def record_frame(self):
        if self.record:
            frame = self.get_frame()
            ##  Write each frame every loop to the opencv object
            self.recorder.write(frame)
            cv2.imshow('Frame', frame)
            if cv2.waitKey(1) & 0xFF == 27:
                self.record = not self.record
                cv2.destroyAllWindows()

    ##  This is where all the transformations of the original image into ASCII will occur
    def draw_converted_image(self):
        ##  Because at each step of the loop a new frame is received, store each as image:
        self.image = self.get_image()
        array_of_values = accelerate_conversion(self.image, self.WIDTH, self.HEIGHT,
                                                self.COLOR_COEFF, self.PIXEL_SIZE)
        for color_key, (x, y) in array_of_values:
            color = self.PALETTE[color_key]
            ##  Display square filled with the color
            pgGfxDraw.box(self.surface, (x, y, self.PIXEL_SIZE, self.PIXEL_SIZE), color)


    def create_palette(self):
        ##  THis is used to pre-render all characters for each colour, for performance boost
        colors, color_coeff = np.linspace(0, 255, num=self.COLOR_LVL, dtype=int, retstep=True)
        color_palette = [np.array([r, g, b]) for r in colors for g in colors for b in colors]
        ##  The palette structure is a dictionary in which the characters will act as its keys...
        ##  Only one dictionary is needed to determine the color by key
        palette = {}
        color_coeff = int(color_coeff)
        ##  Loop through array of tuples of coour channels, r, g, b
        for color in color_palette:
            ##  Normalize color  by a coefficient that is calculated by the initial parameter...
            #  that sets the number of colour levels for each RGB colour level.
            color_key = tuple(color // color_coeff)
            ##  Use normalize color as key to get the renderable text object
            palette[color_key] = color

        return palette, color_coeff



    def get_image(self):
        ##  Get next fram from capture object
        ret, self.cv2_image = self.capture.read()
        ##  Check for end of frames in capture object. If end, exit()
        if not ret:
            exit()
        ##  Then flip image back to its side
        transposed_image =cv2.transpose(self.cv2_image)
        ##  Image with rgb
        image = cv2.cvtColor(transposed_image, cv2.COLOR_BGR2RGB)
        return image
    
    def draw_cv2_image(self):
        ##  This method is just to display the image through opencv in a smaller scale
        resized_cv2_image = cv2.resize(self.cv2_image, (640, 360), interpolation=cv2.INTER_AREA)
        cv2.imshow("img", resized_cv2_image)

    def draw(self):
        self.surface.fill('black')
        self.draw_converted_image()
        # self.draw_cv2_image()

    def save_image(self):
        ##  First, convert pygame surface into a 3d array
        pygame_image = pg.surfarray.array3d(self.surface)
        ##  It turns the image since
        cv2_img = cv2.transpose(pygame_image)
        cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_RGB2BGR)
        cv2.imwrite("Output/pixel_car.jpg", cv2_img)
        print("Image saved!")



    def run(self):
        while True:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    exit()
                ## Pressed to save the image 
                elif e.type == pg.KEYDOWN:
                        if e.key == pg.K_s:
                            self.save_image()
                        ##  So that onee can stop recording anytime
                        if e.key == pg.K_r:
                            self.record = not self.record
            self.record_frame()
            self.draw()
            ##  Displays Frame Rate on Window's Header
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick()


if __name__ == '__main__':
    app = ArtConverter()
    app.run()
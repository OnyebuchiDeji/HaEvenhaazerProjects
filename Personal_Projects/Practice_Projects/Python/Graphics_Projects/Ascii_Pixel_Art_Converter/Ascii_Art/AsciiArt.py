import pygame as pg
import cv2

""""
    The First One!


        Learnt form CoderSpace Youtube
"""

class ArtConverter:
    def __init__(self, path="Resources/car.jpg", font_size=12):
        pg.init()
        self.path = path
        ##  Changed from cv2.imreas(self.path) to...
        self.image = self.get_image()
        self.RES = self.WIDTH, self.HEIGHT = self.image.shape[0], self.image.shape[1]
        print(self.RES)
        ##  Surface for rendering based on resolution
        self.surface = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()

        ##  String of ASCII characters of different brightness based on their number
        self.ASCII_CHARS = '.",:;!~+-xmo*#W&8@'
        ##  A unique coefficient resulting from dividing the colour value by the length of the character string
        ##  which can be used to get the index of each character based on their colour value or brightness from...
        ##  the string. 
        self.ASCII_COEFF = 255 // (len(self.ASCII_CHARS) - 1)

        self.font = pg.font.SysFont('Courier', font_size, bold=True)
        ##  In proportion to the font size, calculating the step of each character
        ##  The step of each character determines how far they are when rendered.
        self.CHAR_STEP = int(font_size * 0.5)
        ##  To improve performance, create a list of all rendered characters in white in advance:
        self.RENDERED_ASCII_CHARS = [self.font.render(char, False, 'white') for char in self.ASCII_CHARS]



    ##  This is where all the transformations of the original image into ASCII will occur
    def draw_converted_image(self):
        ##  Divide the colour values of the pixels by the ascii coefficient so that...
        ##  The entire array consists of the indices needed to select the appropriate ASCII characters from the string
        image_char_indices= self.image // self.ASCII_COEFF
        for x in range(0, self.WIDTH, self.CHAR_STEP):
            for y in range(0, self.HEIGHT, self.CHAR_STEP):
                char_index = image_char_indices[x, y]
                if char_index:  ##  THis if statement makes sure that black colours are not rendered
                    self.surface.blit(self.RENDERED_ASCII_CHARS[char_index], (x, y))


    def get_image(self):
        ##  First, read image
        self.cv2_image = cv2.imread(self.path)
        ##  Then flip image back to its side
        transposed_image =cv2.transpose(self.cv2_image)
        ##  This was changed from cv2.COLOR_RGB2BGR to:
        gray_image = cv2.cvtColor(transposed_image, cv2.COLOR_BGR2GRAY)
        return gray_image
    
    def draw_cv2_image(self):
        ##  This method is just to display the image through opencv in a smaller scale
        resized_cv2_image = cv2.resize(self.cv2_image, (640, 360), interpolation=cv2.INTER_AREA)
        cv2.imshow("img", resized_cv2_image)

    def draw(self):
        self.surface.fill('black')
        self.draw_converted_image()
        self.draw_cv2_image()

    def save_image(self):
        ##  First, convert pygame surface into a 3d array
        pygame_image = pg.surfarray.array3d(self.surface)
        ##  It turns the image since
        cv2_img = cv2.transpose(pygame_image)
        cv2.imwrite("Output/ascii_car.jpg", cv2_img)
        print("Image saved!")



    def run(self):
        while True:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    exit()
                ## Pressed to save the image 
                elif e.type == pg.KEYDOWN:
                        if e.key ==pg.K_s:
                            self.save_image()

            self.draw()
            ##  Displays Frame Rate on Window's Header
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick()


if __name__ == '__main__':
    app = ArtConverter()
    app.run()
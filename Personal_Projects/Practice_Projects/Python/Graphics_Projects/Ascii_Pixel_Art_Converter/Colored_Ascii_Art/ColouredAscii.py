import pygame as pg
import numpy as np
import cv2

""""
    This is coloured ASCII! It is the second one in the tutorial from CoderSpace. His name is actually 
    Stanislav Petrov

    An example of the palette structure, for example, the character, '#', with COLOR_LVL=8 is this:
    With the knowledge that each character will be rendered in 512 possible colors because 8^3=512, so 3 are RGB channels

    The JSON representation of the information could be this way:
    palette =
    {
    '#':
        {
        (0, 0, 0): <Surface(7x14x8 SW)>, ..., (7, 7, 7): <Surface(7x14x8 SW)>
        }
    }
    this representation just means each character can be rendered with 512 different combinations of values for....
    each colour channel, as each combination represents a unique colour

    
    Also, when I tried to save the image, it gave a blue coloured car.
    This was not fixed by changing the line:  image = cv2.cvtColor(transposed_image, cv2.COLOR_BGB2RGB)
    in the getImage() method to
    image = cv2.cvtColor(transposed_image, cv2.COLOR_RGB2BGR)

    Rather, it was fixed in the save_image() method by applying the appropriate changes to the pygame image.
    The following was applied after transposing the image:
    cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_RGB2BGR)
    The transpose method rotates the image to right orientation.
    Then the above code sets its colour aright, before saving it.
    It was simply caused by pygame's being unable to interpret the format the image was stored in the...
    self.surface by the opencv correctly. So opencv had to apply the appropriate changes to it, to use...
    colur format 

        Learnt form CoderSpace Youtube
"""

class ArtConverter:
    def __init__(self, path="Resources/car.jpg", font_size=12, color_lvl=8):
        pg.init()
        self.path = path
        ##  The COLOR_LVL parameter will determine the number of colors in th palette.
        ##  The values chosen for it should be numbers in the power if 2: 4, 8, 16, 32.
        ##  The number of colors will be defines as COLO_LVL^3. For example, with COLOR_LVL = 4, the number....
        ##  of colors will be 4^3 = 64(6 bit), 8 8 = 512(9bit), 16 = 4096(12 bit)
        self.COLOR_LVL = color_lvl
        ##  Changed too. Now working with black and white image to determine each ASCII characters...
        ##  and colour image to determine each characters colour
        self.image, self.gray_image = self.get_image()
        self.RES = self.WIDTH, self.HEIGHT = self.image.shape[0], self.image.shape[1]
        print(self.RES)
        self.surface = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()

        ##  Differetn Ascii characters

        self.ASCII_CHARS = ' ixzao*#MW&8%B@$'
        ##  A unique coefficient resulting from dividing the colour value by the length of the character string
        ##  which can be used to get the index of each character based on their colour value or brightness from the string. 
        self.ASCII_COEFF = 255 // (len(self.ASCII_CHARS) - 1)

        self.font = pg.font.SysFont('Courier', font_size, bold=True)
        ##  In proportion to the font size, calculating the step of each character
        ##  The step of each character determines how far they are when rendered.
        self.CHAR_STEP = int(font_size * 0.5)
        ##  To improve performance, create a list of all rendered characters in white in advance:
        # Removed: self.RENDERED_ASCII_CHARS = [self.font.render(char, False, 'white') for char in self.ASCII_CHARS]
        ##  Get PALETTE and COLOR_COEFF with which to determine the desired color for each character.
        self.PALETTE, self.COLOR_COEFF = self.create_palette()



    ##  This is where all the transformations of the original image into ASCII will occur
    def draw_converted_image(self):
        ##  Divide the colour values of the pixels by the ascii coefficient so that...
        ##  The entire array consists of the indices needed to select the appropriate ASCII characters from the string
        image_char_indices= self.gray_image // self.ASCII_COEFF
        ##  Divide the image array by the COLOR_COEFF 
        image_color_indices = self.image // self.COLOR_COEFF
        for x in range(0, self.WIDTH, self.CHAR_STEP):
            for y in range(0, self.HEIGHT, self.CHAR_STEP):
                char_index = image_char_indices[x, y]
                if char_index:  ##  THis if statement makes sure that black colours are not rendered
                    ##  Get the value of the character and color by which one gets the correct indices of the...
                    #   already rendered ASCII colours from the palette and apply it to the pygame surface.
                    char = self.ASCII_CHARS[char_index]
                    color = tuple(image_color_indices[x, y])
                    ##  Then apply it to pygame surface
                    self.surface.blit(self.PALETTE[char][color], (x, y))


    def create_palette(self):
        ##  THis is used to pre-render all characters for each colour, for performance boost
        colors, color_coeff = np.linspace(0, 255, num=self.COLOR_LVL, dtype=int, retstep=True)
        color_palette = [np.array([r, g, b]) for r in colors for g in colors for b in colors]
        ##  The palette structure is a dictionary in which the characters will act as its keys...
        ##  and the values will be dictionaries with tuples of normalized colour values as their keys.
        palette = dict.fromkeys(self.ASCII_CHARS, None)
        color_coeff = int(color_coeff)
        ##  so for every character that acts as the key in palette
        for char in palette:
            ##  Make an emoty dictionary
            char_palette = {}
            ##  Loop through array of tuples of coour channels, r, g, b
            for color in color_palette:
                ##  Normalize color  by a coefficient that is calculated by the initial parameter...
                #  that sets the number of colour levels for each RGB colour level.
                color_key = tuple(color // color_coeff)
                ##  Use normalize color as key to get the renderable text object
                char_palette[color_key] = self.font.render(char, False, tuple(color))
            ##  Add the dict of renderable coloured text to the palette with the corresponding key
            palette[char] = char_palette
        return palette, color_coeff



    def get_image(self):
        ##  First, read image
        self.cv2_image = cv2.imread(self.path)
        ##  Then flip image back to its side
        transposed_image =cv2.transpose(self.cv2_image)
        ##  Image with rgb
        image = cv2.cvtColor(transposed_image, cv2.COLOR_BGR2RGB)
        ##  Image with just black and white
        gray_image = cv2.cvtColor(transposed_image, cv2.COLOR_BGR2GRAY)
        return image, gray_image
    
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
        cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_RGB2BGR)
        cv2.imwrite("Output/coloured_ascii_car_corrected2.jpg", cv2_img)
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
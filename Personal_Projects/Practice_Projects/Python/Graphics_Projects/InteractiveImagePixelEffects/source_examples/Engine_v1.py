"""
    This program creation started: Tue-30-Jan-2024

    It was made following the procedure of Frank in Franks Laboratory on YT

    On this versin, I completed the method that allows one to fully manipulate an image...
    to crop it and control which parts are rendered.
"""
import sys
import pygame as pg

class Image:
    def __init__(self, path, res: tuple[int, int]):
        self.x, self.y = 0, 0
        self.width, self.height = res
        self.path = path
        self.surface = self.init_image(self.path, (self.width, self.height))
        # self.get_image(0, 0, 0, 0)
    
    @staticmethod
    def init_image(path, resolution):
        image = pg.image.load(path)
        return pg.transform.smoothscale(image, resolution)
    
    def get_image(self, srcx, srcy, src_width, src_height, surf_x, surf_y, surf_width, surf_height):
        """
            This is the method that will take only some parts of the image and display it.
            It accessed the image's pixel array to do this. 

            scrx, scry, src_width, scr_height determine the cropping area
            scr stands for source
        """

        ##  This is a 2D array
        imagePixelArray = pg.PixelArray(self.surface)

        ##  This prints the strides per byte for RGBA.
        ##  For each pixel in a column, to the next is 4 bytes
        ##  For one row to the other is 4*screen_width bytes
        print(imagePixelArray.strides[0], ", ", imagePixelArray.strides[1])

        ##  column or width
        ##  Because stride for pixels in the same row, from column to column is 4 bytess
        stride = 1

        column_start =  srcx * stride
        column_stop = src_width * stride

        ##  row or height
        ##  Don't need to multiply by 4. Row to row only increments by 1
        row_start =  srcy  * stride
        row_stop =  src_height * stride

        ##  Doing this:
        #   newPixelArray: pg.PixelArray = imagePixelArray[column_start:column_stop][row_start:row_stop]
        ##  is the same as...
        ##  This is practically: imagePixelArray(x, y)
        newPixelArray: pg.PixelArray = imagePixelArray[column_start:column_stop:1, row_start:row_stop:1]
        
        newImage = newPixelArray.make_surface()
        ##  This is to make the image fit the surface it is rendered in
        # newImage = pg.transform.smoothscale(newImage, (surf_width, surf_height))

        ##  To move the image

        self.x = surf_x
        self.y = surf_y

        return newImage

class Cell:
    def __init__(self, canvas:"Canvas", x, y, pixels: pg.Surface):
        self.canvas_ref = canvas
        self.x, self.y = x, y
        self.width, self.height = self.decorator_ref.cell_width, self.decorator_ref.cell_height
        self.surface = pg.Surface(self.width, self.height)
        self.image_pixels = pixels
    
    def get_pixels(self):
        self.surface.blit(self.image_pixels, (0, 0))

    def draw(self):
        self.canvas_ref.surface.blit(self.surface, (self.x, self.y))
        # pg.draw.rect(self.decorator_ref.app_ref.screen, (0, 0, 0), pg.Rect((self.x, self.y), (self.width, self.height)), 1)

class Canvas:
    def __init__(self, appRef: "Engine"):
        self.app_ref = appRef
        self.cell_width = self.app_ref.screen_width // 35
        self.cell_height = self.app_ref.screen_height // 35

        self.surface = pg.Surface((self.app_ref.screen_width, self.app_ref.screen_height), pg.SRCALPHA)

        ##  This array, however, is 1D
        self.image_grid: list[Cell] = []
        # self.make_grid()
    
 
    # def make_grid(self):
    #     for row in range(self.app_ref.screen_width):
    #         for column in range(self.app_ref.screen_height):
    #             self.image_grid.append(Cell(self, column * self.cell_width, row * self.cell_height))

    def display_grid(self):
        for cell in self.image_grid:
            cell.draw()
        
    def display_image(self):
        img = Image("resource/sharingan2.png", self.app_ref.resolution)
        # img.surface(x, y, width, height)
        
        # self.surface.blit(img.surface, (img.x, img.y))
        self.surface.blit(img.get_image(0, 0,50, 30, 50, 50, 50, 30), (img.x, img.y))

    # def display_image_grid(self):
    #     self.display_image(0, 0, 250, 250)
    #     for cell in self.image_grid:
    #         cell.draw()
    
    def display(self):
        self.surface.fill((0, 0, 0))
        self.display_image()
        # self.display_Image_grid()
        self.app_ref.screen.blit(self.surface, (0, 0))
        # self.display_grid()


class Engine:
    def __init__(self):
        self.resolution = self.screen_width, self.screen_height = 1120, 630
        self.screen = pg.display.set_mode(self.resolution)
        self.fps = 60
        self.clock = pg.time.Clock()

        self.decor_app = Canvas(self)
    
    def listen_for_exit(self):
        for e in pg.event.get():
            if e.type == pg.QUIT or (pg.key==pg.KEYDOWN and pg.type==pg.K_ESCAPE):
                pg.quit()
                sys.exit()
    
    def update_display(self):
        self.decor_app.display()
        pg.display.flip()
        

    def run(self):
        while True:
            self.listen_for_exit()
            self.update_display()
            self.clock.tick(self.fps)

if __name__=="__main__":
    Engine().run()

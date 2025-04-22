"""
    This program creation started: Tue-30-Jan-2024

    It was made following the procedure of Frank in Franks Laboratory on YT

    You can find explanations in the source_examples folder future me :)


    Date: Sun-04-Feb-2024
    There was a major problem in the get_image() method for getting what part of the image each Cell will render.
    The issue was that I kept doing this:
        stride = 1

        column_start =  srcx * stride
        column_stop = src_width * stride

        row_start =  srcy  * stride
        row_stop =  src_height * stride

        newPixelArray: pg.PixelArray = imagePixelArray[column_start:column_stop:1, row_start:row_stop:1]
        newImage = newPixelArray.make_surface()
    
        Now, this worked for the Engine_v1.py but was not working for this one because of this:
        it would always give the error at  newImage = newPixelArray.make_surface(), that 
        'NoneType' object has no atribute 'make_surface'

        This was because of this line newPixelArray: pg.PixelArray = imagePixelArray[column_start:column_stop:1, row_start:row_stop:1]
        specifically, the values of column_start, column_stop, row_start, and row_stop.
        This is because for the cells,
        in row 1, the first cell has starting position x, y = (0, 0)
        So its column_start = 0, row_start = 0, and column_end should be = x (it's current x position) + its width
        likewise, for row_end, it should be = y (it's current y position) + its height

        This is so that, for example, the second cell in the same row, that is, the next column should be x, y = (self.width, 0)
        column_start and row_start are like the previous, just self.x, self.y respectively.

        But column_end should be = x (it's current x position) + cell width
        likewise row_end should be = y (it's current y position) + cell height

        This way each cell renders the appropriate section of the image that it should occupy and render.

        The mistake I made is not adding self.x + and self.y +.
        This made the newPixelArray object to not be made correctly, resulting in the NonType error
        column_stop = self.x +  self.width * stride
        row_stop =  self.y + self.height * stride

    2. Also, in this segment of code:
        stride = 1

        ##  column or width
        column_start =  self.x * stride
        column_stop = self.x +  self.width * stride

        row_start =  self.y  * stride
        row_stop =  self.y + self.height * stride

        stride is not really important. If anything, it should be 1; anything higher skips pixels at the start and passes pixels at the end...
        or something like that.
        newPixelArray: pg.PixelArray = imagePixelArray[column_start:column_stop:1, row_start:row_stop:1]
        Also, the vale, '1' at the edn of the slice operator imagePixelArray[column_start:column_stop:1, row_start:row_stop:1]...
        for row and column, has more of a rectangular manipulation effect since that is the step.
        It still goes throught everything, but it does not skip pixels but rather... if you change it to a higher value, like 4, it will...
        shrink the image along the x-axis.
"""
import sys
import pygame as pg

class Image:
    def __init__(self, path:str, res: tuple[int, int]):
        self.x, self.y = 0, 0
        self.width, self.height = res
        self.path = path
        self.surface = self.init_image(self.path, (self.width, self.height))

    @staticmethod
    def init_image(path, resolution):
        image = pg.image.load(path)
        return pg.transform.smoothscale(image, resolution)
    


class Cell:
    def __init__(self, canvas:"Canvas", x: int, y: int):
        self.canvas_ref = canvas
        self.x, self.y = x, y
        self.width, self.height = self.canvas_ref.cell_width, self.canvas_ref.cell_height
        self.image = Image("resource/sharingan2.png", (self.canvas_ref.app_ref.screen_width, self.canvas_ref.app_ref.screen_height))
        self.surface = self.get_image()
        

    def draw(self):
        self.canvas_ref.surface.blit(self.surface, (self.x, self.y))
        pg.draw.rect(self.canvas_ref.surface, (0, 0, 0), pg.Rect((self.x, self.y), (self.width, self.height)), 1)
    
    def get_image(self):
        """
            This is the method that will take only some parts of the image and display it.
            It accessed the image's pixel array to do this. 

            scrx, scry, src_width, scr_height determine the cropping area
            scr stands for source
        """

        ##  This is a 2D array
        imagePixelArray = pg.PixelArray(self.image.surface)

        ##  Because stride for pixels in the same row, from column to column is 4 bytess
        stride = 1

        ##  column or width
        column_start =  self.x * stride
        column_stop = self.x +  self.width * stride

        ##  row or height
        ##  Don't need to multiply by 4. Row to row only increments by 1
        row_start =  self.y  * stride
        row_stop =  self.y + self.height * stride

        newPixelArray: pg.PixelArray = imagePixelArray[column_start:column_stop:1, row_start:row_stop:1]
        
        newImage = newPixelArray.make_surface()
        newImage = pg.transform.smoothscale(newImage, (self.width, self.height))

        return newImage





class Canvas:
    def __init__(self, appRef: "Engine"):
        self.app_ref = appRef
        self.cell_width = self.app_ref.screen_width // 32
        self.cell_height = self.app_ref.screen_height // 18

        self.surface = pg.Surface((self.app_ref.screen_width, self.app_ref.screen_height), pg.SRCALPHA)

        ##  This array, however, is 1D
        self.image_grid: list[Cell] = []
        self.make_grid()
    
 
    def make_grid(self):
        for row in range(0, self.app_ref.screen_height, self.cell_height):
            for column in range(0, self.app_ref.screen_width, self.cell_width):
                self.image_grid.append(Cell(self, column, row))

    def display_Image_grid(self):
        for cell in self.image_grid:
            cell.draw()
        
    
    def display(self):
        self.surface.fill((255, 255, 255))
        self.display_Image_grid()
        self.app_ref.screen.blit(self.surface, (0, 0))




class Engine:
    def __init__(self):
        self.resolution = self.screen_width, self.screen_height = 1120, 630
        self.screen = pg.display.set_mode(self.resolution)
        self.fps = 60
        self.clock = pg.time.Clock()

        self.canvas = Canvas(self)
    
    def listen_for_exit(self):
        for e in pg.event.get():
            if e.type == pg.QUIT or (pg.key==pg.KEYDOWN and pg.type==pg.K_ESCAPE):
                pg.quit()
                sys.exit()
    
    def update_display(self):
        self.canvas.display()
        pg.display.flip()
        

    def run(self):
        while True:
            self.listen_for_exit()
            self.update_display()
            self.clock.tick(self.fps)
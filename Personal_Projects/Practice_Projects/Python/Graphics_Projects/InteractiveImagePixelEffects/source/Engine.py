"""
    This program creation started: Tue-30-Jan-2024

    It was made following the procedure of Frank in Franks Laboratory on YT

    You can find explanations in the source_examples folder future me :)

    Date: Sun-04-Feb-2024
    Issue with get_image() method fixed!
    Explanation is in Engine2_ImageGrid.py

    Comment: Thurs-15-Feb-2024
    Imported time to implement the last effect on the Image...
    to delay the call of the start() method, to make the cells of the image being loaded and moving to be visibly seen
"""
import sys
import pygame as pg
import math
import time
import random as rnd
# class Image:
#     def __init__(self, path:str, res: tuple[int, int]):
#         self.x, self.y = 0, 0
#         self.width, self.height = res
#         self.path = path
#         self.surface = self.init_image(self.path, (self.width, self.height))
#         self.img_width, self.img_height = self.surface.get_width(), self.surface.get_height()

#     @staticmethod
#     def init_image(path, resolution):
#         image = pg.image.load(path)
#         return pg.transform.smoothscale(image, resolution)

class Image:
    def __init__(self, path:str):
        self.x, self.y = 0, 0
        # self.width, self.height = res
        self.path = path
        self.surface = self.init_image(self.path)
        self.img_width, self.img_height = self.surface.get_width(), self.surface.get_height()

    @staticmethod
    def init_image(path):
        image = pg.image.load(path)
        # return pg.transform.smoothscale(image, resolution)
        return image


class Cell:
    def __init__(self, canvas:"Canvas", x: int, y: int, index: int):
        self.canvas_ref = canvas
        self.x, self.y = x, y
        self.index = index
        self.width, self.height = self.canvas_ref.cell_width, self.canvas_ref.cell_height
        
        # self.surface = self.canvas_ref.get_image(self.canvas_ref.image.surface, self.x, self.y, self.width, self.height, self.width, self.height)

        self.positionX = self.canvas_ref.image.img_width * 0.5
        self.positionY = self.canvas_ref.image.img_height * 0.5
        self.speedX = 0
        self.speedY = 0
        self.slideX = 0
        self.slideY = 0
        self.vx = 0
        self.vy = 0
        self.ease = 0.01
        self.friction = 0.8
        self.randomizeEase = rnd.random() * 10 + 2

        self.start()
        
    def start(self):
        time.sleep(self.index * 0.000001)
        self.speedX = (self.x - self.positionX) / self.randomizeEase
        self.speedY = (self.y - self.positionY) / self.randomizeEase

    def update(self):
        ##  This is so that the calculation does not keep going for cells...
        ##  that are already in their right positions or close to them
        ##  But this mean
        if (math.fabs(self.speedX) > 0.01 or math.fabs(self.speedY) > 0.01):
            self.speedX = (self.x - self.positionX) / self.randomizeEase
            self.speedY = (self.y - self.positionY) / self.randomizeEase
            ##  self.positionX and self.positionY start at specified regions...
            ##  But their positipn moves over time with self.speedX and self.speedY respectively...
            ## to finally get to their original position. 
            self.positionX += self.speedX
            self.positionY += self.speedY
        
        mousePos = pg.mouse.get_pos()

        dx = mousePos[0] - self.x
        dy = mousePos[1] - self.y
        distance = math.hypot(dx, dy)

        if (distance < self.canvas_ref.mouse_radius):
            angle = math.atan2(dy, dx)
            force = distance / self.canvas_ref.mouse_radius

            self.vx = force * math.cos(angle)
            self.vy = force * math.sin(angle)
        
        self.vx *= self.friction
        self.vy *= self.friction
        self.slideX += self.vx - (self.slideX * self.ease)
        self.slideY += self.vy - (self.slideY * self.ease)
        
    def draw(self):
        self.surface = self.canvas_ref.get_image(self.canvas_ref.image.surface, int(self.x + self.slideX), int(self.y + self.slideY), self.width, self.height, self.width, self.height)
        self.canvas_ref.surface.blit(self.surface, (self.positionX, self.positionY))
        pg.draw.rect(self.canvas_ref.surface, (0, 0, 0), pg.Rect((self.positionX, self.positionY), (self.width, self.height)), 1)

    


class Canvas:
    def __init__(self, appRef: "Engine"):
        self.app_ref = appRef
        self.image = Image("resource/veloci.jpg")

        self.cell_width = self.image.img_width // 20
        self.cell_height = self.image.img_height // 35
        print(f"Image Width: {self.image.img_width}, Image Height: {self.image.img_height}")
        self.surface = pg.Surface((self.image.img_width, self.image.img_height), pg.SRCALPHA)

        self.mouse_radius = 100
        ##  This array, however, is 1D
        self.image_grid: list[Cell] = []
        self.make_grid()

    
 
    def make_grid(self):
        index = 0
        for row in range(0, self.image.img_height, self.cell_height):
            for column in range(0, self.image.img_width, self.cell_width):
                index += 1
                self.image_grid.append(Cell(self, column, row, index))

    def display_Image_grid(self):
        for cell in self.image_grid:
            cell.draw()
            cell.update()
        
    
    def display(self):
        self.surface.fill((255, 255, 255))
        self.display_Image_grid()
        self.app_ref.screen.blit(self.surface, (0, 0))

    def get_image(self, image_surface, srcx, srcy, src_width, src_height, surf_width, surf_height):
        """
            This is the method that will take only some parts of the image and display it.
            It accessed the image's pixel array to do this. 

            scrx, scry, src_width, scr_height determine the cropping area
            scr stands for source
        """

        ##  This is a 2D array
        imagePixelArray = pg.PixelArray(image_surface)

        ##  Because stride for pixels in the same row, from column to column is 4 bytess
        stride = 1

        ##  column or width
        column_start =  srcx * stride
        column_stop = srcx +  src_width * stride

        ##  row or height
        ##  Don't need to multiply by 4. Row to row only increments by 1
        row_start =  srcy * stride
        row_stop =  srcy + src_height * stride

        newPixelArray: pg.PixelArray = imagePixelArray[column_start:column_stop:1, row_start:row_stop:1]
        
        newImage = newPixelArray.make_surface()
        newImage = pg.transform.smoothscale(newImage, (surf_width, surf_height))

        return newImage




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
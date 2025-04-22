import pygame as pg
from collections import deque
from random import choice, randrange

"""
    Even measured the program's performance
"""

class Ant:
    def __init__(self, app, pos, color):
        self.app = app
        self.color = color
        self.x, self.y = pos
        ##  Set of increments for motion of ant, also affecting its rotation
        ##  right, down, left, up -- clockwise. The reverse is anticlockwise
        self.increments = deque([(1, 0), (0, 1), (-1, 0), (0, -1)])

    def run(self):
        """
            Whole array is initially filled with zeros, representing white
            The zero is changed to one, representing black
        """
        value = self.app.grid[self.y][self.x]
        ##  The three below are the same way to do the same thing, switching 0 to 1 and vice versa
        # self.app.grid[self.y][self.x] = (value + 1) % 2
        # self.app.grid[self.y][self.x] = value ^ 2   ##  Bitwise XOR, addition by modular 2
        self.app.grid[self.y][self.x] = not value
        
        SIZE = self.app.CELL_SIZE
        rect = self.x * SIZE, self.y * SIZE, SIZE - 1, SIZE - 1
        if value:
            pg.draw.rect(self.app.screen, pg.Color('white'), rect)
        else:
            pg.draw.rect(self.app.screen, self.color, rect)
        
        self.increments.rotate(1) if value else self.increments.rotate(-1)
        dx, dy = self.increments[0] #   This is the increment for the next step of the ant
        #   The modulus COLS and modulus ROWS is to ensure the cells don't leave screen's boundaries
        self.x = (self.x + dx) % self.app.COLS
        self.y = (self.y + dy) % self.app.ROWS



class App:
    def __init__(self, WIDTH=1200, HEIGHT=675, CELL_SIZE=4):
        pg.init()
        self.screen = pg.display.set_mode([WIDTH, HEIGHT])
        self.clock = pg.time.Clock()
        
        self.CELL_SIZE = CELL_SIZE
        self.ROWS, self.COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
        self.grid = [[0 for col in range(self.COLS)] for row in range(self.ROWS)]

        ##   First ant
        # self.ant = Ant(app=self, pos=[self.COLS // 2, self.ROWS // 2], color=pg.Color('orange'))
        ##   List of ants
        self.ants = [Ant(self, [randrange(self.COLS), randrange(self.ROWS)], self.get_color()) for i in range(13)]
    
    @staticmethod
    def get_color():
        """
            To distinguish between ants, this static method obtains a random value for each color channel
        """
        channel = lambda: randrange(30, 220)
        return channel(), channel(), channel()

    def run(self):
        while True:
            # self.ant.run()
            [ant.run() for ant in self.ants]


            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.flip()
            self.clock.tick()


if __name__ == "__main__":
    app = App()
    app.run()
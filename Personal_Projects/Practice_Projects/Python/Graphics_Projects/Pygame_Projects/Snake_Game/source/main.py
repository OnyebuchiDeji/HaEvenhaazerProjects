import pygame as pg
from game_objects import *
import sys

class Game:
    def __init__(self):
        pg.init()
        self.WINDOW_SIZE = 650
        self.TILE_SIZE = 50
        self.screen = pg.display.set_mode([self.WINDOW_SIZE] * 2)
        self.clock = pg.time.Clock()
        self.fps = 60
        self.new_game()

    def draw_grid(self):
        ##  Create vertical and horizontal lines
        [pg.draw.line(self.screen, [50] * 3, (x, 0), (x, self.WINDOW_SIZE))
                                for x in range(0, self.WINDOW_SIZE, self.TILE_SIZE)]
        [pg.draw.line(self.screen, [50] * 3, (0, y), (self.WINDOW_SIZE, y))
                                for y in range(0, self.WINDOW_SIZE, self.TILE_SIZE)]

    def new_game(self):
        self.snake = Snake(self)
        self.food = Food(self)

    def update(self):
        self.snake.update()
        pg.display.flip()
        self.clock.tick(self.fps)
    
    def draw(self):
        self.screen.fill("black")
        self.draw_grid()
        self.snake.draw()
        self.food.draw()

    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            #   Snake contol
            self.snake.control(event)

    def run(self):
        while True:
            self.check_event()
            self.update()
            self.draw()

if __name__=="__main__":
    game = Game()
    game.run()
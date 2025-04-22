import pygame as pg
import sys
from random import randint

WIN_SIZE = 660
CELL_SIZE = WIN_SIZE // 3
INF = float("inf")
vec2 = pg.math.Vector2

CELL_CENTER = vec2(CELL_SIZE / 2)

"""
    Game Logic, Elab:

    The playing field is a 2D array, of rows and columns.
    Each cell will have infinity values or null
    The number 1 will be an X and 0 an O

    So by filling the array with 1s and 0s, it will ensure the game logic works well
"""



##  Class with main logic of the game

class TicTacToe:
    def __init__(self, game):
        self.game = game
        self.field_image = self.get_scaled_image(path="resources/field.png", res=[WIN_SIZE]*2)
        self.O_image = self.get_scaled_image(path="resources/o.png", res=[CELL_SIZE]*2)
        self.X_image = self.get_scaled_image(path="resources/x.png", res=[CELL_SIZE]*2)

        ## The game field
        self.game_array = [
            [INF, INF, INF],
            [INF, INF, INF],
            [INF, INF, INF],
        ]

        ## Which player will go first by random
        self.player = randint(0, 1)

        ##  To determine winner!
        """"""
        ##  An array of indices of each line being checked for striking
        ##  It is (col, row)
        self.line_indices_array = [
            ##  Horizontal top
            [(0, 0), (0, 1), (0, 2)],
            ##  Horizontal second row
            [(1, 0), (1, 1), (1, 2)],
            #   Horizontal Third row
            [(2, 0), (2, 1), (2, 2)],
            # Vertical first column
            [(0, 0), (1, 0), (2, 0)],
            # Vertical second column
            [(0, 1), (1, 1), (2, 1)],
            # Vertical third column
            [(0, 2), (1, 2), (2, 2)],
            # Diagonal negative slope from left
            [(0, 0), (1, 1), (2, 2)],
            # Diagonal positive slope from right
            [(0, 2), (1, 1), (2, 0)],
        ]
    
        self.winner = None
        self.game_steps = 0

        self.font = pg.font.SysFont("Verdana", CELL_SIZE // 4 , True)

    def check_winner(self):
        ##  Iterate over the list of indices of all lines, checking each of their cells' values.
        ##  and finding the sum. If it adds up to 3 or 0, then the player wins.

        for line_indices in self.line_indices_array:
            sum_line = sum([self.game_array[i][j] for i, j in line_indices])
            ##  Only if the sum is either 0 or 3
            if sum_line in (0, 3):
                ##  If sum_line is 0, sum_line==0 evaluates to 1
                ##  SO "O" will be selected.
                ##  Else, "X"
                self.winner = "XO"[sum_line==0]
                ##  Getting the coordinates of the line
                self.winner_line = [vec2(line_indices[0][::-1])*CELL_SIZE + CELL_CENTER,
                                    vec2(line_indices[2][::-1])*CELL_SIZE + CELL_CENTER]

    def run_game_process(self):
        ##  Coordinates of mouse position by size of cell will give the indexes of the array at that point 
        current_cell = vec2(pg.mouse.get_pos()) // CELL_SIZE
        col, row = map(int, current_cell)
        ##  This returns three boolean values as a Tuple
        left_click = pg.mouse.get_pressed()[0]

        ##  If the left mouse is clicked and the cell at the specified index has a value
        ##  ...and there is no winner...
        if  left_click and self.game_array[row][col] == INF and not self.winner:
            self.game_array[row][col] = self.player
            ##  Since player has successfully played, switch them
            self.player = not self.player
            self.game_steps += 1
            self.check_winner()
    
    def draw_objects(self):
        ##  For every row
        for y, row in enumerate(self.game_array):
            ##  For every column
            for x, obj in enumerate(row):
                ##  If object is not infinity
                if obj != INF:
                    ##  Blit the corresponding picture based on its value of obj
                    ##  1 - true, 0 - false
                    self.game.screen.blit(self.X_image if obj else self.O_image, vec2(x, y) * CELL_SIZE)

    def draw_winner_line(self):
        if self.winner:
            pg.draw.line(self.game.screen, "red", *self.winner_line, CELL_SIZE//8)
            label = self.font.render(f"Player '{self.winner}' wins!", True, "white", "black")
            self.game.screen.blit(label, (WIN_SIZE // 2 - label.get_width() // 2, WIN_SIZE//4))
    
    def draw(self):
        self.game.screen.blit(self.field_image, (0, 0))
        self.draw_objects()
        self.draw_winner_line()

    @staticmethod
    def get_scaled_image(path, res):
        img = pg.image.load(path)
        return pg.transform.smoothscale(img, res)
    
    def print_caption(self):
        ##  TO show which player goes first!
        pg.display.set_caption(f"Player '{"OX"[self.player]}' turn!")
        if self.winner:
            pg.display.set_caption(f"Player '{self.winner}' wind! Press SPace to Restart!")
        ##  Every cell is full so no winners
        elif self.game_steps==9:
            pg.display.set_caption(f"Game Over! Press Space to Restart!")


    def run(self):
        self.print_caption()
        self.draw()
        self.run_game_process()




class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode([WIN_SIZE] * 2)
        self.clock = pg.time.Clock()
        self.tic_tac_toe = TicTacToe(self)

    def new_game(self):
        self.tic_tac_toe = TicTacToe(self)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.new_game()
    

    def run(self):
        while True:
            self.tic_tac_toe.run()
            self.check_events()
            pg.display.update()
            ##  Frames per second
            self.clock.tick(60)


if __name__=="__main__":
    game = Game()
    game.run()
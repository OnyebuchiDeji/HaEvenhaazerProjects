import pygame as pg
from random import choice

"""
    the implmentation of the depth-first search requires the use of a Stack datatype
    1.  Makde area
    2.  Made cells
    3.  Made grid with borders
    4.  Implemented checking for a cell and then selecting a neighbor to become the
        current cell by random
    5.  Implemented removing cell wall when the current cell moves to the next cell,
        to build the path of the maze.
    6.  The maze making cell stops moving after the cells around it (neighbors) have been visited already, so
        there was nowhere to go.
        Solution was to implement a stack in which every visited cell is written to. Then when there is nowhere to go,
        the current_cell will take steps back using the visited cells' positions from the stack being popped until it 
        reaches a position where there are neighbors to visit, so that one can traverse the entire 2d area/field
    7. Added some color trails to show where the maze-maker has visited, and it is then removed when maze is complete.

"""

RES = WIDTH, HEIGHT = 1200, 650
TILE = 25
cols, rows = WIDTH // TILE, HEIGHT // TILE


pg.init()
sc = pg.display.set_mode(RES)
clock = pg.time.Clock()

class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {'top':True,'right':True, 'bottom': True, 'left': True}
        self.visited  = False
    
    def draw_current_cell(self):
        ##  Identify current cell.
        x, y = self.x * TILE, self.y * TILE
        pg.draw.rect(sc, pg.Color('saddlebrown'), (x + 2, y + 2, TILE -2, TILE - 2))

    def draw(self):
        ##  Multiplying because x and y are passed in as 0 1, 2, 3, 4
        ##  Hence each consecutive is 100 units wide in both width and height
        x, y = self.x * TILE, self.y * TILE

        if self.visited:
            #   Paint black
            pg.draw.rect(sc, pg.Color("black"), (x, y, TILE, TILE))

        if self.walls['top']:
            pg.draw.line(sc, pg.Color('darkorange'), (x, y), (x + TILE, y), 2)
        if self.walls['right']:
            pg.draw.line(sc, pg.Color('darkorange'), (x + TILE, y), (x + TILE, y + TILE), 2)
        if self.walls['bottom']:
            pg.draw.line(sc, pg.Color('darkorange'), (x + TILE, y + TILE), (x , y + TILE), 2)
        if self.walls['left']:
            pg.draw.line(sc, pg.Color('darkorange'), (x, y + TILE), (x , y), 2)
        
    def check_cell(self, x, y):
        find_index = lambda x, y: x + y * cols
        ##  Check that cell does not go beyond the edges of the field
        if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
            return False
        return grid_cells[find_index(x, y)]
    
    def check_neighbours(self):
        """
            This gets the neighbors of the current cell
            then checks if that neighbor is an actual cell and not a boundary
            if the neighbour is a cell, th ecurrent cell appends it to its list
            of neighbors.
            And then it chooses any of the neighbours to go to randomly with `choice()`
        """
        neighbors = []
        top = self.check_cell(self.x, self.y - 1)
        right = self.check_cell(self.x + 1, self.y)
        bottom = self.check_cell(self.x, self.y + 1)
        left = self.check_cell(self.x - 1, self.y)
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)

        ##  If list is empty, return False
        return choice(neighbors) if neighbors else False


def remove_walls(current, next):
    # dx and dy can only either give 1 or -1, depending on which cell is higer or ahead of which
    dx = current.x - next.x
    if dx == 1:
        current.walls['left'] = False
        next.walls['right'] = False
    elif dx == -1:
        current.walls['right'] = False
        next.walls['left'] = False
    
    dy = current.y - next.y
    if dy == 1:
        current.walls['top'] = False
        current.walls['bottom'] = False
    elif dy == -1:
        current.walls['bottom'] = False
        next.walls['top'] = False


##  Cell Grid
grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)]
current_cell = grid_cells[0]
stack = []
colors, color = [], 40


while True:
    sc.fill(pg.Color('darkslategray'))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    
    ##  Draw grid
    [cell.draw() for cell in grid_cells]
    current_cell.visited = True
    current_cell.draw_current_cell()
    ##  Drawing round-edged, varying colored cells to represent trails for where the maze-maker has passed
    [pg.draw.rect(sc, colors[i], (cell.x * TILE + 5, cell.y * TILE + 5,
                                  TILE - 10, TILE - 10), border_radius=12) for i, cell in enumerate(stack)]

    ##  Here, it can be seen that there is a random movement
    next_cell = current_cell.check_neighbours()
    if next_cell:   ##  If next cell
        next_cell.visited=True
        stack.append(current_cell)
        ##  For trails
        colors.append((min(color, 255), 10, 100))
        ##  Making small colour gradient
        color += 1
        remove_walls(current_cell, next_cell)
        current_cell = next_cell
    elif stack: #   If no next cell (all neighbors have been visited)
        current_cell = stack.pop()

    

    pg.display.flip()
    clock.tick(30)

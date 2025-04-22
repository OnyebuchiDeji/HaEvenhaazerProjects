import pygame as pg
import math
from Zekerai import HopfieldN1
"""
    This provides the interface with the Hopfield System.

    1.  It provides the graphics and input system for input of patterns to save.
    2.  It allows one to save them and press a button to construct the Hopfield structure.
    3.  then after saving another button is clicked to enter the test input that is to be transformed
        to any stored in the memory system. 
    4.  Then it does its worl and for every iteration displays live 
"""

# class Cell:
#     """
#         Constituent object of Grid
#     """
#     def __init__(self):
#         ...
#     def __call__(self, surf, x, y, size, colForm):
#         match (colForm):
#             case -1:
#                 pg.draw.rect(surf, (108, 108, 108), (x, y, size, size), width=0, border_radius=-1)
#             case 1:
#                 pg.draw.rect(surf, (8, 8, 8), (x, y, size, size), width=0, border_radius=-1)

        
def draw_cell(surf: pg.Surface, x:float, y:float, size:int, colForm:int):
    match (colForm):
        case -1:
            pg.draw.rect(surf, (126, 126, 126), (x, y, size, size), width=0, border_radius=-1)
        case 1:
            pg.draw.rect(surf, (8, 8, 8), (x, y, size, size), width=0, border_radius=-1)

        
class Grid:
    """
        Consists of Cells.
        *   This data structure allows one to modify the structure that represents a grid,
        so it can be easily passsed to the Hopfield Network for processing.
        *   Then the modified grid array by the Hopfield network is passed back to this Grid
            so it renders its cells differently.
        
        Array:
        *   It's a 1D array
        *   This is what is interpreted to render specific colors for each cell.
        *   It's basically an array of pixels' color values.
        *   It doesn't store positions of a cell. Cells are displayed in succession
            starting from top left corner of grid area, row by row.
        *   -1 ==> grey color
            +1 ==>  black color

    """
    def __init__(self, surf, dimensions:tuple[float, float], colsNrows:tuple[int, int], cellSize:int, winDimensions):
        self.surf = surf
        self.win_width, self.win_height = winDimensions
        self.width, self.height = dimensions
        self.cell_size = cellSize
        self.cols, self.rows = colsNrows
        self.inputs : list[list[int]] = []
        self.noisy_input: list[int] = []
        self.current_array: list[int] = []
        self.max_inputs = 3
        self.noisy_input_set = False

        ##  Flag to update the current array
        ##  It is checked to see if the Hopfield
        ##  has started modifying the current array of the Grid
        ##  to display the results of its processing.
        self.update_flag = False

        self._oninit_current_array()

        #   Threshold value was gotten by trial and error
        self.mouse_touch_threshold = 12
        self.mouse_touch_counter = 0
        self.grid_gen = None
    
    def _oninit_current_array(self):
        for i in range(self.cols * self.rows):
            self.current_array.append(-1)
        
    def new_noise_input(self):
        """
            This only removes the onld noise input
            It doesn't clear the inputs used to get the Hopfield weights
        """
        self.noisy_input.clear()
        self.noisy_input_set = False
        self.update_flag = False
        self._reset_current_array()
        
    def clear_inputs(self):
        """
            This empties the array of inputs
            so new inputs can be entered.
        """
        self.inputs.clear()
        self.noisy_input.clear()
        self.noisy_input_set = False
        self.update_flag = False
        self._reset_current_array()

    def _reset_current_array(self):
        """
            It's called when a current grid is saved, so the array
            is 'emptied' so the user can enter a new set of color inputs.
            Its not actually emptied but rather tje current_array's values
            are reset to the value -1.
        """
        for i in range(len(self.current_array)):
            self.current_array[i] = -1
        # print("Length of Current Array After Reset:", len(self.current_array))
        # print("Current Array After Reset:", self.current_array)

    def _normalize_mouse_pos(self, mouse_pos: tuple[int, int]):
        """
            This normalizes the mouse position to the grid space
        """
        mx = min(max(0.1, (mouse_pos[0] - self.win_width / 2) + self.width/2), self.width)
        my = min(max(0.1, (mouse_pos[1] - self.win_height / 2) + self.height/2), self.height)
        print("Norm X, Y:", mx, my)
        return (mx, my)

    def _get_clicked_cell(self, click_pos: tuple[int, int]) -> int:
        """Logic for getting clicked cell"""
        ##  factor of grid width / click position x
        fx = self.width / click_pos[0]
        ##  factor of grid height / click position y
        fy = self.height / click_pos[1]
        # print("fx, fy: ", fx, fy)

        #   Get corresponding factor based on num of cols and rows
        #   in 2D array grid
        x2d = math.ceil(self.cols / fx) - 1
        y2d = math.ceil(self.rows / fy) - 1

        # print("X2d, Y2d: ", x2d, y2d)

        #   calculate the 1D index of that 2D array position
        index = x2d + y2d * self.cols
        # print("1D Index: ", index)
        return index


    def update_cell(self):
        """
            Runs continually.
            It checks for a mouse click.
            It checks the position the moise was clicked in
            If that position is on a Cell in the grid.
            It changes the cell's color between white and gray by changing
            the color value of the Cell's corresponding position in the array.
        """

        ##  .get_pressed() takes either literal 3 or 5 as an argument
        ##  the number specifies what kind of mouse it is because
        ##  of how many inputs it can receive.
        ##  I use 3 since my mouse is normal
        ##  and index 0 [0] since I'm target the left mouse button 
        if not pg.mouse.get_pressed(3)[0]:
            return


        mouse_pos = 0, 0
        self.mouse_touch_counter += 1

        # while self.mouse_touch_counter < self.mouse_touch_threshold:
        #     self.mouse_touch_counter += 1
        if self.mouse_touch_counter < self.mouse_touch_threshold:
            return
        
        mouse_pos = self._normalize_mouse_pos(pg.mouse.get_pos())
        indexOfClickedCell = self._get_clicked_cell(mouse_pos)

        print("Clicked: ", indexOfClickedCell)
        current_val = self.current_array[indexOfClickedCell]

        if current_val == 1:
            self.current_array[indexOfClickedCell] = -1
        else:
            self.current_array[indexOfClickedCell] = 1

        self.mouse_touch_counter = 0
        

    def save_current_array(self):
        """
            It saves the current array to the array of inputs.
            After `max_inputs` inputs have been entered, this
            no longer adds arrays to the input.
            It waits for the inputs to be sent to the Hopfield
            and can only be reset by a special button.
            It calls _reset_current_array() at the end.
        """
        if len(self.inputs) >= self.max_inputs:
            print("Maximum Inputs have been entered.")
            return
        
        # print("Current Array:", self.current_array)
        #   Ensure to make a copy, lest a bug arrises when current_array is changed.
        self.inputs.append(list(self.current_array))
        print("Saved Input:", self.current_array)
        self._reset_current_array()

    def save_noisy_input(self):
        if self.noisy_input_set:
            return

        #   Ensures to make a copy
        self.noisy_input = list(self.current_array)
        print("Saved Noisy Input:", self.noisy_input)
        self.noisy_input_set = True
        

    def update_current_array(self, newArr: list[int]):
        """
            It is called when the Hopfield is 'remembering'
            a previously stored input.
            It continually modifies the current array to show the update
            done by the Hopfield live.
        """
        ##  Ensures to make a copy.
        self.current_array = list(newArr)
    
    
    def render(self):
        """
            renders the current_array to show which array
            is currently being modified.
        """
        self.update_cell()
        target_index = 0
        for row in range(self.rows):
            for col in range(self.cols):
                target_index = col + row * self.cols
                # print("target index: ", target_index)
                draw_cell(self.surf, col * self.cell_size,
                    row * self.cell_size, self.cell_size,
                        self.current_array[target_index])



class App:
    def __init__(self):
        self.win_width, self.win_height = 720, 405
        self.grid_arx, self.grid_ary = 7, 9
        self.cell_size = 40
        self.grid_width, self.grid_height = self.grid_arx * self.cell_size, self.grid_ary * self.cell_size

        self.window = pg.display.set_mode((self.win_width, self.win_height))
        self.grid_surf = pg.Surface((self.grid_width, self.grid_height))

        pg.display.set_caption("Artificial Memory - The Hopfield")
        self.clock = pg.time.Clock()
        self.fps = 60

        self.stop = False
        self.grid = Grid(self.grid_surf, (self.grid_width, self.grid_height),
                        (self.grid_arx, self.grid_ary), self.cell_size,
                        (self.win_width, self.win_height))
        self.hopfield = HopfieldN1()

    def run(self):
        """Main Loop and Key Callbacks"""
        while not self.stop:
            for e in pg.event.get():
                if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                    self.stop = True
                if e.type == pg.KEYDOWN:
                    if e.key == pg.K_s:
                        self.grid.save_current_array()
                    if e.key == pg.K_n:
                        self.grid.save_noisy_input()
                    if e.key == pg.K_c:
                        self.grid.clear_inputs()
                        self.hopfield.reset()
                    if e.key == pg.K_k:
                        self.grid.new_noise_input()
                    if e.key == pg.K_r:
                        #   Runs the HopfieldAlgo
                        #   and switches flag to display changing current_array
                        self.hopfield.oninit(self.grid.inputs)
                        self.grid.update_flag = True

                        self.grid_gen = self.hopfield.retrieve_pattern_v2(self.grid.noisy_input)
                    

            if self.grid.update_flag:
                # print("Noisy Input Length:", len(self.grid.noisy_input))
                
                # self.grid.noisy_input = next(self.hopfield.retrieve_pattern(self.grid.noisy_input))
                try:
                    self.grid.noisy_input = next(self.grid_gen)
                except StopIteration:
                    print("Finished Revising!")
                self.grid.update_current_array(self.grid.noisy_input)
            
            self.render_grid()
            pg.display.update()
            self.clock.tick(self.fps)

        
    def render_grid(self):
        """Creates Grid to interact with"""
        # self.grid_surf.fill((0, 0, 0))
        self.window.fill('grey')

        # draw_cell(self.grid_surf, 0, 0, self.cell_size, -1)
        self.grid.render()

        center_w = self.win_width/2 - self.grid_width /2
        center_h = self.win_height/2 - self.grid_height /2
        self.window.blit(self.grid_surf, (center_w, center_h))


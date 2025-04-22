import pygame as pg
from random import randrange


"""
    1. At first, when the `move()` method was made using the `rect.move_ip()`
    the rect was moving too fast, according to the number of frames.
    2. Added time delay between frames for motion
    3. Added controls to change direction of motion.
    4. Fully implemented the random position of Snake on restart and Food object's random position
    5. Added Snake-Food interaction
    6. Added border collision to restart
    7. Added self-eating rule'
    8.  Prevented snake from moving on the opposite direction without turning properly
            E.g: left then right
    """
vec2 = pg.math.Vector2


class Snake:
    def __init__(self, game):
        self.game = game
        self.size = game.TILE_SIZE
        self.rect = pg.rect.Rect([0, 0, game.TILE_SIZE - 2, game.TILE_SIZE - 2])
        self.rect.center = self.get_random_position()
        # self.direction = vec2(self.size, 0)
        self.direction = vec2(0, 0)
        self.step_delay = 100 #milliseconds
        self.time = 0
        self.length = 1
        self.segments = []
        ##  Acts as the move controls permission
        self.directions = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}

    def control(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and self.directions[pg.K_w]:
                self.direction = vec2(0, -self.size)
                ##  Then they are re-written based on which key is being pressed
                self.directions = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d: 1}

            if event.key == pg.K_s and self.directions[pg.K_s]:
                self.direction = vec2(0, self.size)
                ##  Then they are re-written based on which key is being pressed
                self.directions = {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}

            if event.key == pg.K_a and self.directions[pg.K_a]:
                self.direction = vec2(-self.size, 0)
                ##  Then they are re-written based on which key is being pressed
                self.directions = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 0}

            if event.key == pg.K_d and self.directions[pg.K_d]:
                self.direction = vec2(self.size, 0)
                ##  Then they are re-written based on which key is being pressed
                self.directions = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0, pg.K_d: 1}


    def delta_time(self):
        ##  This simply gets the time spent for that frame
        ##  any time the time spent has passed the set limit/delay
        ##  the True is returned. This is used in the move() method
        ##  to ensure the time delay is spent before the rect moves
        time_now = pg.time.get_ticks()
        if time_now - self.time > self.step_delay:
            self.time = time_now    ##  self.time stores the time for from the previous frame (or iteration)
            return True
        return False
        
    def get_random_position(self):
        ##  Between half its size (left edge tile of screen) and ( the right edge tile)
        ##  Stepping by its size in both x and y hence *2 
        return [randrange(self.size // 2, self.game.WINDOW_SIZE - self.size // 2,
                          self.size)] * 2

    def check_borders(self):
        ##  If the snake goes past the borser, restart the game
        if self.rect.left < 0 or self.rect.right > self.game.WINDOW_SIZE:
            self.game.new_game()
        if self.rect.top < 0 or self.rect.bottom > self.game.WINDOW_SIZE:
            self.game.new_game()

    def check_food(self):
        """
            Compare snake's position to food's position
            if equal, change food's position to random
        """
        if self.rect.center == self.game.food.rect.center:
            self.game.food.rect.center = self.get_random_position()
            self.length += 1

    def check_selfeating(self):
        """
            Comparing the length of the segments with the lenght of the set
            composed by the coordinates of the segments.
            if the snake ran over itself, the length of the set will be different
            since the set contains only unique elments in duplicated coordinates to 
            reduce its length.
            My explanation:
                If the length of segments in the list is not equal to the length of
                of the centers of each item but put in a set, that means it has collided with
                itself because...
                    1. Sets remove duplicate items, and not that it is the item's centers
                        used to initialize the set.
                        so if there is a collision with itself, one mor more items will have the same
                        center, hence, putting it in a Set will remove that item, as Sets
                        only keep unique instances of items.
                        Hence the length of the Set will be less, thus the condition is True
         """
        if len(self.segments) != len(set(segment.center for segment in self.segments)):
            self.game.new_game()

    def move(self):
        if self.delta_time():
            self.rect.move_ip(self.direction)    
            self.segments.append(self.rect.copy())
            ##  The below slices the list along the length of the snake  
            self.segments = self.segments[-self.length:]

    def update(self):
        self.check_selfeating()
        self.check_borders()
        self.check_food()
        self.move()

    def draw(self):
        [pg.draw.rect(self.game.screen, 'green', segment) for segment in self.segments]


class Food:
    def __init__(self, game):
        self.game = game
        self.size = game.TILE_SIZE
        self.rect = pg.rect.Rect([0, 0, game.TILE_SIZE - 2, game.TILE_SIZE - 2])
        self.rect.center = self.game.snake.get_random_position()

    def draw(self):
        pg.draw.rect(self.game.screen, 'red', self.rect)
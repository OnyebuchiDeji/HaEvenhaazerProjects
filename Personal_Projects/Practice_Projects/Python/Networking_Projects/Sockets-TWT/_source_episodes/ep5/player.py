"""
    Episode 5:
        Sending the Player data as a pickle-serialized object.
"""

import pygame as pg

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height) 
        self.vel = 5
    
    def draw(self, win):
        """Draw Rectangle that represents the character"""
        pg.draw.rect(win, self.color, self.rect)
    

    def update_pos(self, x, y):
        self.x = x
        self.y = y
        self.update_rect()

    def update_rect(self):
        self.rect = (self.x, self.y, self.width, self.height)

    def move(self):
        """
            Checks Key Presses and Moves Accordingly
            Using `pg.keys.get_pressed()` allows you to check more than one key at once to perform an action.
            wso actions that require more than one keys can be done.
        """
        #   Gives a Dict of keys
        #   Each key can have a value of either zero (Not Pressed) or one (Pressed)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.x -= self.vel

        if keys[pg.K_RIGHT]:
            self.x += self.vel

        if keys[pg.K_UP]:
            self.y -= self.vel

        if keys[pg.K_DOWN]:
            self.y += self.vel

        self.update_rect()


"""
    In this episode, the player was made.
"""

import pygame as pg



WIDTH, HEIGHT = 500, 500
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Client")

CLIENTNUMBER = 0

####################################################
##-------------------CLASSES----------------------##
####################################################

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
        pg.draw.rect(WIN, self.color, self.rect)
    
    def move(self):
        """
            Checks Key Presses and Moves Accordingly
            Using `pg.keys.get_pressed()` allows you to check more than one key at once to perform an action.
            wso actions that require more than one keys can be done.
        """
        #   Gives a Dict of keys
        #   Each key can have a value of either zero (Not Pressed) or one (Pressed)
        keys = pg.keys.get_pressed()
        if keys[pg.K_LEFT]:
            self.x -= self.vel

        if keys[pg.K_RIGHT]:
            self.x += self.vel

        if keys[pg.K_UP]:
            self.y -= self.vel

        if keys[pg.K_DOWN]:
            self.y += self.vel

        self.rect = (self.x, self.y, self.width, self.height)


####################################################
####################################################

def redraw_window(player: Player):
    WIN.fill("antiquewhite")
    player.draw(WIN)
    pg.display.update()


def main():
    run = True
    p1 = Player(50, 50, 100, 100, "cyan")
    clock = pg.time.Clock()


    #   Game Loop
    while run:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
        
        p1.move()
        redraw_window(p1)


if __name__ == "__main__":
    main()
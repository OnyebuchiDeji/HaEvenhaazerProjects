"""
    Episode 1:
        Creating the client side; setting up Pygame and creating the Player object
    
    Episode 2:
        Added server script
    
    Episode 3:
        Updating the Client Side

    Episode 4:
        Hooking the graphical client to server through the 'client_network' to send info back and fort

        Here, information is sent with strings, not objects.
"""



import pygame as pg
from client_network import Network


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
        print(self.rect)
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

####################################################
####################################################


def read_pos(string):
    string = string.split(",")
    return int(string[0]), int(string[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])



def redraw_window(p1: Player, p2: Player):
    WIN.fill("antiquewhite")
    p1.draw(WIN)
    p2.draw(WIN)
    pg.display.update()


def main():
    run = True
    ##  Connect to the server
    ##  Enter the ip address used by server script
    client_net_obj = Network("10.240.120.2", 5555)
    start_pos:tuple[int, int] = read_pos(client_net_obj.get_pos())

    p1 = Player(start_pos[0], start_pos[1], 100, 100, (255, 0, 0))
    p2 = Player(0, 0, 100, 100, (109, 26, 255))

    clock = pg.time.Clock()


    #   Game Loop
    while run:
        clock.tick(60)

        ##  Note that p1 refers to the current client player
        ##  So it is p1 that is being updated by each client and hence
        ##  needs to be sent.
        p2_pos = read_pos(client_net_obj.send(make_pos((p1.x, p1.y))))
        p2.update_pos(p2_pos[0], p2_pos[1])

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
        
        p1.move()
        redraw_window(p1, p2)


if __name__ == "__main__":
    main()
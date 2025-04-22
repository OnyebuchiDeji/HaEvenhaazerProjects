"""
    Episode 5:
        Sending objects with Pickle library
"""



import pygame as pg
from client_network import Network
from player import Player


WIDTH, HEIGHT = 500, 500
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Client")

CLIENTNUMBER = 0

####################################################
##-------------------CLASSES----------------------##
####################################################

####################################################
####################################################


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

    p1: Player = client_net_obj.get_instance()

    clock = pg.time.Clock()

    #   Game Loop
    while run:
        clock.tick(60)
        ##  Note that p1 refers to the current client player
        ##  So it is p1 that is being updated by each client and hence
        ##  needs to be sent.
        p2 = client_net_obj.send(p1)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
        
        p1.move()
        redraw_window(p1, p2)


if __name__ == "__main__":
    main()
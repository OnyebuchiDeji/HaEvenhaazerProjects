"""
    Episode 6-9: Rock Paper Scissors Game
"""

import sys

import pygame as pg
import pickle

from client_network import Network

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game

pg.font.init()


WIDTH, HEIGHT = 700, 700

WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Client")


class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100
    
    def draw(self, win):
        pg.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pg.font.SysFont("bangers", 40)
        text = font.render(self.text, 1, (255, 255, 255))
        win.blit(text, (self.x + round(self.width / 2) - round(text.get_width() / 2),
                        self.y + round(self.height / 2) - round(text.get_height() / 2)))
    
    def clicked(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False



def redraw_window(win, game: 'Game', player: int):
    win.fill("antiquewhite")
    
    if not game.connected():
        font = pg.font.SysFont("bangers", 50)
        text = font.render("Waiting for Player...", 1, (255, 12, 170))
        win.blit(text, (WIDTH / 2 - text.get_width() /2, HEIGHT / 2 - text.get_height() / 2))
    else:
        font = pg.font.SysFont("bangers", 50)
        text = font.render("Your Move", 1, (26, 207, 207))
        win.blit(text, (80, 200))

        text = font.render("Opponent", 1, (26, 207, 207))
        win.blit(text, (380, 200))

        ##  Now To Draw the Actual Names of the Move
        ##  Now the Other Player Cannot Know what the Current Player's
        ##  Move is until they both make a move. 

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)
        if game.both_went():    #   If both players have played, show their moves
            text1 = font.render(move1, 1, (0, 0, 0))
            text2 = font.render(move2, 1, (0, 0, 0))
        else:
            #   If player 1 has gone and the current player is player 1
            if game.p1_went and player == 0:
                text1 = font.render(move1, 1, (0, 0, 0))
            elif game.p1_went:
                text1 = font.render("Locked In", 1, (0, 0, 0))
            else:
                #   If p1 (the current client) hasn't moved yet
                text1 = font.render("Waiting ..", 1, (0, 0, 0))

            if game.p2_went and player == 1:
                text2 = font.render(move2, 1, (0, 0, 0))
            elif game.p2_went:
                text2 = font.render("Locked In", 1, (0, 0, 0))
            else:
                #   If p1 (the current client) hasn't moved yet
                text2 = font.render("Waiting ..", 1, (0, 0, 0))
            
        #   Blit to Screen
        if player == 1:
            win.blit(text2, (100, 350))
            win.blit(text1, (400, 350))
        else:
            win.blit(text1, (100, 350))
            win.blit(text2, (400, 350))
            
        for btn in btns:
            btn.draw(win)

    pg.display.update()



                


        

btns = [Button("Rock", 50, 500, (120, 64, 196)),
        Button("Scissors", 250, 500, (209, 26, 0)),
        Button("Paper", 450, 500, (255, 209, 209))]


def main():
    run = True

    clock = pg.time.Clock()
    client_net_obj = Network("10.240.120.2", 5555)

    player = int(client_net_obj.get_player_id())
    print("You are Player ", player)

    while run:
        clock.tick(60)
        try:
            #   It's in a try block so that if the game to be gotten
            #   does not exist, no response comes from the server
            game: Game = client_net_obj.send("get")
        except:
            #   So exit out of this game, go to the main menu that enables
            #   one to choose a new again
            run = False
            print("Couldn't Get a Game")
            break
            
        if game.both_went():
            pg.time.delay(500)
            redraw_window(WIN, game, player)
            pg.time.delay(200)
            try:
                #   To enable the next round
                game = client_net_obj.send("reset")
            except:
                run = False
                print("Couldn't Get a Game")
                break
            
            #   Now display message of winner.
            font = pg.font.SysFont("bangers", 90)
            if game.winner() == 1 and player == 1 or game.winner() == 0 and player == 0:
                text = font.render("You Won!", 1, (206, 12, 220))
            elif game.winner() == -1:
                text = font.render("Tie!", 1, (220, 12, 206))
            else:   ##  No win nor tie
                text = font.render("You Lost...", 1, (220, 30, 220))
            
            WIN.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
            pg.display.update()
            pg.time.delay(2000)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                sys.exit()
            
            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                #   For every button, check if it was clicked.
                #   If clicked, do something
                for btn in btns:
                    #   to not let one click the "Rock" "Paper" "Scissors"
                    #   buttons when the game is not connected
                    if btn.clicked(pos) and game.connected():
                        if player == 0:
                            if not game.p1_went:
                                #   The button's text is the name of the moved
                                #   which is processed on the client side
                                client_net_obj.send(btn.text)
                        else:
                            if not game.p2_went:
                                client_net_obj.send(btn.text)
        
        redraw_window(WIN, game, player)

def menu_screen():
    run = True
    clock = pg.time.Clock()

    while run:
        clock.tick(60)
        WIN.fill("grey")
        font = pg.font.SysFont("bangers", 60)
        text = font.render("Click to Play!", 1, (25, 12, 25)) 
        WIN.blit(text, (WIDTH/2 - text.get_width() /2, HEIGHT / 2 - text.get_height()))
        pg.display.update()
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                run = False
    main()

if __name__ == "__main__":
    menu_screen()

"""
    Episode 6: Rock Paper Scissors Game
"""

import socket
import threading
from game import Game

server = "10.240.120.2"
port = 5555

socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket_obj.bind((server, port))
except socket.error as e:
    print(str(e))


socket_obj.listen(2)
print("Server Started; Now Waiting For Connection from Clients!")

g_CONNECTED = set()     #   Stores the IPS of the connected clients
g_GAMES = {}            #   Stores All Games based on their IDS
g_IDCOUNT = 0           #   Keeps track of the current id

def threaded_client(conn, player_id, game_id):
    ...


while True:
    conn, addr = socket_obj.accept()
    print("Server Connected to Client at Address: ", addr)


    g_IDCOUNT += 1
    p = 0
    #   The below keeps track of the game_id and ensures that only 2 people can connect
    #   to a game.
    #   Scenario: After two clients connect, game_id will still be 0.
    #   A Game is only for *Two People*.
    #   Then when the third and fourth connect, their game_id will be 1
    #   and so on.
    game_id = (g_IDCOUNT - 1) // 2
    if g_IDCOUNT % 2 == 1:
        g_GAMES[game_id] = Game(game_id)
        print("Creating a New Game...")
    else:
        #   This ensures that when a Game is not yet full (hasn't gotten
        #   two participants yet, just 1), ensure that the next person to
        #   connect joins the pending Game
        g_GAMES[game_id].ready = True
        p = 1




    threading.Thread(target=threaded_client, args=(conn,)).start()

"""
    Episode 6-9: Rock Paper Scissors Game
"""

import socket
import threading
import pickle

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
    """
        Runs for each client that connects
    """
    #   To be able to modify the Global variable, g_IDCOUNT
    global g_IDCOUNT, g_GAMES

    #   Make First Connection
    conn.send(str.encode(str(player_id)))
    reply = ""
    while True:
        """
            Send one of three different options from these:
                GET, RESET, MOVE
            GET: is sent every frame; to get the current state of the Game
                of the game_id from the server
            RESET:  Reset the game; the game has finished, both players played.
            MOVE:   When a Player, a Client makes a move, send to the Server
                to update the game accordingly and sends back the Game to the client
        """

        try:
            data = conn.recv(4096).decode()

            #   Check if the game still exists.
            #   so if one of the clients disconnects from the game...
            #   delete the Game and take other client back to Main Screen
            if game_id in g_GAMES:
                game: Game = g_GAMES[game_id]

                if not data:
                    break
                else:
                    ##   Now check the three options
                    ##  If the data is not "reset" and is not "get"
                    ##  then its to make a play ("R", "P", "S")
                    if data == "reset":
                        game.reset_went()
                    elif data != "get":
                        game.play(player_id, data)
                    
                    reply = pickle.dumps(game)
                    conn.sendall(reply)
            else:
                break    
        except:
            break
    
    #   Once the while loop is broken out of, close the game and delete it
    print("Lost Connection")
    """
        There is this try block because if both players disconnect at the same
        time, both will try to delete the same memory.
        If one deletes it and then the other, the latter will be trying to delete 
        memory that is already deleted.
        In that case, do nothing; make sure no Exception stops the program!
    """
    try:
        del g_GAMES[game_id]
        print(f"Closing Game of ID {game_id}")
    except:
        pass

    g_IDCOUNT -= 1
    conn.close()

while True:
    conn, addr = socket_obj.accept()
    print("Server Connected to Client at Address: ", addr)


    g_IDCOUNT += 1
    current_player = 0
    #   The below keeps track of the game_id and ensures that only 2 people can connect
    #   to a game.
    #   Scenario: After two clients connect, game_id will still be 0.
    #   A Game is only for *Two People*.
    #   Then when the third and fourth connect, their game_id will be 1
    #   and so on.
    game_id = (g_IDCOUNT - 1) // 2
    #   If its an odd number of players, create a new game
    if g_IDCOUNT % 2 == 1:
        g_GAMES[game_id] = Game(game_id)
        print("Creating a New Game...")
    else:   #   If its even, add that player.
        #   This ensures that when a Game is not yet full (hasn't gotten
        #   two participants yet, just 1), ensure that the next person to
        #   connect joins the pending Game
        g_GAMES[game_id].ready = True
        current_player = 1

    threading.Thread(target=threaded_client, args=(conn, current_player, game_id)).start()

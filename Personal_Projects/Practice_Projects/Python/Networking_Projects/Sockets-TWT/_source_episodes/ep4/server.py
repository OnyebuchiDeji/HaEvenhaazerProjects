"""
    Episode 1:
        Creating the client side; setting up Pygame and creating the Player object

    Episode 2:
        The server side is made.

    Episode 3:
        Update this.
        Added code to send an acknowledgment message after the client has connected
        in function `threaded_client`

    Episode 4:
        Hooking the graphical client to server through the 'client_network' to send info back and fort

        For Server: Added a global list to store the positions of the Players

"""
import socket
# from thread import *
import threading
import sys


"""
    For an app to connect to another app on another device via a network, it needs
    to connect to the port that its target app is running on.

    For that target app to be visible to its connector (connection source), it has to be "hosted"
    on a certain port.
    Every port is associated with a protocol it excels in; Ports are themselves System applications that
    accept connections.
    Connections can be of various protocols, e.g. HTTP, HTTPS, SMTP, FTP, etc. Hence why there are specific ports
    that excel in handling each unique connection.

    There are also "free" ports that are freee for users to run their custom app services on.
    These apps are free to use whatever kind of protocol; hence these ports work with the app receive and relay the incoming
    connections from outside unto that app.

    You know I said there are specific ports that "excel" in handling connections of specific protocols.
    I stand corrected: rather those protocols are made as a standard for businesses and companies so that
    apps they make that use a certain service will always utilize the same port for their users.
"""
##  Putting localhost means this app only able to connect to devices on one's local network.
##  So anything on the WiFi network that can see each other will work.
##  But once outside, the app cannot
server = "10.240.120.2"
port = 5555   #   A safe port to connect the server (running of this application) to


sock_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

##  Binding the connection/
try:
    sock_obj.bind((server, port))
except socket.error as e:
    print(str(e))


##   This opens up the port to allow multiple clients connect to it.
##  Adding a value as an argument: `sock_obj.listen(2)` runs the server more than once
sock_obj.listen(2)
print("Server Started; Waiting for a Connection.")

def read_pos(string: str):
    string = string.split(",")
    return int(string[0]), int(string[1])

def make_pos(tup: tuple):
    return str(tup[0]) + "," + str(tup[1])


##  Stores the positions of the players
g_POS = [(0, 0), (100, 100)]

def threaded_client(conn, addr, player_id):
    """What a connected client does"""

    ##  Send Starting Position based on Player Id
    conn.send(str.encode(make_pos(g_POS[player_id])))

    reply = ""
    while True:
        try:
            #   This takes the number of bits
            data: str = conn.recv(2048).decode()
            # reply = data.decode("utf-8")
            data = read_pos(data)
            g_POS[player_id] = data


            #   If no data is received, break; stop trying to receive
            if not data:
                print(f"{addr} Disconnected!")
                break
            else:
                ##  If it#s player 1, send reply of Player 0's data. Else send vice versa
                if player_id == 1:
                    reply = g_POS[0]
                else:
                    reply = g_POS[1]

                ##  Received data from cuurrent player
                print(f"Received from {addr}: ", data)
                ##  Sending position of other player
                print(f"Sending to {addr}: ", reply)
            
            ##  Encodes and sends the message sent to the Server from Client back to the Client
            conn.sendall(str.encode(make_pos(reply)))
        except:
            break
    
    print("Lost Connection.")
    conn.close()
        
current_player = 0

##  This while loop will continually wait for and receive a connection
while True:
    #   This waits here to receive a connection froom a client
    #   and stores the connection object and ip address of the connector
    conn, addr = sock_obj.accept()
    print("Connected to: ", addr)

    ##  This started thread runs independent of the main thread.
    threading.Thread(target=threaded_client, args = (conn, addr, current_player)).start()
    current_player += 1
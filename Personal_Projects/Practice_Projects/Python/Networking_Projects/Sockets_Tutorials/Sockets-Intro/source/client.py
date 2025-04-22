"""
    This is the client
"""

import socket as sckt
import random as rnd
"""
    This has to specify the ip that the server app uses.
    It must be that host regardless of which device runs this client script.
    But the above is only if that device running this client script is in the same LAN
    as the device running the server.

    But if it's not, this script should use as HOST the public IP of the device running the server
    app.
    This can be found out using web tools like 'myip.is'.

    A way is to use a while loop that only breaks when the right IP is gotten and the connection
    is established.
    First, it requests from a remote server the private IP of the server app. If they are both in the same
    LAN, the connection should work. But if not, it closes the failed connection and retries this time
    requesting via an API what the Public IP of that device that osts the server's app. 
"""


quotes = ["Bigger than Life", "The Mysteries Within", "The Belly of the Deep", "The Sea Clad with Swaddling Bands",
          "The Morning Stars", "Yo! This is Earth!", "The Song of Rejoicing", "The Strength in the Belly",
          "The Glory of the Son", "The Glory of Man", "The Glory of God", "A Refuge; A String Tower!",
          "The Stength of His Arm", "The Strength to Trust In", "The Safety of the Heart", "The Earth Hangs on What?",
          "The Ordinances of Heaven"]

   
HOST = '192.168.56.1'
PORT = 9047

#   Create the client's socket endpoint
socket = sckt.socket(sckt.AF_INET, sckt.SOCK_STREAM)

#   Connect to server via IP and PORT
socket.connect((HOST, PORT))
socket.send(rnd.choice(quotes).encode("utf-8"))
print(socket.recv(1024).decode("utf-8"))   #   utf-8 is default
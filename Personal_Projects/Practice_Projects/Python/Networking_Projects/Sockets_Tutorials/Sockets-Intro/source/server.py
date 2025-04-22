"""
    This tutorial demonstrates a TCP Socket.
    This server is a very simple test server.
    It cannot handle multiple client connections at once as it does not employ multi-threading.
    The various other tutorials like the Chat Apps cover this.

    Hence it is serial.
"""

import socket as sckt

#   Either add your local/private IP
# HOST = '10.240.109.117'
#   OR
"""
    This dynamically gets your IP address
    But it does not wor if you're using a virtual box

    sckt.gethostname() gives my device's name: LAPTOP-LPTFQ2O3
    sckt.gethostbyname() gives my device's IP info, specifically the Ethernet 4 not the LAN
    as below:

        Ethernet adapter Ethernet 4:
            Connection-specific DNS Suffix  . :
            Link-local IPv6 Address . . . . . : fe80::7329:609e:7546:491d%3
            IPv4 Address. . . . . . . . . . . : 192.168.56.1
            Subnet Mask . . . . . . . . . . . : 255.255.255.0
            Default Gateway . . . . . . . . . : 

    And it must take the device host name. 
"""
HOST = sckt.gethostbyname(sckt.gethostname())
# print(HOST)
#   Ensure the PORT is not a common one usually used by system services
PORT = 9047

#   The server socket
server = sckt.socket(sckt.AF_INET, sckt.SOCK_STREAM)
server.bind((HOST, PORT))
#   The number is how many connections to allow before rejecting new connections
server.listen(5)

client_id = 0


while True:
    print(f"Server is Live at PORT {PORT}! Waiting for Connections.")

    # This is the socket that the server uses to talk to the client.
    #   So for each client that connects, their own socket connects to the servers
    #   and is used to talk to that client
    communication_socket, address = server.accept()
    # print(communication_socket)
    print(f"Connected to {address}\n")
    #   Receive message from client
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"Message from Client {client_id} is: {message}\n")
    #   Send response to client
    communication_socket.send(f"Reply From Server: Message Received! Your Id is {client_id}\n".encode('utf-8'))
    communication_socket.close()
    print(f"Connection with client {client_id} of address {address} ended.\n")

    client_id += 1
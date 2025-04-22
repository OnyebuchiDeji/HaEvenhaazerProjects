"""
    Episode 3:
        Sending & Receiving Information from the Server

    This file defines the class that handles the client-side networking semantics

"""

import socket


class Network:
    def __init__(self, server_addr, port_num):
        self.client = socket.socket(socket.AF_NET, socket.SOCK_STREAM)
        self.server_address = server_addr    ##  this value is the ipaddress of the server, same with what is used in the server file
        self.port = port_num
        self.addr = (self.server_address, self.port)
        self.id = self.connect()
    
    def connect(self):
        try:
            self.client.connect(self.addr)
            #   Receives the Acknowledgment Message sent by the Server when the Client connects
            recevied = self.client.recv(2048).decode()
            print("Client says, ", received)
            return received
        except:
            print("Connection from Client to Server failed!")

    def send(self, data):
        """sends data to the server"""
        try:
            #   Send data
            self.client.send(str.encode(data))
            #   Return Response from Server
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(str(e)


n = Network("", 5555)
reply_from_server = n.send("Yo Server! I'm Client")
print(reply_from_server)
reply_from_server = n.send("Yo! Yo! Yo!")
print(reply_from_server)

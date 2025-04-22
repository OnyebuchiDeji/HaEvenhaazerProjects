"""
    Episode 5:
        Utilizes pickle to serializes an object, saving its state in byte.
        This can then be sent over the network and deserialized into the object once again
"""

import socket
import pickle
# from player import Player


class Network:
    def __init__(self, server_addr:str, port_num:int):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = server_addr    ##  this value is the ipaddress of the server, same with what is used in the server file
        self.port = port_num
        self.addr = (self.server_address, self.port)
        ##  This is to get the current state of the Player Object; getting its object itself
        self.p_instance = self.connect()
        print(type(self.p_instance))
    
    def get_instance(self):
        """
            This is used to get the current object's instance
        """
        return self.p_instance
    
    def connect(self):
        try:
            self.client.connect(self.addr)
            #   Receives the Acknowledgment Message sent by the Server when the Client connects
            ##  Note it's not decoded since pickle needs it to remain encoded
            print("Client Received Data.")
            return pickle.loads(self.client.recv(2048))
        except:
            print("Connection from Client to Server Failed!")

    def send(self, data):
        """sends data to the server"""
        try:
            #   Send data to Server
            self.client.send(pickle.dumps(data))
            #   Return Response from Server
            ##  Note it's not decoded since pickle needs it to remain encoded
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(str(e))

def test1():    
    n = Network("10.240.120.2", 5555)
    reply_from_server = n.send("Yo Server! I'm Client")
    print(reply_from_server)
    reply_from_server = n.send("Yo! Yo! Yo!")
    print(reply_from_server)

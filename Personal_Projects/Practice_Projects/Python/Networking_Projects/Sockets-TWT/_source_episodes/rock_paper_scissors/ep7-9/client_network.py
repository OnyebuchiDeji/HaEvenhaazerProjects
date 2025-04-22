"""
    Episode 6-9: Rock Paper Scissors Game
"""

import socket
import pickle


class Network:
    def __init__(self, server_address: str, port_num: int):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server_address
        self.port = port_num
        self.addr = (self.server, self.port)
        self.player_id = self.connect()
    
    def get_player_id(self):
        return self.player_id
    
    def connect(self):
        try:
            self.client.connect(self.addr)
            #   This gets the player number; either Player 1 or Player 2
            return self.client.recv(2048).decode()
        except Exception as e:
            print("Connection from Client to Server Failed!")
    
    def send(self, data):
        try:
            #   Sending the object data as String to Server
            self.client.send(str.encode(data))
            #   Receiving server responde and returning to caller of `send`
            #   Which is in client.py
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(str(e))
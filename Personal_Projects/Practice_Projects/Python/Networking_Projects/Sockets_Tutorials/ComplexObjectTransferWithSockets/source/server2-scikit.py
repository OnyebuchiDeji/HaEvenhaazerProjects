"""
    Server side that handles receipt of the serialized object
    and redirecting it.

    This one handles the Scikit Data Model object being sent to it.

    In the client half of the data is trained and on the server that same half
    is evaluated.
"""

import socket as sckt
import pickle

from sklearn.datasets import load_iris

data = load_iris()
x, y = data.data, data.target


server_socket = sckt.socket(sckt.AF_INET, sckt.SOCK_STREAM) 
server_socket.bind(('127.0.0.1', 9999))

server_socket.listen(1)

while True:
    print("Server Live! Waiting for Connection...\n")
    client_sock, addr = server_socket.accept() 

    try:
        print("Connected to Client!\n")

        data = b''
        while True:
            chunk = client_sock.recv(4096)
            if not chunk:   #   If there was nothing in chunk, break
                break
            #   else
            data += chunk
        
        received_obj = pickle.loads(data)
        print(f"From Client, Received: {received_obj}\n")

        #   Evaluate the model
        print(f"Accuracy of Received Scikit Model:\n{received_obj.score(x, y)}\n")

    finally:
        client_sock.close()
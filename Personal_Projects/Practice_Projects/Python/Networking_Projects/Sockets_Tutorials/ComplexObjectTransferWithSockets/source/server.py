"""
    Server side that handles receipt of the serialized object
    and redirecting it.

    It's trickier because the size of the object being gotten is not known
    by the server; hence some logic is needed to properly get the
    data of the object being transmitted
"""

import socket as sckt
import pickle



server_socket = sckt.socket(sckt.AF_INET, sckt.SOCK_STREAM) 
server_socket.bind(('127.0.0.1', 9999))

server_socket.listen(1)

while True:
    print("Server Live! Waiting for Connection...")
    client_sock, addr = server_socket.accept() 

    try:
        print("Connected to Client!")

        data = b''
        while True:
            chunk = client_sock.recv(4096)
            if not chunk:   #   If there was nothing in chunk, break
                break
            #   else
            data += chunk
        
        received_obj = pickle.loads(data)
        print(f"From Client, Received: {received_obj}")
    finally:
        client_sock.close()
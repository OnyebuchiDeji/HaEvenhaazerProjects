"""
    Remember the server is just what accepts a connection
    In the end, you'll have to create a socket to the client that connected to the server.
"""

import socket as sck
import threading


HOST = "127.0.0.1"
PORT = 9090

server = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
server.bind((HOST, PORT))


server.listen()


clients = []
usernames = []


#   Broadcast: sends a message from a client to every other client
def broadcast(message: str|bytes, exclude=None):
    """This sends the message to all clients"""
    for client in clients:
        if exclude != None and client != exclude:
            client.send(message)


#   handle: handles the connections to each individual client; will be run in their own threads
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            if message:
                print(f"{usernames[clients.index(client)]} says {message.decode('utf-8')}")
                broadcast(message, client)
            
        except:
            #   If there was an issue; e.g. client disconnects by crash or other reason
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames.pop(index)
            print(f"{username} has disconnected")
            break


#   receive: Keeps listening to accept new connections
def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        #   A propmpt that makes the client know to send their user name
        client.send("USER".encode('utf-8'))
        username = client.recv(1024).decode('utf-8')

        usernames.append(username)
        clients.append(client)

        print(f"User {username} just connected")
        broadcast(f"{username} connected to the server!\n")
        client.send("Connected to the server\n".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()



if __name__ == "__main__":
    print("Server Live! Awaiting Connection...")
    receive()

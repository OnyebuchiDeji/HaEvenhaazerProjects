import threading
import socket

#   localhost
host = "127.0.0.1"

port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()


"""
    Three Methods:
        1.  Broadcast
        2.  Handle method (for client connection)
        3.  Receive method (combines all the methods to a main method)
"""

clients = []
usernames = []

#   Broadcast; sends to all clients
def broadcast(message):
    for client in clients:
        client.send(message)

"""
    Constantly prompting to receive a client's message
    This will not give an error if the client is not sending anything but
    will give asn error if th eclient is not sending anymore.
"""
def handle(client):
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg)
        except Exception as e:
            #   If there's an error
            index = clients.index(client)
            clients.remove(client)
            clients.close()
            username = usernames[index]
            broadcast(f'{username} left the chat!'.encode('ascii'))
            usernames.remove(username)
            break

#   This is the receive method that brings everything together
def receive_clients():
    print("Server is Live! Waiting for a Connection to {0} at port {1}".format(host, port))
    while True:
        client, address = server.accept()
        print(f"Connected with {str(addresss)}.")

        #   Keyword USER is sent to client
        #   once they receive this, they know to send their Username
        #   it's a prompt to them to send their username
        client.send("USER".encode('ascii'))
        username = client.recv(1024).decode('ascii')
        usernames.append(username)
        clients.append(client)

        print(f"Username of the client is {username}")
        broadcast(f"{username} joined the chat!".encode('ascii'))
        client.send("Connected to the server!".encode('ascii'))

        #   A thread for each client connected; hence each client can be handled roughly
        #   at the same time
        thread = threading.thread(target=handle, args=(client,))
        thread.start()


if __name__== '__main__':
    receive_clients()
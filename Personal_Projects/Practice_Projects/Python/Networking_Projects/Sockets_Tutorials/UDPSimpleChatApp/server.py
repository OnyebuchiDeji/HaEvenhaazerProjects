"""
    UDP is a connection-less protocol
    There's no connection
    The client sends a message to the server via the server's IP
    and the server just receives the message.
    There's no way for either to verify that the message they sent has been
    received.
    There's also no guarantee of the order in which the messages going either way
    are received.
    For this reason, the queue data structure is used to ensure
    the order in which messages are received.

    The clients and server run on different ports; it's just how UDP works.

    Messages can be lost; they can still be received in the wrong order if there's
    a ot of clients
"""

import threading
import socket
import queue

host = "localhost"
port = 55555

messages = queue.Queue()
clients = []
usernames = []

#   UDP sockets
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#   binding the server to the address at specified port
server.bind((host, port))


def receive():
    """
        This accepts the messages and stores in the
        queue 
    """
    while True:
        try:
            message, addr = server.recvfrom(1024)
            messages.put((message, addr))
        except:
            pass
    
def broadcast():
    """Takes message and sends to all clients"""
    while not messages.empty():
        message, addr = messages.get()
        print(f"Broadcasted {message.decode()}")
        if addr not in clients:
            clients.append(addr)
        for client in clients:
            try:
                if message.decode().startswith("SIGNUP_TAG"):
                    #   using slicing to get the name, which is the string
                    #   after the "SIGNUP_TAG"
                    #   so using .index(":") to get everything after that index
                    name = message.decode()[message.decode().index(":") + 1 : ]
                    server.sendto(f"{name} joined!".encode(), client)
                    usernames.append(name)
                else:
                    server.sendto(message, client)
            except:
                #   if anything fails

                ##  Get client's index
                index = clients.index(client )
                #   pop uses the index to return and remove that item at the index
                name = usernames.pop(index)
                clients.remove(client)
                print(f"{name} has disconnected.")

                
def main():
    t1 = threading.Thread(target=receive)
    t2 = threading.Thread(target=broadcast)

    t1.start()
    t2.start()


if __name__ == "__main__":
    main()


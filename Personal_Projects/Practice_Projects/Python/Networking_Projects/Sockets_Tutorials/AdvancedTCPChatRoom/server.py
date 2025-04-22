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

def kick_user(name):
    if name in usernames:
        name_index = usernames.index(name)
        client_to_kick = clients[name_index]
        clients.remove(client_to_kick)
        client_to_kick.send("You were kicked by an admin!".encode('ascii'))
        usernames.remove(name)
        broadcast(f"{name} was kicked by an admin!".encode('ascii'))

#   Broadcast; sends to all clients
def broadcast(message):
    for client in clients:
        client.send(message)

"""
    Constantly prompting to receive a client's message
    This will not give an error if the client is not sending anything but
    will give asn error if th eclient is not sending anymore.

    Added if statement to check what message is sent.
    For example, whether it's a command, or normal message
"""
def handle(client):
    while True:
        try:
            ##  msg_b is for broadcasting
            ##  msg is for checking the normal message
            msg = msg_b = client.recv(1024)
            if msg.decode('ascii').startswith('KICK'):
                """
                    This is the server handling the permission
                    for whether one can kick or ban by checking if the name of
                    the current client is indeed 'admin'
                """
                if usernames[clients.index(client) == 'admin']:
                    #   cut off first 5 characters
                    name_to_kick = msg.decode('ascii')[5:]
                    kick_user(name_to_kick)
                else:
                    client.send("Command was refused! You're not an admin!".encode('ascii'))
            elif msg.decode('ascii').startswith('BAN'):
                if usernames[clients.index(client) == 'admin']:
                    name_to_ban = msg.decode('ascii')[4:]
                    ban_user(name_to_ban)
                    with open('ban_list.txt', 'a') as f:
                        f.write(f"{name_to_ban}\n")
                    print(f"{name_to_ban} was banned")    
                else:
                    client.send("Command was refused! You're not an admin!".encode('ascii'))
                
            else:
                broadcast(msg)
        except Exception as e:
            if client in clients:
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

        #   Check if user is banned
        with open('ban_list.txt', 'r') as f:
            bans = f.readlines()
        
        if username+'\n' in bans:
            client.send("BAN".encode('ascii'))
            client.close()
            continue

        if username == "admin":
            client.send("PWD".encode('ascii'))
            password = client.recv(1024).decode('ascii')

            #   Normally you will hash every password
            #   and when the user enters their password, hash that input
            #   and then compare the entered one vs. the stored
            ##  But here, this is not done
            if password != "beansNrice":
                #   When the client receives this keyword
                #   it inteprets it as that the connection was refused
                #   because the password was wrong
                client.send("REFUSE".encode('ascii'))
                client.close()
                #   note: it's not broken because this is the loop that enables
                #   more servers to connect
                continue

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
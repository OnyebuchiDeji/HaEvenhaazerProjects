
import socket as sck
import threading


HOST = sck.gethostbyname(sck.gethostname())
PORT = 9999

server = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

clients = []
usernames = []



def broadcast(message, client_to_exclude=None):
    if client_to_exclude is not None:
        for client in clients:
            if client_to_exclude != client:
                client.send(message)
    else:
        for client in clients:
            client.send(message)


def handle_connection(client):
    stop = False
    while not stop:
        try:
            msg = client.recv(1024)
            if not msg:
                continue
            print(f"{usernames[clients.index(client)]}: {msg.decode('utf-8')}\n")
            broadcast(msg)
        except:
            index = clients.index(client)
            clients.remove(client)
            username = usernames.pop(index)
            broadcast(f"{username} left the chat.\n".encode('utf-8'))
            stop = True

def main():
    print("Server is running...")
    while True:
        client, addr = server.accept()
        print(f"Connected to {addr}")

        #   Makes the client know that the client should sent their name
        client.send(f"USER".encode('utf-8'))

        clients.append(client)
        username = client.recv(1024).decode('utf-8')
        usernames.append(username)

        print(f"User {username} just connected!")

        #   WIll not send the broadcast to the current client
        broadcast(f"{username} joined the chat!".encode('utf-8'), client)

        client.send("Server: You are now connected!".encode('utf-8'))

        thread = threading.Thread(target=handle_connection, args=(client,))
        thread.start()


if __name__ == "__main__":
    main()
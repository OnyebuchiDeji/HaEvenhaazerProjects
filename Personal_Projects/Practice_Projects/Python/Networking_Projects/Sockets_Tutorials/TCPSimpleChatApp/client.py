import threading
import socket


username = input("Enter a Username:\t")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((127.0.0.1, 55555))

def receive():
    while True:
        try:
            #   trying to receive messages from server
            msg = client.recv(1024).decode('ascii')
            if message == "USER":
                client.send(username.encode('ascii'))
            else:
                print(message)
        except Exceptions as e:
            print("An Error Occurred")
            client.close()
            break


def write():
    """
        This is always run in a thread.
        It can only be stopped by closing the client
        Once Enter is pressed, send it

    """
    while True:
        msg = f"{username}: {input("")}"
        client.send(msg.encode('ascii'))

def main():
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()


if __name__ == "__main__":
    main()
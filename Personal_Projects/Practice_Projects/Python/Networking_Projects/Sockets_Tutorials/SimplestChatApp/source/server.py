"""
    This is a very simple chat app that only allows a single
    client to join.
    The current server is the only other participant
"""
import socket as sck


server = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
server.bind('localhost', 9999)


def main():
    print("Server is Live and Running! Waiting for a Connection.")
    client, addr = server.accept()
    print("Client has joined.")
    while True:
        try:
            msg_received = client.recv(1024)
            if not msg_received:
                break
            if msg == "quit":
                print("Client has quit. Shutting Down...")
                break
            print(f"Client:\t{msg_received.decode('utf-8')}")
            msg = input("Server:\t")
            client.send(msg.encode('utf-8'))
        except OSError:
            ...
    
    server.close()
    client.close()


if __name__ == "__main__":
    main()
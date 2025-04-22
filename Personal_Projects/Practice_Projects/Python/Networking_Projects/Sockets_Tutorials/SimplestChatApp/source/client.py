import socket as sck



client = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
client.connect('localhost', 9999)


def main():
    while True:
        try:
            client.send(input("Client:\t").encode('utf-8'))
            msg_received = client.recv(1024).decode('utf-8')
            if not msg_received:
                break
            if msg_received == "quit":
                print("Server quit. Exiting...")
                break
            else:
                print(f"Server:\t{msg_received}")
            
        except OSError:
            ...
    client.close()

if __name__ == "__main__":
    main()
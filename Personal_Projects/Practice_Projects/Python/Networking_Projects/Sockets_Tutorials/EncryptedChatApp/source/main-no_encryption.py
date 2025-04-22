"""
    This video does not separate the client and server scripts
    they are all in this one script, 'main.py'
    
    Hence, below, a prompt is made to anyone who runs the script on whether they want to
    be the HOST.
    Of course, once a host is gotten, no other host can be; so after the first, the prompt is not made
    anymore.
    The only thing is that there's no central script storing this information...
    execept, perhaps, once the central host is gotten, they update their state, hence any client
    that tries to connect, even though this prompt is asked, it won't make them a host.

    There's just no way to keep track of if one has already become a host, since the different
    devoces run the same script.
"""
import socket as sck
import threading
import rsa


choice = input("Will you host (1) or connect (2)?\t")

if choice == "1":
    server = sck.socket(sck.AF_INET<sck.SOCK_STREAM)
    server.bind(("192.168.56.1", 9999 ))
    #   The below just controls the max number of connections that can be made
    server.listen()
    client, _ = server.accpet()

elif choice == "2":
    client = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    client.connect(("192.168.56.1", 9999))

else:
    exit()


def sending_messages(c):
    while True:
        message = input("")
        c.send(message.encode())
        print("You:\t", message)

def receive_messages(c):
    while True:
        print("Partner: " + c.recv(1024).decode())

def main():
    threading.Thread(target=sending_messages, args=(client,)).start()
    threading.Thread(target=receive_messages, args=(client,)).start()

if __name__ == "__main__":
    main()
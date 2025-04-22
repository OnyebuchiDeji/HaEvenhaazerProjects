"""
    In this version of `main.py`, there is an issue with being able
    to type in 'quit' to stop the connections.

    But I tinkered with it and it kind of works
"""
import socket as sck
import threading
import rsa
import sys


public_key, private_key = rsa.newkeys(1024)
public_partner = None


choice = input("Will you host (1) or connect (2)?\t")

server = None

if choice == "1":
    server = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    server.bind(("192.168.56.1", 9999 ))
    #   The below just controls the max number of connections that can be made
    server.listen()
    client, _ = server.accept()

    """
        NOTE : this is not encryption; the public key does
        not need to be encrypted.
        these code sections are teh two endpoints sharing their Public Keys
    
    """

    #   The public key is saved in that format, PEM
    #   the pkcs1 is packaging it as bytes in the PEM format
    client.send(public_key.save_pkcs1("PEM"))
    #   Public key received from partner:

    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))

elif choice == "2":
    client = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    client.connect(("192.168.56.1", 9999))
    #   Here the received data sent in encrypted form is decrypted by private key
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
    client.send(public_key.save_pkcs1("PEM"))

else:
    exit()

g_running = True

def sending_messages(c):
    global g_running
    while g_running:
        message = input("")
        #   Encrypt message with the public key of partner
        c.send(rsa.encrypt(message.encode(), public_partner))
        if message == "quit":
            g_running = False
            break
        print("You:\t", message)

def receive_messages(c):
    global g_running
    while g_running:
        #   decrypt received message with private key that both endpoints know
        msg_received = rsa.decrypt(c.recv(1024), private_key).decode()
        if msg_received == "quit":
            g_running = False
            print("Partner:\t Partner left the chat")
            break
        print("Partner: " + msg_received)

def main():
    global client
    global server
    t1 = threading.Thread(target=sending_messages, args=(client,))
    t2 = threading.Thread(target=receive_messages, args=(client,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    client.close()
    if server:
        server.close()
    sys.exit()


if __name__ == "__main__":
    main()
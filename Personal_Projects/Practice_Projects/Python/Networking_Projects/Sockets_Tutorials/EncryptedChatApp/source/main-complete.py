"""
    This video does not separate the client and server scripts
    they are all in this one script, 'main.py'
    
    This version of `main.py` shows the implementation of encryption into the
    networking app

    This is the working version
"""
import socket as sck
import threading
import rsa


public_key, private_key = rsa.newkeys(1024)
public_partner = None


choice = input("Will you host (1) or connect (2)?\t")

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


def sending_messages(c):
    while True:
        message = input("MSG:\t")
        #   Encrypt message with the public key of partner
        c.send(rsa.encrypt(message.encode(), public_partner))
        print("You:\t", message)

def receive_messages(c):
    while True:
        print("Partner: " + rsa.decrypt(c.recv(1024), private_key).decode())

def main():
    threading.Thread(target=sending_messages, args=(client,)).start()
    threading.Thread(target=receive_messages, args=(client,)).start()

if __name__ == "__main__":
    main()
import socket

"""
    Using the 127.0.0.1 is the localhost, meaning that the sockets connect to this same device

    But if one wants to connect two different devices using this app, since the device
    that runs the server script takes the local ip of the device running it, if the device
    trying to connect to it is in the same LAN, then the client script should connect
    to the local/private ip address.
    However, if the device that is trying to connect to the server script is not in the same
    LAN as the device hosting the server script, the client script in that device should connect
    to the public IP of the server device.

    For example, one has a remote server machine and wants to run the server.py script there.
    The IP that the socket should bind to should be the private/local ip of the server.
    One can do these two ways:
        1.  Type in the local IP of that remote server machine
        2.  do `socket.bind(('0.0.0.0', 9999))` <-- This makes Python automatically get the correct
        IP of the host device
    The above is for the server.py

    But now, you are using your own device to run the client.py script to connect to the server.py
    hosted on that remote device.
    Because your device and the remote device are not in the same local network, the client.py script
    must connect using the public IP of that your remote server device.

    This can be done by having a script in that your remote device that the client.py can send a request
    to to get its public IP --- or you could hard code it.
    Either way, it must be the public IP and the Port Number must be the same.
    If these are true, it should work.

    I COULD TEST THIS WITH MY TRYHACKME ACCOUNT. BUT WILL DO THIS IN ANOTHER DAY, GOD GIVEN.
"""


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.bind(('127.0.0.1', 9999))
socket.bind(('192.168.56.1', 9999))


server.listen(1)

while True:
    client,addr = server.accept()
    client.send("Yo! From the server!")
    print("From Client: ", client.recv(1025).decode())

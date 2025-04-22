"""
    The UDP server receives independent messages from the client.
    Note how it does not listen for connections or accept connections; it
    only listend for messages comming in.

    It has no connection, so it is not known which client the message is from.
    Hence one cannot send anything from the server to the client..

    Also, UDP does not have an internal data stream buffer that persists.
    Hence one must choose to get an amount of bytes that exceeds the size of bytes
    of the data sent from the client.

    E.g. could not do:
    ```
        message, address = server_socket.recvfrom(1)
    ``` 
    Else it gives an error like this:
        'A message sent on a datagram socket was larger than the internal message buffer or some
        other network limit, or the buffer used to receive a datagram into was smaller than the
        datagram itself.'
    
    Hence the buffer that is receiving data must be large enough to accommodate all the data the client
    might send.
    It is not like TCP that has a data stream from which the buffer can read bits of data until the
    stream is exhausted, meaning all the sent data is read.
"""


import socket as sckt


server_socket = sckt.socket(sckt.AF_INET, sckt.SOCK_DGRAM)
server_socket.bind(("127.0.0.1", 9999))

#   Understand that execution pauses to wait for a message
message, address = server_socket.recvfrom(1024)
print("Message From Client: ", message.decode('utf-8'))
#   Sends to the address of whom the message is received from
#   So one can answer to that address
server_socket.sendto("Yo! Client!".encode('utf-8'), address)

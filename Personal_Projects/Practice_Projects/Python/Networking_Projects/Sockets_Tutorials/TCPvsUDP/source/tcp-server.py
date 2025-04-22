import socket as sckt


#   TCP is a connection-oriented protocol; it employs establishing
#   a connection with a handshake and ensures data transfer success using acknowledgements
#   and resending of data. TCP for the AF_INET socket connection type is
#   specified by the .SOCK_STREAM
server_socket = sckt.socket(sckt.AF_INET, sckt.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 9999))

server_socket.listen()

while True:
    print(f"TCP Servr is Live! Waiting for a Connection")
    client, address = server_socket.accept()
    print(f"Connected to {address}")
    """
        For TCP, the parameter specifying the amount of bytes is not as important as it
        is in UDP.
        This is because if the 1024 bytes taken from the stream buffer in one try
        is not enough to empty the buffer, the buffer remains, allowing subsequent tries
        until all the data in the buffe ris empty. This is why it's called a Stream.
        TCP ensures this.

        UDP, in contrast does not, which can lead to data loss. Hence the amount of bytes to be received
        has to be large enough to get all the data that has been sent from the client side.
        UDP does not save the data in a buffer stream.
    """
    print("Consider how here just a few bytes are gotten. It demonstrates how in TCP nothing is lost:")
    print("Received From Client: ", client.recv(10).decode('utf-8'))
    client.send("From Server: Yo! Client!\n".encode('utf-8'))
    print("Received From Client: \n", client.recv(1024).decode('utf-8'))
    client.send("Peace from Server!\n".encode('utf-8'))
    client.close()
    
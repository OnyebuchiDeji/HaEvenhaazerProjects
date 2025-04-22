import socket as sckt



client_socket = sckt.socket(sckt.AF_INET, sckt.SOCK_DGRAM)
client_socket.sendto("Yo! Server! From Client".encode('utf-8'), ('127.0.0.1', 9999))

print(client_socket.recvfrom(1024)[0].decode('utf-8'))
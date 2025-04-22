import socket as sckt


client_socket = sckt.socket(sckt.AF_INET, sckt.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 9999))


client_socket.send("Yo! Server!".encode('utf-8'))
print(client_socket.recv(1024).decode('utf-8'))
client_socket.send("Peace from Client!".encode('utf-8'))
print(client_socket.recv(1024).decode('utf-8'))
import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.56.1', 9999))

print(client.recv(1024).decode())
client.send("Yo Server! From Client".encode())
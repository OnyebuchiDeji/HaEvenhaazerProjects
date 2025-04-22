import socket as sck


client = sck.socket(sck.AF_INET6, sck.SOCK_STREAM)
# client.connect(("localhost", 9999))
client.connect(("fe80::7329:609e:7546:491d%3", 9999))


client.send("Yo! From Client, Fam!".encode())
print(client.recv(1024).decode())
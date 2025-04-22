import socket as sck



#   This is my IPV6 address
# host = "fe80::7329:609e:7546:491d%3"
# port = 9999

"""
    To automatically get the IPV6 address automatically as long as you're not running the
    scrypt when a Virtual System is on or an Adapter that can be mistaken for the original.
    then choose the appropriate one
"""
print(sck.getaddrinfo(sck.gethostname(), 9999, sck.AF_INET6))


server = sck.socket(sck.AF_INET6, sck.SOCK_STREAM)
#   Can also use localhost with IPV6
# server.bind(("localhost", 9999))
server.bind(("fe80::7329:609e:7546:491d%3", 9999))

server.listen()


while True:
    client, addr = server.accept()
    print(client.recv(1024).decode())
    client.send("Yo! The Server Greets You, Bro!".encode())
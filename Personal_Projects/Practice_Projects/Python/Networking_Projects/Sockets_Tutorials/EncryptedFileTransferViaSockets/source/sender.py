import os
import socket

from Crypto.Cipher import AES


#   Define Key
key = b"TheEvenhaazerKey"
nonce = b"TheEvenhaazerNce"

#   Create Cipher Key
cipher = AES.new(key, AES.MODE_EAX, nonce)

#   Create Client Socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))

#   Get file size
file_size = os.path.getsize("_to_send/file_to_send.txt")

#   Get file's data
with open("_to_send/file_to_send.txt", "rb") as f:
    data = f.read()

encrypted = cipher.encrypt(data)
client.send("file_to_send.txt".encode())
client.send(str(file_size).encode())
client.sendall(encrypted)   #   no need to encode; already byte data
client.send(b"<END>")


client.close()
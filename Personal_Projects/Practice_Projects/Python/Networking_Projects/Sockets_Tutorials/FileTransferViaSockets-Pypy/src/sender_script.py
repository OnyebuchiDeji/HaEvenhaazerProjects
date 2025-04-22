import os
import socket


#   This is an INTRANET TCP Socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#   Connect to that port at localhost.
client.connect(("localhost", 9999))


#   Now, the sender knows how large the file is and so can send without issues
#   So one needs a way to ensure the reciever waits to get all the bytes that make up the file.

# file = open("resources/morning_glory.jpg", "rb")
file = open("resources/procexp.exe", "rb")

file_size = os.path.getsize("resources/procexp.exe")

#   Next important thing is to send the file name with extension info specified
#   of the file so the receiver can reconstruct it.
#   Sending the file's name
client.send("received_exe.exe".encode())
#   Sending the file size
client.send(str(file_size).encode())

data = file.read()
client.sendall(data)
##  This is an ending tag/token to make the receiver know that it has received the whole file's data.
client.send(b"<END>")


file.close()
client.close()
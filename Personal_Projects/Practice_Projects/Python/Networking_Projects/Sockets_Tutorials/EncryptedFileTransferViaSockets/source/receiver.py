import socket
import tqdm

from Crypto.Cipher import AES


#   Define Key
key = b"TheEvenhaazerKey"
nonce = b"TheEvenhaazerNce"

#   Create Cipher Key
cipher = AES.new(key, AES.MODE_EAX, nonce)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen()

#   It will not be a multi threaded receiver
#   Hence it accepts exactly one connection


client, addr = server.accept()

file_name = client.recv(1024).decode()
file_size = client.recv(1024).decode()
print(file_name)
print(file_size)


file =  open("received/received_file.txt", "wb")

done = False

file_bytes = b""

progress = tqdm.tqdm(unit="B", unit_scale=True,
                    unit_divisor=1000, total=int(file_size))


##  This keeps getting bytes until all bytes are gotten
##  which is indicated by the data ending with "<END>"
while not done:
    data = client.recv(1024)
    if file_bytes[-5:] == b"<END>":
        done = True
    else:
        file_bytes += data

file.write(cipher.decrypt(file_bytes[:-5]))


file.close()
client.close()
server.close()
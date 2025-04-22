import socket
import tqdm


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#   Note that you bind a server to a domain with a port number
server.bind(("localhost", 9999))
server.listen()

##  Accept connection
client, addr = server.accept()

file_name = client.recv(1024).decode()
print(file_name)

file_size = client.recv(1024).decode()
print(file_size)

#   Open file output stream for writing
file = open("received/" + file_name, "wb")
file_bytes = b""
done = False

progress_bar = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000,
                        total=int(file_size))

"""
    The below is done to check whether the end of the transomitted data is reached.
    It keeps prompting to receive the data from the client
    and keeps populating the `file_bytes` buffer
    until the last five characters match the termination tag b'<END>'
    Note why `data=client.recv(1024)` is being called continually
    is because the file, especialy when it's an executable, is usually very big.
    So not all the data can be gotten at once; this is why the end of the
    content received and put in the data variable every loop is not directly
    checked in the condition like this:
            if file_bytes[-5:] == b"<END>":
    It is because at a point it could hold something like:
        <E
    and then
        ND>
    Which will cause the loop never to be stopped
"""
while not done:
    data = client.recv(1024)
    #   If the last fice characters are equa to the termination tag b'<END>'
    if file_bytes[-5:] == b"<END>":
        done=True
    else:
        file_bytes += data
    progress_bar.update(1024)

file.write(file_bytes)

file.close()
client.close()
server.close()
print("Done")

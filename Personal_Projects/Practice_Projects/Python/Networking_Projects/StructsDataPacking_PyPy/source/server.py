"""
    Modified it to receive the struct byte format from the client. Then use this to
    unpack the bytes stream appropriately.
"""

import socket as sck
import struct




def main():
    server = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    server.bind(("localhost", 9999))
    server.listen()

    client, addr = server.accept()
    format_str = client.recv(1024).decode()
    data = client.recv(2048)

    info = fname, lname, age, gender, occupation, weight, orientation = struct.unpack(format_str, data)
    for item in info:
        #   Without the `rstrip("\x00")`, there will be some null terminating characters
        #   also the float has rounding errors.
        if type(item) != bytes:
            print(item)
            continue
        print(item.decode().rstrip("\x00"))


if __name__ == "__main__":
    main()
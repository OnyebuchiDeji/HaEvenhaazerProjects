import socket as sck



#   The medium/communication family, the stream type, and the exact protocol for bluetooth 
client = sck.socket(sck.AF_BLUETOOTH, sck.SOCK_STREAM, sck.BTPROTO_RFCOMM)
#   Bluetooth MAC address and Bluetooth channel id.
client.connect(("00:e9:3a:6f:a4:2a", 4))



def main():
    try:
        while True:
            message = input("Enter Message: ")
            client.send(message.encode('utf-8'))
            data = client.recv(1024)
            if not data:
                break
            print(f"Message: {data.decode('utf-8')}")
    except OSError as e:
        ...
    
    client.close()


if __name__ == "__main__":
    main()
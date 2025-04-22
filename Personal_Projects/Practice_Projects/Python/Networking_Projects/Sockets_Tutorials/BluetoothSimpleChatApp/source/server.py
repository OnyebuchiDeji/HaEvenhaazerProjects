"""
    RFCOMM is the communication protocol for bluetooth.

    Bluetooth has to be on to see the adapter's MAC address
"""

import socket as sck

"""
    Here, the socket needs to be bound to a Bluetooth interface.
    A bluetooth connection is established to a Hardware Address; it does not use an IP.
    This is because an IP is in the TCP/IP stack/layer in the OSINT model, and is one layer
    above the MAC Address (Hardware Address), hence the IP is a higher level of abstraction.

    To get the MAC address for the Bluetooth interface, in Windows, go to the Device Manager -->
    Bluetooth devices --> find the Bluetooth adapter, right-click it --> properties --> Advanced
    --> there you'll see its MAC address. 
"""
#   The medium/communication family, the stream type, and the exact protocol for bluetooth 
server = sck.socket(sck.AF_BLUETOOTH, sck.SOCK_STREAM, sck.BTPROTO_RFCOMM)
#   The first value is my Bluetooth Adapter's MAC address.
#   the second value is the number of channels.
#   Bluetooth has up to 20 channels. Here, channel 4 was used
server.bind(("00:e9:3a:6f:a4:2a", 4))


def main():
    #   This is a client that is communicating with this server
    client, addr = server.accept()

    try:
        while True:
            data = client.recv(1024)
            if not data:
                break
            print(f"Message: {data.decode('utf-8')}")
            message = input("Enter Message:\t")
            client.send(message.encode('utf-8'))

    except OSError as e:
        ...
    
    client.close()
    server.close()
    


if __name__ == "__main__":
    main()
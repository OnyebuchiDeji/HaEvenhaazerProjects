import threading
import socket

##  Check that the username is admin
##  if it is, prompt for password
username = input("Enter a Username:\t")
if username == 'admin':
    password = input("Enter password for admin:\t")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((127.0.0.1, 55555))

stop_thread = False


def receive():
    global stop_thread

    while True:
        if stop_thread:
            break
        try:
            #   trying to receive messages from server
            msg = client.recv(1024).decode('ascii')
            if message == "USER":
                client.send(username.encode('ascii'))
                next_msg = client.recv(1024).decode('ascii')
                if next_msg == 'PWD':
                    client.send(password.encode('ascii'))
                    if client.recv(1024).decode('ascii') == "REFUSE":
                        print("Connection was refused! Wrong Password!")
                        stop_thread = True
                elif next_msg == 'BAN':
                    #   When this keyword is gotten, do BAN logic
                    print("Connection refused because of ban!") 
                    client.close()
                    stop_thread = True

            else:
                print(message)

        except Exceptions as e:
            print("An Error Occurred")
            client.close()
            break


def write():
    """
        This is always run in a thread.
        It can only be stopped by closing the client
        Once Enter is pressed, send it

    """
    while True:
        if stop_thread:
            break

        msg = f"{username}: {input("")}"
        ##  the below skips the "username: " in the string
        ##  and then checks whether the command string only
        ##  starts with /kick -- could use endswith()
        if msg[len(username) + 2:].startswith('/'):
            if username == 'admin':
                if msg[len(username) + 2:].startswith('/kick'):
                    #   skips "username: /kick" in "username: /kick <username>"
                    #   to only send the <username>
                    client.send(f"KICK {message[len(username) + 2 + 6]}".send('ascii'))
                elif msg[len(username) + 2:].startswith('/bam'):
                    #   skips "username: /ban" in "username: /ban <username>"
                    #   to only send the <username>
                    client.send(f"KICK {message[len(username) + 2 + 5]}".send('ascii'))
            else:
                print("Commands can only be executed by the admin!")
                
        else:   ##  just send to server
            client.send(msg.encode('ascii'))

def main():
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()


if __name__ == "__main__":
    main()
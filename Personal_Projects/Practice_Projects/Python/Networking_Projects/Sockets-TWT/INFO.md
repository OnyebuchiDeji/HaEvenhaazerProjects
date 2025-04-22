#   Date Started: Wed-25-Sept-2024

#   Overview
This Practice Project is a tutorial created by Tech With Tim on Youtube.
This project involves the creation of an online multiplayer game on Python, using sockets.
In Episode 6, a Rock, Paper, Scissors game was created

##  Requirements
    1.  Pygame: ```pip install pygame```
    2.  Socket: `import socket`
    3.  Thread: `import thread`
    4.  Pickel: `import pickle`

<br>


#   Elaboration

##  Explanations

### 
### 

##  My Notes
    For an app to connect to another app on another device via a network, it needs
    to connect to the port that its target app is running on.

    For that target app to be visible to its connector (connection source), it has to be "hosted"
    on a certain port.
    Every port is associated with a protocol it excels in; Ports are themselves System applications that
    accept connections.
    Connections can be of various protocols, e.g. HTTP, HTTPS, SMTP, FTP, etc. Hence why there are specific ports
    that excel in handling each unique connection.

    There are also "free" ports that are free for users to run their custom app services on.
    These apps are free to use whatever kind of protocol; hence these ports work with the app receive and relay the incoming
    connections from outside unto that app.

    You know I said there are specific ports that "excel" in handling connections of specific protocols.
    I stand corrected: rather those protocols are made as a standard for businesses and companies so that
    apps they make that use a certain service will always utilize the same port for their users.

    Consider Them:
        Port 20/21: FTP for file transfers

        Port 22: SSH for secure logins and file transfers

        Port 23: Telnet for unencrypted text communications

        Port 25: SMTP for email routing between mail servers

        Port 53: DNS for domain name resolution

        Port 80: HTTP for web traffic

        Port 110: POP3 for receiving emails

        Port 143: IMAP for managing emails on a server

        Port 443: HTTPS for secure web traffic

        Port 993: IMAPS for secure email retrieval

        Port 3306: MySQL for database management

        Port 5432: PostgreSQL for database management

        Port 5900: VNC for remote desktop control

        Port 8080: Alternative HTTP port often used in web development

##  Things Learned

###
###


<br>

#   Reference
Tech With Tim, 2020, "Python Online Game Tutorial" Playlist on Yotube


#   Finally
Done: Thurs-26-Sept-2024
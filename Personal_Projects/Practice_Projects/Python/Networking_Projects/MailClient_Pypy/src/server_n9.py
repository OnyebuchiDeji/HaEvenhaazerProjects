"""
    Automating sending an email.
"""
from dotenv import load_dotenv, find_dotenv
import os

import smtplib, ssl
##  All of the below is so that one can easily construct an email
from email import encoders    ##  Also built-in
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


load_dotenv(find_dotenv())

##  The SMTP server address is specific to your provider, e.g smtp.gmail
##  One can have his email address linked to his website's url
##  SMTP port number is 25
server = smtplib.SMTP('smtp.gmail.com', 25)
server.connect('smtp.gmail.com', 25)



##  This needs to be called to start the service.
server.ehlo()
server.starttls()
server.ehlo()
#   Now, login to your account; add your email and password.

server.login(os.getenv("EMAIL"), os.getenv("PSW"))


msg = MIMEMultipart()
msg["From"] = "Deji"
msg["To"] = 'ebenayo10@gmail.com'
msg["Subject"] = 'Automating email sendinf with Python'

#   Load the message text file
with open("src/message.txt", "r") as f:
    message = f.read()
    msg.attach(MIMEText(message, "plain"))

#   Now, attaching an image...
file_name = "resource/20230129_112910.jpg"
attachment = open(file_name, 'rb')

#   Payload object
#   The `octet-stream` is the stream that will be used to process the payload data.
#   I reckon that it is somehting that optimises the sending of data via emails...
#   I think I read it somewhere.
payload = MIMEBase('application', 'octet-stream')
payload.set_payload(attachment.read())

encoders.encode_base64(payload)
payload.add_header('Content-Disposition', f'attachement; filename={"Keele_Tree.jpg"}')
msg.attach(payload)

text_msg = msg.as_string()
server.sendmail('ebenayo10@gmail.com', 'ebenayo10@gmail.com', text_msg)
attachment.close()
server.quit()
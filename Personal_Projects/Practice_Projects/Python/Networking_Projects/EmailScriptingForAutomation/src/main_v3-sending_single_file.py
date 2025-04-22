"""Adding Image Attachement to Email"""


import smtplib
import os
from dotenv import load_dotenv, find_dotenv

from email.message import EmailMessage
import imghdr


load_dotenv(find_dotenv())

SENDER = os.getenv("EMAIL")
RECEIVER = "ebenayo10@gmail.com"


def plain_text_msg():
    subject = "Want to finish Python"
    body = "Let's go! Power with the iteration!"

    msg = f"Subject: {subject}\n\n{body}\n"

    return msg

def msg_using_email_module():
    msg = EmailMessage()
    msg["From"] = SENDER
    msg["To"] = RECEIVER
    msg["Subject"] = "Want to finish Python."
    msg.set_content("Let's go! Power with the iteration! Sent using the Email Message object.")
    return msg


def msg_with_attachement():
    msg = EmailMessage()
    msg["From"] = SENDER
    msg["To"] = RECEIVER
    msg["Subject"] = "Want to finish Python."
    msg.set_content("Let's go! Power with the iteration! Check the Tree.")

    with open("resources/20230129_112910.jpg", "rb") as fstr:
        file_data = fstr.read()
        
        #   Before attaching, determine what image is being attached, that is, its type.
        #   This is needed when attaching multiple images of different types 
        file_type = imghdr.what(fstr.name)  #   Returns the image's type
        file_name = os.path.basename(fstr.name)

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
    return msg

"""
    using smtplib.SMTP_SSl and port 465 does not include these:
    smtp.ehlo()
    smtp.starttls() ##  This encrypts the traffic
    smtp.ehlo()
    The authentication is done by SMTP_SSL
    However, no other port number can be used as SMTP_SSL only works for port 465
"""
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.login(SENDER, os.getenv("PSW"))

        ##  Now send this plaintext email
    smtp.send_message(msg_with_attachement())
    


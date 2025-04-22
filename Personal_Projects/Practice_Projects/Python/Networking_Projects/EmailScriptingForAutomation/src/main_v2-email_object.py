"Using EmailMessage to build image content"

import smtplib
import os
from dotenv import load_dotenv, find_dotenv

from email.message import EmailMessage

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
    smtp.send_message(msg_using_email_module())
    


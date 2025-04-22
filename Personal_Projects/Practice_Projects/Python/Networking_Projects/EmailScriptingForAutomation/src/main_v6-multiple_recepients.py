"""
    Here multiple sending multiple emails to multiple addresses.

"""


import smtplib
import os
from dotenv import load_dotenv, find_dotenv

from email.message import EmailMessage


load_dotenv(find_dotenv())

SENDER = os.getenv("EMAIL")
contacts = ["ebenayo10@gmail.com", "evenhaazer335@gmail.com"]


def plain_text_msg():
    subject = "Want to finish Python"
    body = "Let's go! Power with the iteration!"

    msg = f"Subject: {subject}\n\n{body}\n"

    return msg

def msg_multiple_recepients():
    msg = EmailMessage()
    msg["From"] = SENDER
    #   .join concactenates a number of strings using the character at the front
    #   as the delimeter
    msg["To"] = ', '.join(contacts)
    msg["Subject"] = "Want to finish Python."
    msg.set_content("Let's go! Power with the iteration! Sending email to many recepients.")
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
    smtp.send_message(msg_multiple_recepients())
    


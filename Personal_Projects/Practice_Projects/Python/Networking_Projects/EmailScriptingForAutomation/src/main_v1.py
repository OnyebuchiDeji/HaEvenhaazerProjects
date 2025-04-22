import smtplib
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SENDER = os.getenv("EMAIL")
RECEIVER = "ebenayo10@gmail.com"


def plain_text_msg():
    subject = "Want to finish Python"
    body = "Let's go! Power with the iteration!"

    msg = f"Subject: {subject}\n\n{body}\n"

    return msg



with smtplib.SMTP('smtp.gmail.com', 25) as smtp:
    smtp.ehlo()
    smtp.starttls() ##  This encrypts the traffic
    smtp.ehlo()

    smtp.login(SENDER, os.getenv("PSW"))

        ##  Now send this plaintext email
    smtp.sendmail(SENDER, RECEIVER, plain_text_msg())
    


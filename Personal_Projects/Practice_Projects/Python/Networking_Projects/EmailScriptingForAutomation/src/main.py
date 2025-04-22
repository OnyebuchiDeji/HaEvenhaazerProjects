"""
    This demonstrates sending HTML files
"""


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


"""
    Note that because some people turn off HTML emails, it is good
    to send plain_text message as a fallback.
"""
def msg_html_v1():
    msg = EmailMessage()
    msg["From"] = SENDER
    msg["To"] = RECEIVER
    msg["Subject"] = "Want to finish Python; Sending HTML"
    msg.set_content("Let's go! Power with the iteration! This is plain text.")
    
    msg.add_alternative("""\
        <!DOCTYPE html><html>
            <body>
                <h1 style="color:blueviolet; font-size:2rem">
                    Let's go! Power with the iteration!
                    HTML Style!
                </h1>
            </body>
        </html>
    """, subtype='html')
        
    return msg

def msg_html_v2():
    msg = EmailMessage()
    msg["From"] = SENDER
    msg["To"] = RECEIVER
    msg["Subject"] = "Want to finish Python; Sending HTML"
    msg.set_content("Let's go! Power with the iteration! This is plain text.")

    with open("./message.html", "r") as fstr:
        html_content = fstr.read()
        msg.add_alternative(html_content, subtype="html")

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
    smtp.send_message(msg_html_v1())
    


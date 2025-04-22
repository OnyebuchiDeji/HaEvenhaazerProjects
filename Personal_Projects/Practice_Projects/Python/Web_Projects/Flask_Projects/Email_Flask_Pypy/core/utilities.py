import smtplib, ssl
from email.mime.text import MIMEText
# from email import encoders <-- for attaching files
# from email.mime.base import MIMEBase <-- for attaching files
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Utils:
    g_email_verified = False
    g_recipient_email = "ebenayo10@gmail.com"

    def __init__(self):
        ...
    
    def send_email_v1(self):
        """
            This just sends the email
            This could not send the email with a markup message
        """
        msg = MIMEMultipart()
        msg["From"] = "Deji"
        msg["to"] = self.g_recipient_email
        msg["Subject"] = "Verification Email Sent from Python Script"

        with open("core/message.html", "r") as f:
            message = f.read()
            msg.attach(MIMEText(message, "plaintext"))
        email_message = msg.as_string()

        context = ssl.create_default_context()

        with smtplib.SMTP("smtp.gmail.com", port=25) as smtp:
            #   Start 'transfer layer socket'
            smtp.starttls(context=context)
            smtp.login(os.getenv("SENDER_EMAIL"), os.getenv("APP_PSW"), initial_response_ok=True)
            smtp.sendmail(os.getenv("SENDER_EMAIL"), self.g_recipient_email, email_message)
            smtp.quit()

        print("Email Sent Successfully.")

    def send_email_v2(self):
        """
            This just sends the email
            This sends the email with message with link
            with the email.message EmailMessage object...
            but without the use of these:
            1.  MIMEMultipart()
            2. `msg.attach(MIMEText, ...)
        """
        msg = EmailMessage()
        msg["From"] = "Deji"
        msg["to"] = self.g_recipient_email
        msg["Subject"] = "Verification Email Sent from Python Script"

        with open("core/message.html", "r") as f:
            message = f.read()
            msg.set_content(message)

        email_message = msg.as_string()

        context = ssl.create_default_context()

        with smtplib.SMTP("smtp.gmail.com", port=25) as smtp:
            #   Start 'transfer layer socket'
            smtp.starttls(context=context)
            smtp.login(os.getenv("SENDER_EMAIL"), os.getenv("APP_PSW"), initial_response_ok=True)
            smtp.sendmail(os.getenv("SENDER_EMAIL"), self.g_recipient_email, email_message)
            smtp.quit()

        print("Email Sent Successfully.")

    def send_email_v3(self):
        """
            This sends the email with Markup
            But the links do not work for some reason, probably because its part of the email
            So I remove the link from the 'a' anchor tag.
        """

        msg = EmailMessage()
        msg["From"] = os.getenv("SENDER_EMAIL")
        msg["to"] = self.g_recipient_email
        msg["Subject"] = "Verification Email Sent from Python Script"

        with open("core/message.html", "r") as f:
            message = f.read()
            msg.set_content(message)

        with open("core/message.html", "r") as f:
            html_content = f.read()
            msg.add_alternative(html_content, subtype='html')
        

        context = ssl.create_default_context()

        with smtplib.SMTP("smtp.gmail.com", port=25) as smtp:
            #   Start 'transfer layer socket'
            smtp.starttls(context=context)
            smtp.login(os.getenv("SENDER_EMAIL"), os.getenv("APP_PSW"), initial_response_ok=True)
            smtp.send_message(msg)
            # smtp.sendmail(os.getenv("SENDER_EMAIL"), self.g_recipient_email,msg.as_string())
            smtp.quit()

        print("Email Sent Successfully.")

        


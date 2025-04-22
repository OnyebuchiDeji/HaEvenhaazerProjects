#   Date: Mon-8-July-2024



#   Briefing
Sending email - plain text, adding attachements, html emails, and others

Could even emulate an smtp debugging server by running this on command line:
```
    python -m smtpd -c DebuggingServer -n localhost:1025
```
It will listen for emails snet via smtp and display it.

Then in the code, the line with the context controller will change to this:
```
    with smtplib.SMTP('localhost', 1025) as smtp:
        ...
```
Then remove the following:
```
    smtp.ehlo()
    smtp.starttls() ##  This encrypts the traffic
    smtp.ehlo()
```

#   References
"How to Send Emails Using Python - Plain Text, Addinf Attachements, HTML Emails, and More"
- Corey Schafer
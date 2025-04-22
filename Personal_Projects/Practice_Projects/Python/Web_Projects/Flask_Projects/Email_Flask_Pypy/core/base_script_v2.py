"""
    This script was to be used
    to test asynchronous flask endpoints.
"""

from flask import Flask, redirect, url_for, render_template, request

import os
import time
import threading

from .utilities import Utils

static_dir = str(os.path.abspath(os.path.join(__file__, "..","client")))
templates_dir = str((os.path.join(static_dir,"templates")))
print(templates_dir)

app = Flask(__name__, static_folder=static_dir, template_folder=templates_dir)
app.secret_key = "msdf923jsnskbf1"
app.config["SERVER_NAME"] = "localhost:4242"

@app.route("/home")
def home_page():
    if Utils.g_email_verified:
        return render_template("home.html")

    return redirect(url_for("login_page"))    ##  Go to login page.


#   Already GET by default, but just made it explicit
@app.route("/confirm", methods=["GET"])
def confirm_link():
    """
        When email recepient receives the email and clicks the link in it
        It sets the 'email_verified' global to True.
    """
    Utils.g_email_verified = True
    return render_template("success.html")


def verify_email_logic():
    ##  Send email on separate thread
    threading.Thread(target=Utils().send_email_v2).start()
    count = 0
    ##  Gives a 60 seconds leeway
    while not Utils.g_email_verified:
        if (count >= 60):
            break
        time.sleep(1)
        count += 1
    if Utils.g_email_verified:
        return redirect(url_for("home_page"))

    msg = "Login Not Successful; Check your email and click the link"   
    """
        Trying to attach the message so that Jinja can render it on 
        the html taemplate, so I tried these:
        1.  
            The argument in url_for attaches the data to the URL in GET form
            return redirect(url_for("login_page", message=msg))
        2.  return redirect(url_for("login_page"))
    """
    #   So do this instead:
    return redirect(url_for("login_page"))
    

@app.route("/verify-email", methods=["GET"])
def verify_email():
    """
        This waits in a loop fot the 'email_verified' flag to become True.
        This flag only becomes True when the email recepient clicks the confirm
        link in the email
    """
    threading.Thread(target=verify_email_logic).start()
    return redirect(url_for("login_page"))

    

        

@app.route("/login", methods=["GET"])
def login_page():
    """
        This simply renders the login page.
        When the login's page's link is clicked, it sends the
        email and that endpoint stalls for 30 seconds...
        if the email verification link is clicked, the site redirects
        to the home page.
        If not, after the 30 seconds, it redirects to the same login page.
    """
    return render_template("login.html", message="Not yet logged in.")


"""
    This tutorial shows the use of sessions to enable scripts communicate...
    or to store information while the servers are running.

    For this version, it does everthing the tutorial on sessions does.
    But this time, permanent sessions are implemented. So though app is closed, on logging back in, the user data is there.
    the session is not really stored permanently as this is bad practice. Rather, it is stored for 5 minutes.
"""

from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta  ##  TO set up the max time the session can last for

app = Flask(__name__)
app.secret_key = "l#dsnfkasnm"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        """ Making a session permanent """
        session.permanent = True
        user = request.form["nm"]

        if user != "":
            session["user"] = user
            return redirect(url_for("user"))
        else:
            return redirect(url_for("login.html"))
    else:
        ##  Already logged in? Redirect back to user page once logged in
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")
    
@app.route("/user")
def user():
    """
        ##C1
    """
    logout_link = "<br><a href='/logout' style='font-size=1em;'" + "onmouseover=this.style.color='red' onmouseleave=this.style.color='blue'>Logout</a>"
    ##  Checking if the user key is in the session
    if "user" in session:
        user = session["user"]
        return f"<h2 style='font-style: normal; text-decoration: none;'>User <b><em>{user}</em></b> has logged in!</h2>{logout_link}"
    else:
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__=="__main__":
    app.run(debug=True)
"""
    Date: Fri-10-May-2024
    This is about showing information from the pevious page on the next page when
    something happens to the GUI.
    E.g. Logging in takes you from the login oage to the next. In that next you'll want to show
    a message saying 'logged in'
    Likewise for logout.
"""

from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta


app = Flask(__name__)
app.secret_key = "l#dsnfkasnm"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        ##  The session stores data as a dictionary.
        ##  The sectin is a global object, like in PHP!
        if user != "":
            session["user"] = user
            flash("Login Successful!")
            return redirect(url_for("user"))
        else:
            return redirect(url_for("login.html"))
    else:
        ##  Already logged in? Redirect back to user page once logged in
        if "user" in session:
            flash("Already Logged In!")
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
        return render_template("user.html", user=user)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    ##  Only tell them they'e logged out if the user is in the session
    if "user" in session:
        user = session["user"]
        #   Here show logged out succesfully
        #   There are categories to show icons: info or info and error,
        flash(f"You have logged out, {user}!!!", "info")
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__=="__main__":
    app.run(debug=True)
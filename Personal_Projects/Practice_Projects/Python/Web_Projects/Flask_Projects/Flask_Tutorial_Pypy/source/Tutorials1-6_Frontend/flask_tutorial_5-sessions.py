"""
    This tutorial shows the use of sessions to enable scripts communicate...
    or to store information while the servers are running.

    This time, the user's name is not passed as an argument. It's gotten from the session!

    YO! Session data is encrypted on the server. So a secret key is needed to be able to encrypt...
    and decrypt the data.

    Notice that session data is only open when the app is running. If the app is closed and reopened...
    even thought the /usr url is entered, it redirects back to the login according to line ##C1

    Then the clearing of sessions and logging out is implemented. When a user logs out, session info is deleted!
"""

from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = "l#dsnfkasnm"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        ##  The session stores data as a dictionary.
        ##  The sectin is a global object, like in PHP!
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
"""
    This tutorial is about using GET and POST methods of sending data.

    This tutorial involves building a login form to implement this process

"""
from flask import Flask, redirect, url_for, render_template, request


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

#3  THe second argument in @app.route() is the http transfer request method
@app.route("/login", methods=["POST", "GET"])
def login():
    """
        How to check if one reached the page with a GET or POST request
        Usin request object
    """
    ##  If the request is POST, it's from the form
    if request.method == "POST":
        ##  This gets the data posted from the form
        user = request.form['nm']
        ##  Then redirect to the user page that displays the user that logged in!
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")
        

#   The </usr> is a parameter that one can type into the url to display in the page.
#   It's exactly how get method works! 
@app.route("/<usr>")
def user(usr):
    return f"<h2>User <b>{usr}</b> Logged in!</h2>"


if __name__ == "__main__":
    app.run(debug=True)
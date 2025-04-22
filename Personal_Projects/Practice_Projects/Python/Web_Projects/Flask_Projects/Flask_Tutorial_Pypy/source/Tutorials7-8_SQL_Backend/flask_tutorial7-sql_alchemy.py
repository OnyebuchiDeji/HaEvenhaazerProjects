"""
    Date: Fri-10-May-2024
    This turorial is about databaases and saving user-specific info.

    Import sqlalchemy with pip install flask-sqlalchemy

    Note that before you call DB.create_all(), call app.app_contect.push()
    then the DB.create_all() in __main__
    OR
    Do:
    with app.app_contect():
        DB.create_all()
        app.run()

    If you see this tutorial7, A of flask_tutorial8, because this is not done, it gives an error
    _get_current_object
    raise RuntimeError(unbound_message) from None

    This typically means that you attempted to use functionality that needed
    the current application. To solve this, set up an application context
    with app.app_context(). See the documentation for more information.

    Note that tutorial8_ogv2 tries a different approach from the SQLAlchemy documentation!


    
"""

from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.secret_key = "l#dsnfkasnm"
##  Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
##  To remove a common warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5)

"""
 Makes it way easier to save information since it enables one to
 write the database stuff in python code instead of writing sql queries

 Note that before you call DB.create_all(), call app.app_contect.push()
 then the DB.create_all() in __main__
 OR
 Do:
 with app.app_contect():
    DB.create_all()
    app.run()

"""
DB = SQLAlchemy(app)

##  ROWS AND COLUMNS

class users(DB.Model):
    ##  .Column(Name, type, primary_key?)
    _id = DB.Column("id", DB.Integer, primary_key=True)
    # name = DB.Comlumn("name", DB.String(100))
    # email = DB.Column("email", db.String(100))
    """No need for the name optional parameter because of the variable name is used"""
    name = DB.Comlumn(DB.String(100))
    email = DB.Column(DB.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
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
    
@app.route("/user", methods=["POST", "GET"])
def user():
    # logout_link = "<br><a href='/logout' style='font-size=1em;'" + "onmouseover=this.style.color='red' onmouseleave=this.style.color='blue'>Logout</a>"
    email = None

    ##  Checking if the user key is in the session
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            ##  Grab email from the email field
            email = request.form["email"]
            ##  Store in session
            session["email"] = email
            flash("Email Saved!")
        else:
            ##  if GET, get the previous email that has been entered, if any
            ##  because if not by POST, thee is no other way to get the email
            if "email" in session:
                email = session["email"]
                flash("Showing Recent Email!")
        ##  Passing in the email parameter into user.html
        ##  If email is nOne, the placeholder text from the user.html form is displayed
        return render_template("user.html", email=email)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))
    

@app.route("/logout")
def logout():
    ##  Only tell them they've logged out if the user is in the session
    if "user" in session:
        user = session["user"]
        flash(f"You have logged out, {user}!!!", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))

if __name__=="__main__":
    ##  Creates the database if it doesn't already exist in the program
    ##  when the app is run
    DB.create_all()
    app.run(debug=True)
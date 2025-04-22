"""
    Date: Fri-10-May-2024
    This tutorial is about databases and saving user-specific info.

    Import sqlalchemy with pip install flask-sqlalchemy

    Adding deleting and updating users with SQLAlchemy
"""

from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase



app = Flask(__name__)
app.secret_key = "l#dsnfkasnm"
##  Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
##  To remove a common warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5)

class Base(DeclarativeBase):pass

"""
 SQLAlchemy makes it way easier to save information since it enables one to
 write the database stuff in python code instead of writing sql queries

 note the DB.create_all() in __main__
 It's above app.run()
"""

"""
    It is a subclass of DeclarativeBase or DeclarativeBaseNoMeta
    that is used to initialise the database.

    This object gives access to the DB.Model once construvted.
    The DB.Model class is used to define models
    and the DB.session to execute queries.
"""
DB = SQLAlchemy(model_class=Base)


"""
    Configure the extension
    This connects the database extension to my Flask app/
    The only required Flask app config is the `SQLALCHEMY_DATABASE_URI` key
    this connection string tells SQLAlchemy qhat database to connect to.

"""
DB.init_app(app)

##  ROWS AND COLUMNS

class users(DB.Model):
    ##  .Column(Name, type, primary_key?)
    _id = DB.Column("id", DB.Integer, primary_key=True)
    # name = DB.Comlumn("name", DB.String(100))
    # email = DB.Column("email", db.String(100))
    """No need for the name optional parameter because of the variable name is used"""
    name = DB.Column(DB.String(100))
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
        session["user"] = user

        ##  This query will find all the users in the table with a name
        ##  it grabs the first entry since this program only stores one user with one name
        ##  if nothing is found, None is returned
        found_user = users.query.filter_by(name=user).first()

        if found_user:
            session["email"] = found_user.email
        else:
            ##  pass in the user name and a blank for the eamil since it has not yet been entered
            ##  to create the user
            usr = users(user, "")
            ##  Add the user to the database's staging area. It does the associating with column names
            DB.session.add(usr)
            ##  This finally updates the original database -- committing the changes
            DB.commit()

            flash("Login Successful!")
            return redirect(url_for("user"))
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
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email
            ##  Now save the changes
            DB.commit()
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
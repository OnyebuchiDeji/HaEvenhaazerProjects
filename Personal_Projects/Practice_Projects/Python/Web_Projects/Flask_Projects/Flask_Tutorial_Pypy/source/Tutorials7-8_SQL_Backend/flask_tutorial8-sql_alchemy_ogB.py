"""
    Date: Fri-10-May-2024
    This tutorial is about databases and saving user-specific info.

    Import sqlalchemy with pip install flask-sqlalchemy

    Adding deleting and updating users with SQLAlchemy

    Added advanced queries

    Note @C1 <-- find it to k ow what I mean
    ##  Note that you can use .all() instead of .first() to get all the results that meet that criteria

    Note that I add my own code here!!!! view_and_edit

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
"""
DB = SQLAlchemy(app)

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

@app.route("/view")
def view():
    ## the users.query.all() gets alll the users and pass them as object into the render template (html file)
    ## where the information is displayed 
    return render_template("view.html", values=users.query.all())

@app.route("/view_and_edit", methods=["POST", "GET"])
def view_and_edit():
    usrToRemove = None
    """"I must consider case sensitivity. So I will first get all user names"""
    if request.method == "POST":
        usrToRemove = request.form["nm"].lower()
    if usrToRemove != None:
        all_users = users.query.all()
        for user in all_users:
            if user.name.lower() == usrToRemove:
                ##  This checks for the row object that has the matching name
                ##  Then it deletes the whole object, both the name and email
                users.query.filter_by(name=user.name).delete()

                ##  Finally, commit changes to database
                DB.session.commit()

    ## the users.query.all() gets all the users and pass them as object into the render template (html file)
    ## where the information is displayed 
    return render_template("viewNedit.html", values=users.query.all())

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user

        """
            This query will find all the users in the table with the name that matches 
            that gotten from variable `user`
            it grabs the first entry, that is, the name column, not the email.

            When I do:
            users.query.filter_by(name=user), this is the SQL query returned
                SELECT users.id AS users_id, users.name AS users_name, users.email AS users_email 
                FROM users
                WHERE users.name = ?
            So it selects the row of data that has users.name = `user`, the `user` variable.
            What .first() does is to returns you the first response object that matches!
            Note, it is not the name, but the object. That is why you can access the name and email attributes this way:
            found_user.name, found_user.email

            the below code was like this before:
                found_user = users.query.filter_by(name=user).first()
                if found_user:
                    session["email"] = found_user.email
        """
        found_user = users.query.filter_by(name=user)
        if found_user.first():
            session["email"] = found_user.first().email
            print(found_user)
        else:
            ##  pass in the user name and a blank for the eamil since it has not yet been entered
            ##  to create the user
            usr = users(user, "")
            ##  Add the user to the database's staging area. It does the associating with column names
            DB.session.add(usr)
            ##  This finally updates the original database -- committing the changes
            DB.session.commit()

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
            """@C1"""
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email
            ##  Now save the changes
            DB.session.commit()
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

    """Do this..."""
    with app.app_context():
        DB.create_all()
        app.run(debug=True)

    """OR"""
    """
        app.app_contect().push()
        DB.create_all()
        app.run(debug=True)
    """
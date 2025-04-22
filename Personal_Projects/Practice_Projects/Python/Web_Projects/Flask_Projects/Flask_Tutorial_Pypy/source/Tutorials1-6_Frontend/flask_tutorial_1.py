from flask import Flask, redirect, url_for

"""
    An Intro into Flask
    
    Port 5000 is the default port that Flask uses.

    1. Creation of page.
    2. Adding content to page.
    3.  Passing values to be displayed in page -- arguments via urls
    4.  redirect module and url_for allow one to return a redirect from a specific function.
        here an administrator page is created.
        In the implementation below, when '/admin' is entered into the url when the web app...
        is currently viewing at: http://127.0.0.1:5000/Yo, for example, when Yo is replaced with admin...
        it redirects to the home page.
    5. Note that the html templates must be in the folder named templates!
"""

##  Instance of Flask Web App
app = Flask(__name__)

## This will be the home page
##  The decorator gives the page a root to access the page
##  The argument in .route() is the path to the homepage
@app.route("/")
def home():
    ##  Return inline html
    return "Yo! This is the main page! <h1>Yo!</h1>"

##  When data are put within these tags in the app.route() argument...
##  It will take that value and pass it into the  function -- the wayof passing parameters
@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    """
        To redirect one to another page.
        But using flask, it is done by putting the name of the funciton to be redirected to.
        In this case, 'home'

        Note that typing '/admin' to the url redirects back to home page
    """

    return redirect(url_for("home"))

if __name__=="__main__":
    app.run()
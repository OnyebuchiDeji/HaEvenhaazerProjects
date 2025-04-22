from flask import Flask, redirect, url_for

"""
    Here the implementation of redirecting to a page that takes a value.

    Second. When specifying the routes:
    If app.route is specified as "/admin", if on the browser from the root http://127/0/0/1:5000...
    you add "/admin/" it will cause an error.
    But if yo do @app.rout("/admin/") if you add either "/admin/" or "/admin" both will work perfectly!
"""

##  Instance of Flask Web App
app = Flask(__name__)


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

        For redirecting to a page that takes an argument:
        just specify the argument and give the value. 
    """


    return redirect(url_for("user", name="Admin!"))

if __name__=="__main__":
    app.run()
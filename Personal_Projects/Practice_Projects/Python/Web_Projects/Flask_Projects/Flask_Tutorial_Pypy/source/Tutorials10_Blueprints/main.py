"""
    Done: Fri-10-May-2024
    
    These are done:
    Making a blueprint: they are extensions to one's apps

    They enable one to divide the app into separate python files where one can pass specific views
    and render_templates from different areas of one's projects or applications.

    In the previous tutorials, one will have to do these in a single python file
    but with blueprints one can use multiple python files.

    @C1
        Consider that @app.route("/") is also in home.py...
        If I run this I see that it shows the homepage displayed by home.py

        How it works is that flask will check if this @app.route("/") matches any blue print
        since home.py has @home_page.route("/"), the match is successful.
        It will then run the home() function in home.py, returning the template "home.html"

        If home.py didn't have the '/' route, it will display the <h1> Testing Blueprints </h1>

    @C2
        Using ``url_prefix``, one can make @app.route("/") and @home_page.route("/') reference
        their own functions.

        The `url_prefix` specifies what needs to come first in the route url for one to access a blueprint
        In this code, url_prefic = '/admin'
        This will make it be that to access the home_page rendered templates in home.py from the web app...
        one needs to type "/admin/" or "/admin/home" according to these:
            @home_page.route("/home")
            @home_page.route("/")
    
"""

from flask import Flask, render_template

from home import home_page

app = Flask(__name__)
app.register_blueprint(home_page, url_prefix="/admin")

##  This makes the routes '/' and 'home' refer to the same function `home`
"""@C1"""
@app.route("/")
def home():
    return "<h1>Testing Blueprints</h1>"



if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)

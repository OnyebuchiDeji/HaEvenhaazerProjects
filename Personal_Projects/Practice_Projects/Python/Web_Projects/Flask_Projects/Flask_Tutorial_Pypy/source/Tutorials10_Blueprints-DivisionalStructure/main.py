"""
    Done: Fri-10-May-2024
    
    These are done:
    Employing the ``Divisional Structuring`` of My Project
    I use packages to structure the project.
    I add home.py, the templates, and static folders in a package, and add an __init__.py
    file to make it a package.
    Hence I do:
        from admin.home import home_page
    to access home.py

"""

from flask import Flask, render_template

from admin.home import home_page

app = Flask(__name__)
app.register_blueprint(home_page, url_prefix="/admin")

##  This makes the routes '/' and 'home' refer to the same function `home`
@app.route("/")
def home():
    return "<h1>Testing Blueprints</h1>"


if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)

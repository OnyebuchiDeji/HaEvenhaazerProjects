from flask import Blueprint, render_template

"""
    This is an extension of main.py
"""

##  Last argument is the path to the static folder and template folder
##  This is because different folders can store the templates for different views
home_page = Blueprint("home_page", __name__, static_folder="static", static_url_path="static", template_folder="templates")


@home_page.route("/home")
@home_page.route("/")
def home():
    return render_template("home.html")

@home_page.route("/test")
def test():
    return """
                <h1 style='color: purple;'>
                    <b>This is a test page testing blueprints and accessing the pages they render!</b>
                </h1>
                <br><br>
                <a href='../'><em>Go To Root</em></a> <br><br>
                <a href='/admin/'><em>Go Home</em></a>
            """
from flask import Flask, redirect, url_for, render_template

"""
    HTML Templates.

    The render_template module helps one grab an html file and render it as one's web page.
"""
app = Flask(__name__)


##  The root page usually treated as home
@app.route("/")
def home():
    return render_template("index.html")


if __name__=="__main__":
    app.run()
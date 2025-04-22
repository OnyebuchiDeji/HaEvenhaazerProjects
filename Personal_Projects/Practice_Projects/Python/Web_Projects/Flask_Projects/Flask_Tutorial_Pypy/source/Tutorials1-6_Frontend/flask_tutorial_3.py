"""
    This tutorial looks on template inheritance.
    It also involves adding bootstrap.

    Wed-1-May-2024
"""

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/") ##  For root
def home():
    return render_template("index-template_inheritance1.html", content="Testing")

@app.route("/test") 
def test():
    return render_template("index-template_inheritance2.html", content="Testing")

if __name__ == "__main__":
    ##  The debug enable us to not have to rerun the server every change.
    # It detects the changes and applies it for us
    app.run(debug=True)
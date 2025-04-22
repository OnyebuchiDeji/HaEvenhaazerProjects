from flask import Flask, redirect, url_for, render_template

"""
    HTML Templates.

    *The render_template module helps one grab an html file and render it as one's web page.

    1. In this version, content will be passed to the html file before it is displayed.
    2. Python code can be written inside the templates.
    
"""
app = Flask(__name__)


##  The root page usually treated as home
"""When I any string to the root http://127.0.0.1:5000, it replaces the content in <p>"""
@app.route("/<name>")
def home(name):
    ##  Notice! The parameters contentr and aVal are the same as those specified in the html!
    return render_template("index_v3B.html", word=name)


if __name__=="__main__":
    app.run()
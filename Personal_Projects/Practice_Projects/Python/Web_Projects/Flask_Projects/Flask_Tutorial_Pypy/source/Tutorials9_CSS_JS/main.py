"""
    Done: Fri-10-May-2024
    
    These are done:
    JS, CSS, Images

    1) Import custom CSS from style directory:
        Flask makes all static files will be saved in the folder called 'static'
        just like all dynamic files, the render templates, in folder 'template'
        b) Folders can be made within the static folder
    2) the JS is similar to how CSS is done!
    
"""

from flask import Flask, render_template


app = Flask(__name__)

##  This makes the routes '/' and 'home' refer to the same function `home`
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)

"""
    Contains the app's main configuration.

    Note that configurations are done before setting up databse models.

    ORDER: 1
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
"""
    CORS -- cross-origin requests: allows one send a request to the backend server from a different URL
    By default when a request is sent, the server is protected from requests from a different URL.
    This is because in this application, the fron-end is in a different server from the backend (NODE.js)...
    and it is essential for the frontend and backend to communicate (send requests).
    So for the communication to occur, it is needed to remove the CORS error that prevents the inter-server communication.
"""
from flask_cors import CORS ##  Cross-Origing requests



app = Flask(__name__)
##  Disables the CORS error to enable sending of cross-origin requests between the app's
##  frontend and backend servers
CORS(app)

##  Note that it is `='sqlite:///<database_name.db>'`
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
##  This specifies that not all modifications made to the database are not going to be tracked.
##  It makes things a little bit easier.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

##  Creaate an instance of the database
##  This database instance gives access to the database configured by the Flask app object
DB = SQLAlchemy(app)



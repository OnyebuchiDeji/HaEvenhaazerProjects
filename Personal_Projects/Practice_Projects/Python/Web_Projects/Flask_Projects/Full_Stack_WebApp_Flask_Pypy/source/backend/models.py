"""
    Contains the database models, through which one communicates with the database.
    Flask-SQLAlchemy involves creating a Python class represent entries or rows in the database, like a table,
    that has defined columns of data that the object will be storing.

    ORDER: 2
"""

from config import DB

class Contact(DB.Model):
    """
        This is a database model represented by a Python class. Hence using Python,
        the different fields of the object can be defined.

        Note that the id is auto-generated
    """
    ##______________THE FIELDS
    id = DB.Column(DB.Integer, primary_key=True)
    ##  nullable=False makes it impossible for the first_name to be a null value (None in Python)
    first_name = DB.Column(DB.String(80), unique=False, nullable=False)
    last_name = DB.Column(DB.String(80), unique=False, nullable=False)
    email = DB.Column(DB.String(120), unique=True, nullable=False)

    def to_json(self):
        """
            This takes all the fields above and converts them into a Python dicitonary.
            The dictionary can then be converted into JSON, which can then be passed
            from the API.
            JSON is the typical way of communicating data over a network.
            The API will return a JSON object and will be able to send JSON to the SQL database server
            to create the database objects.
            Also, to send to th Frontend in response to a request for one of the data
        """
        ##  Here, camelCase is used conventionally for JSON data field keys.
        ##  Snake case is th e convention for Python code
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
        }
        





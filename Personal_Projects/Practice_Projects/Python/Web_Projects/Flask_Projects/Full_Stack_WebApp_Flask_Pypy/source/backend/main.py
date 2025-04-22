"""
    Date: Tue-14-May-2024,
    Contains main routes/endpoints -- if the app was larger it would have bene segregated into multiple files.
    But the app is ok as is.

    Before writing, plan what different endpoints and routes needed for the app's API.
    Since it is a CRUD (Create, Read, Update, Delete) app, these routes are needed.

    Endpoints can be though of as target locations.

    #1   Create -- what is needed?
        Create endpoint requires these:
        first_name
        last_name
        email

    ##::## Requests: requests for something to happen;
        Types:
            GET -- to access a resource -- Read
            POST -- to create something new -- Create
            PUT/PATCH requests -- to update 
            DELETE requests
        Information sent in or alongside a request is most times in JSON format.
    Frontend sends a request to backend. Backend sends a response.
    Response contains these:
        1. Status:
            200 - Success
            404 - Not Found
            400 - Bad Requests
            403 - Forbidden
        2. JSON:
            Contains data
    
            
    #2  One would want to test their backend API before working on the frontend
        to ensure everything is working properly.
        Then afterwards, one can go to the frontend, make it pleasant, and make it interact
        with the backend API.

        POSTMAN is an app that enables you to test and API on it's virtual development server

    Even when the same details are repeated, an error indicating that the UNIQUE constraint failed
    is shown!
"""

##  jsonify to import json data
from flask import request, jsonify
from config import app, DB
from models import Contact



@app.route("/contacts", methods=["GET"])
def get_contacts():
    """
        This url endpoint uses only the GET method
    """
    ##  This uses the flask-sqlalchemy databaser to get all the contacts that exist in the
    ##  SQL contact database
    ##  But these contacts are Python objects.
    contacts = Contact.query.all()

    """ 
        Because they are Python objects, they cannot be returned to the frontend server
        So the need to be converted to JSON
        Map takes all the elements in the list and applies a function to them
        It iterates through the list, saving each element in the in x and applying it to the
        method, .to_json()
        But it returns a map object, hence why it's converted to a list
     """
    json_contacts = list(map(lambda x: x.to_json(), contacts))

    ##  The below creates a dictionary that uses the 'contact_objects' as
    ##  a keys, and the actual list of json_contacts as it's value
    return jsonify({"contacts": json_contacts})
    
@app.route("/create_contact", methods=["POST"])
def create_contacts():
    """
        These look at the JSON data returned from from `get_contacts`
        and they are used to create the contacts.

        If the keys below do not exist, None is given to each of the following variables.

        Not by default, error codes are 200 -- success
    """
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        ##  Sends error message and error code 400 standing for bad request.
        return (
            jsonify({"message": "you must include a first name, last name, and an email."})
            , 400)

    ##  Create new contact object with different fields
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)

    ##  Add it to the database
    ##  Put in try-except block due to errors
    try:
        ##  Add to staging area trying to commite
        DB.session.add(new_contact)
        ##  Actually update database
        DB.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    ##  If no errors occured, everything worked!
    return jsonify({"message": "User Created!"}), 201

@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    """
        To update, it is required to know what contact one is updating and
        the data one wants to update the contact item with.
        This route takes a number indicating the user id as a parameter.
        It is this user whose info will be updated.

        NOTE also that it uses method PATCH.
    """
    contact = Contact.query.get(user_id)

    if not contact:
        ##  Return 404 if contact is not found
        return jsonify({"message": "User not found."}), 404

    ## If contact's found:
    data = request.json
    """
        This modifies this contact's first name to be equal to what the JSON.
        The data.get(<key>, optional/default_value) looks for a key inside it's JSON data
        and returns the corresponding value.
        But if that key does not exist, it returns the optional_value specified.

        Here, we get the contact we want to update.
        Then we get the JSON data returned by `get_contacts()`
        We get that data and update the corresponding contact object.
    """
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)

    ##  Because this contact already exists in the session, no need to do
    ##  DB.session.add(contact)
    ##  Just commiting it is ok
    DB.session.commit()

    return jsonify({"message": "User Updated."}), 200

@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contacts(user_id):
    contact = Contact.query.get(user_id)
    
    if not contact:
        ##  Return 404 if contact is not found
        return jsonify({"message": "User not found."}), 404

    DB.session.delete(contact)
    DB.session.commit()

    return jsonify({"message": "User Deleted!"}), 200

if __name__=="__main__":
    with app.app_context():
        ##  The below creates all the different models that already exist
        DB.create_all()
    app.run(debug=True)


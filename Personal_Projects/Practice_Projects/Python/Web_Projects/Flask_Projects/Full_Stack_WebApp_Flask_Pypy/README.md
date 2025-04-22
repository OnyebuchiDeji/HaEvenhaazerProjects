Start Date: Sat-11-May-2024

Done following TWT on YT, "Python + JS Full Stack App Tutorial"

NOw: Mon-13-05-2024

To create a new React App via Node.js:

npm create vite@latest <folder_name> -- --template react

In this case, the <folder_name> was 'frontend'

So run the code to initialize the frontend end.

Then run these commands
cd frontend -- change to this directory first
npm install -- to install neccessary packages in the frontend directory.
npm run dev -- to run the code on the frontend server.

This app includes a CRUD backend:
Create Read Update Delete

THE BACKEND IS THE API

Here, these four main operations will be implemented for each object instance.
This object instance is the contact -- the contact (stored data object) can be created and stored, fetched,
updated and deleted.
These operations can be implemented by setting up different routes. these routes or endpoints can be called
from any type of application: another frontend or backend, aside from React.

This Project App's idea is to create the protocols or APIs (Application Programming Interfaces) that definet the set of
operations that the application has.
After this the frontend is structured to call the operations and can be beautified.

pip install Flask
pip install Flask-SQLAlchemy -- an ORM -- allows one to connect to an SQL database and map the entries in SQL into Python
objects quite easily using Python
pip install flask-cors -- allows one to have cross-origin requests -- requests between websites on different servers.
to help against the Same Origin Policy.


To run the code on the frontend server:
npm run dev

DONE: 14-05-2024
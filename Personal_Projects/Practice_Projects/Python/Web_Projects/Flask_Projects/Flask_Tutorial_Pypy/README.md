Done: Fri-22-March-2024


This project is for learning flask in python.
It was done following Tech With Tim Youtube

pip install flask to get the flask module

Flask acts like PHP: generating and manipulating html

Flask here simulates a server... thus it warns that it IS a development server.

Continued: Tue-1-May-2024

Continued: Fri-10-May-2024
pip install flask-sqlalchemy.


THE FLASK-SQLALCHEMY DOCUMENTATION IS SO SIMPLE:
I will use it for my own work!
https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/


Lastly, after tutorial10:

Install putty
https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html

Install winscp:
https://winscp.net/download/WinSCP-6.3.3-Setup.exe/download

These two are used to communicate with the linux server that we set up.


DONE: Sat-11-May-2024

Fixed an issue in the Tutorials10_Blueprints-DivisionalStructure.

Because of it, the stylesheets weren't linking.
This was the proper way to link style sheets when using blueprints from 
a file in a separate module:
    <link rel="stylesheet" href="{{url_for('home_page.static', filename='page_styles/image_styles.css')}}">
and for the image:
    <img src="{{url_for('home_page.static', filename='resources/images/kuruko_img-10052024.png')}}"></img>
    Note the name of the blue print is appended to the '.static'

But in Tutorials10_Blueprints-FunctionalStructure, this was not required...
because the main file with the actual Flask app and the blueprint and their static and
template folders were in the same package!

!!!DONE!!!
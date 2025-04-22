#   Date: Fri-26-July-2024


#   Briefing
Learning a lot about Kivy from Codemy

<br>

##  To Install
1. Make virtual environment
2. python -m pip install "kivy[base]" kivy_examples -- installs the minimum Kivy requirements
3. python -m pip install "kivy[full]" kivy_examples -- installs all features of Kivy, such as video/audio support.
    The second one installs all of Kivy, including its dependencies, like gstreamer, sdl2, opengl and/or angle.

##  Logs

### Installed `KvLang` from Monk3yDev for Kivy syntax highlighting.


###  Continued: mon-12-Aug-2024

####    Episode 40
    Google's KivyMD. 

    One can read through these to see what Google expects one to do with KivyMD.
    
    One Site at material.io/design
    The DOCS: https://kivymd.readthedocs.io/en/latest/
    Download Instructions at: https://github.com/kivymd/KivyMD

    To install it: 
        git clone https://github.com/kivymd/KivyMD.git --depth 1
        cd KivyMD
        pip install .


### Continued: Mon-19-Aug-2024
####    Episode 56: Using KivyMD and MySQL; Installing MySQL
    1.  Go to https://www.mysql.com/downloads/
    2.  Then scroll down and choose 'MySQL Community (GPL) Downloads', which redirects to
        https://dev.mysql.com/downloads/ <-- This is the free one
    3.  Then Click 'MySQL Community Server' or 'MySQL Installer for Windows', which redirects to https://dev.mysql.com/downloads/mysql/
    4.  However, it's best to download the MSI installer, rather than the ZIP file, and download the
        one with a bigger size.
    
    After installing MySQL and restarting my computer, install some connectors with PIP
    Why they are so many is because some work for one's device while others don't:

    ```pip install mysql-connector mysql-connector-python mysql-connector-python-rf```
    1.  mysql-connector
    2.  mysql-connector-python
    3.  mysql-connector-python-rf

    `
        Finally, when connecting to the database, put in the password for that root account used in Episode 56
        I probably will make more accounts just for this.
    `

####    Episode 57: Using KivyMD and Postgres; Installing the Heroku CLI
    Now, Postgres for this episode is used online in the cloud, not installed.

    This requires downloading the Heroku CLI, to allow the terminal to talk to Heroku.
    Heroku is a hosting service and has a free version.
    The free version of Postgres on Heroku empties itself at the end of a day. So anything thing
    that was in there gets deleted.

    Steps for Heroku:
        1.  Go to https://devcenter.heroku.com/articles/heroku-cli
        2.  Choose the 64-bit MSI installer
    
    After installing Heroku, install connector for Postgres, to allow connection to a Postgres DB:
        ```pip install psycopg2``` <-- psycho postgres 2.

    Then after these:
        1.  type `heroku login` in the command line. this will take one to the Login Page of Heroku CLI.
            Create a free account and Log in.
            They might ask for one's credit card to confirm the account.
        2.  To use the Postgres database from Heroku, one needs to create an app instance locally on
            one's device.
            Do this by running `heroku create`. Though this requires one to enter some Billing Information 
            Then the url generated in the CLI should be copied and pasted into the web browser Search Bar.
        3.  In the Python file, ```import psychopg2```
    Then to get the account information to connect to the DB:
        1.  Login to Heroku and look for the app by name; the name should be in the prior url
        2.  Click on the app.
        3.  Now, to add Postgres addons from the terminal, type:
            ```heroku addons:create heroku-postgresql:hobby-dev```
        4.  Then back in the web page you'll see that the addon has been added.
        5.  Click on the Postgres addon and got to `Settings`.
        6.  Then where it says 'Database Credentials', click 'View Credentials'. This lists all the things needed for the
            credentials to connect the Python app to the Postgres DB.
            Put them appropriately to the block of code that uses ``psycopg2` to connect to the database.
        
    `However, I couldn't do it at this time because for the part that requires Billing Information, there wasn't enough funds in the account then.`



#   Done: Tue-20-Aug-2024

#   Reference:
Codemy (2021),"Python GUI's With Kivy", Youtube (Playlist).
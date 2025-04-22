"""
    Date: Mon-19-Aug-2024

    This episode demonstrates the use of the MySQL and KivyMD

    Sqlite3 is not the kind used in Production. But it's useful 
    But MySQL is more powerful, and is prodiuction level

"""

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
import mysql.connector



#   Designate the .kv design file
Builder.load_file("base_style.kv")


class MyBoxLayout(MDBoxLayout):
    pass


#   The KivyMD app
class MyApp(MDApp):
    light_theme = False
    theme_text_l = "L"
    theme_text_d = "D"


    def build(self):
        self.title = "MySQL DB With KivyMD"
        Window.clearcolor = (0.3, 0.25, 0.3, 1)

        ##  Define Database Specs to Connect
        mydb = mysql.connector.connect(
            host = "localhost",     #  If DB is online, host will be an IP address
            user = "root",          #  root is the default user in MySQL
            passwd = "", #   Same used to set up one's MySQL. Enter the Password
            database = "mysql_db",
        )

        ##  Create a Cursor
        c = mydb.cursor()

        ##  Create an Actual Database ONLY if it exists
        c.execute("CREATE DATABASE IF NOT EXISTS mysql_db")

        ##  Check to see if the Database was created
        # c.execute("SHOW DATABASES")
        # for db in c:    ##  This lists all databases belonging to one's MySQL user account
        #     print(db)
        
        ##  Create a Table
        ##  customers is the table and `name` is the column
        c.execute("""CREATE TABLE if not exists customers(
            name VARCHAR(50))
        """)

        ##  Check to see if the Table was created
        # c.execute("SELECT * FROM customers")
        # print(c.description)            ##  This will print out the name of the table if it exists

        ##  Ensure to commit and close for the database to be saved here!
        mydb.commit()
        mydb.close()

        """ By Default, the light theme is used. """
        #   Set theme style and color palettes
        self.theme_cls.theme_style = "Light" if self.light_theme else "Dark"
        self.theme_cls.primary_palette = "Goldenrod"
        self.theme_cls.accent_palette = "skyblue"

        self.root = MyBoxLayout()
        return self.root

    def toggle_theme(self):
        self.light_theme = not self.light_theme
        self.theme_cls.theme_style = "Light" if self.light_theme else "Dark"
        self.root.ids.id_theme_btn.text = self.theme_text_l if self.light_theme else self.theme_text_d
    
    def submit_name(self):
        input_ref = self.root.ids.id_word_input
        diplay_label_ref = self.root.ids.id_word_label

        if len(input_ref.text) <= 1:
            diplay_label_ref.text = "[b][size=35]You've Entered Nothing Yet[/size][/b]"
            return

        mydb = mysql.connector.connect(
            host = "localhost",     #  If DB is online, host will be an IP address
            user = "root",          #  root is the default user in MySQL
            passwd = "", #   Same used to set up one's MySQL
            database = "mysql_db",
        )

        ##  Create a Cursor
        c = mydb.cursor()

        ##  Add a Record
        ##  The below means insert data into the 'name' column.
        sql_command = "INSERT INTO customers (name) VALUES (%s)"
        values = (input_ref.text, )
        
        ##  To Finally Execute the SQL Command
        c.execute(sql_command, values)

        #   Add a Little Message
        diplay_label_ref.text = f"[b][size=35]Added {input_ref.text}[/size][/b]" 
        
        #   Clear the Input Box
        input_ref.text = ""

        ##  Commit Changes  
        mydb.commit()

        ##  Close our Connection
        mydb.close()
        
    
    def show_records(self):
        """Shows Everything in Database and Adds to the Display Label"""
        display_label = self.root.ids.id_word_label

        mydb = mysql.connector.connect(
            host = "localhost",     #  If DB is online, host will be an IP address
            user = "root",          #  root is the default user in MySQL
            passwd = "", #   Same used to set up one's MySQL. Enter the Password
            database = "mysql_db",
        )

        ##  Create a Cursor
        c = mydb.cursor()

        ##  Add a Record. The * means everything in the Table customers
        c.execute("""SELECT * FROM customers""")
        records = c.fetchall()  ##  Returns a List of Tuples, a List of all the data in a row of the table

        ##  Did it to only get the first value, since only one calue is in each row
        ### The errors are not working right. The program still runs and compiles
        records = [name[0] for name in records]
        # print(type(records))
        # print(records)

        display_label.text = "[b][size=35]"+"\n".join(records)+"[/size][/b]"


    
if __name__ == "__main__":
    MyApp().run()



#   'Red', 'Pink', 'Purple', 'DeepPurple',
#   'Indigo', 'Blue', 'LightBlue', 'Cyan',
#   'Teal', 'Green', 'LightGreen', 'Lime',
#   'Yellow', 'Amber', 'Orange', 'DeepOrange',
#   'Brown', 'Gray', 'BlueGray'.

"""
ThemeManager.primary_palette must be one of:
 ['Aliceblue', 'Antiquewhite', 'Aqua', 'Aquamarine', 'Azure', 'Beige', 'Bisque', 'Black', 'Blanchedalmond',
 'Blue', 'Blueviolet', 'Brown', 'Burlywood', 'Cadetblue', 'Chartreuse', 'Chocolate', 'Coral', 'Cornflowerblue',
 'Cornsilk', 'Crimson', 'Cyan', 'Darkblue', 'Darkcyan', 'Darkgoldenrod', 'Darkgray', 'Darkgrey', 'Darkgreen',
 'Darkkhaki', 'Darkmagenta', 'Darkolivegreen', 'Darkorange', 'Darkorchid', 'Darkred', 'Darksalmon', 'Darkseagreen', 'Darkslateblue',
 'Darkslategray', 'Darkslategrey', 'Darkturquoise', 'Darkviolet', 'Deeppink', 'Deepskyblue', 'Dimgray', 'Dimgrey',
 'Dodgerblue', 'Firebrick', 'Floralwhite', 'Forestgreen', 'Fuchsia', 'Gainsboro', 'Ghostwhite', 'Gold', 'Goldenrod', 'Gray',
 'Grey', 'Green', 'Greenyellow', 'Honeydew', 'Hotpink', 'Indianred', 'Indigo', 'Ivory', 'Khaki', 'Lavender', 'Lavenderblush',
 'Lawngreen', 'Lemonchiffon', 'Lightblue', 'Lightcoral', 'Lightcyan', 'Lightgoldenrodyellow', 'Lightgreen', 'Lightgray', 'Lightgrey',
 'Lightpink', 'Lightsalmon', 'Lightseagreen', 'Lightskyblue', 'Lightslategray', 'Lightslategrey', 'Lightsteelblue', 'Lightyellow', 'Lime',
 'Limegreen', 'Linen', 'Magenta', 'Maroon', 'Mediumaquamarine', 'Mediumblue', 'Mediumorchid', 'Mediumpurple', 'Mediumseagreen', 'Mediumslateblue',
 'Mediumspringgreen', 'Mediumturquoise', 'Mediumvioletred', 'Midnightblue', 'Mintcream', 'Mistyrose', 'Moccasin', 'Navajowhite', 'Navy', 'Oldlace',
 'Olive', 'Olivedrab', 'Orange', 'Orangered', 'Orchid', 'Palegoldenrod', 'Palegreen', 'Paleturquoise', 'Palevioletred', 'Papayawhip', 'Peachpuff', 'Peru',
 'Pink', 'Plum', 'Powderblue', 'Purple', 'Red', 'Rosybrown', 'Royalblue', 'Saddlebrown', 'Salmon', 'Sandybrown', 'Seagreen', 'Seashell', 'Sienna', 'Silver',
 'Skyblue', 'Slateblue', 'Slategray', 'Slategrey', 'Snow', 'Springgreen', 'Steelblue', 'Tan', 'Teal', 'Thistle', 'Tomato', 'Turquoise', 'Violet', 'Wheat', 'White',
 'Whitesmoke', 'Yellow', 'Yellowgreen']
"""



"""
    This is a larger GUI app that implements a login form, enables changing screen, and saves the information of added accounts
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase



class CreateAccountWindow(Screen):
    nameVar = ObjectProperty(None)
    emailVar = ObjectProperty(None)
    passwordVar = ObjectProperty(None)

    def submit(self):
        if self.nameVar.text != "" and self.emailVar.text != "" and self.emailVar.text.count("@") == 1 and self.emailVar.text.count(".") > 0:
            if self.passwordVar != "":
                db.add_user(self.emailVar.text, self.passwordVar.text, self.nameVar.text)
                self.reset()
                ##  Refers to current screen
                sm.current = "login"
            else:
                invalidForm()
        
        else:
            invalidForm()
    
    def login(self):
        self.reset()
        ##  Refers to current screen
        sm.current = "login"
    
    def reset(self):
        self.emailVar.text = ""
        self.passwordVar.text = ""
        self.nameVar.text = ""

class LoginWindow(Screen):
    emailVar = ObjectProperty(None)
    passwordVar = ObjectProperty(None)

    def loginBtn(self):
        ##  On login, when the button is pressed
        #3  if the email and password are valid, that is, they exist in database
        if db.validate(self.emailVar.text, self.passwordVar.text):
            """
                Change the screen to the after-login screen
                Refers to the current email variable
                Also, note that this variable is a class variable, not a member.
                This is why it can be accessed the way it is:
                MainWindow.currentVar = self.emailVar.text
            """
            MainWindow.currentVar = self.emailVar.text
            self.reset()
            ##  Refers to current screen
            sm.current = "main"
        else:
            invalidLogin()
    
    def createBtn(self):
        self.reset()
        sm.current = "create"
        
    def reset(self):
        self.emailVar.text = ""
        self.passwordVar.text = ""

class MainWindow(Screen):
    account_name = ObjectProperty(None)
    createdVar = ObjectProperty(None)
    emailVar = ObjectProperty(None)
    currentVar = ""

    def logOut(self):
        sm.current = "login"
    
    """
        on_enter is a predefined method inherited from the Screen class
        So here, I overload it! This is the reason why you cannot find it called anywhere.
        It is because, immediately you login from the login window, the instructions in heere are called!
    """

    def on_enter(self, *args):
        password, name, created = db.get_user(self.currentVar)
        self.account_name.text = "Account Name: " + name
        self.emailVar.text = "Email: " + self.currentVar
        self.createdVar.text = "Created On: " + created


class WindowManager(ScreenManager):
    pass

def invalidLogin():
    pop = Popup(title="Invalid Login",
                    content=Label(text="Invalid username or password."),
                    size_hint=(None, None), size=(400, 400))
    pop.open()

def invalidForm():
    pop = Popup(title="Invalid Form",
                    content=Label(text="Please fill in all inputs with valid information!"),
                    size_hint=(None, None), size=(400, 400))
    pop.open()

kv = Builder.load_file("app11_guiapp.kv")

##  screen manager
sm = WindowManager()
db = DataBase("source/users.txt")

screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"), MainWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)

##  Current is the property that determines which screen is being rendered
## sm.current = "login" makes the program to start from the login screen
sm.current = "login"
sm.current_screen

class GUIApp11(App):
    def build(self):
        return sm

if __name__ == "__main__":
    GUIApp11().run()
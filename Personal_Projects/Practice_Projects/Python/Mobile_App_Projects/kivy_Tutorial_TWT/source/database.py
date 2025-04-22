import datetime

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()
    
    def load(self):
        self.file = open(self.filename, "r")
        self.users = {}
    
        for line in self.file:
            email, password, name, created = line.strip().split(";")
            self.users[email] = (password, name, created)
        
        self.file.close()
    
    def get_user(self, email):
        if email in self.users:
            return self.users[email]
        else:
            ##  -1 indicates that user is not found
            print("No such user exists!")
            return -1
        
    def add_user(self, email, password, name):
        ##  This line of code checks if the key exists in the dictionary!
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), name.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            print("Email exists already!")
            return -1
    
    def validate(self, email, password):
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else:
            return False
    
    def save(self):
        """
            This saves every data that has been loaded into the users dictionary when the app starts up.
            Note that it is called every time a new user is added.
            Note that it does not append but writes, meaning it clears and writes to the file again!
        """
        with open(self.filename, "w") as f:
            ##  the user is the email, which is always unique, and so is used as the dictionary's key!
            for user in self.users:
                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + "\n")
    
    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]
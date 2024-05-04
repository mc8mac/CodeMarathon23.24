import csv

class User:
    def __init__(self, istid,name, password):
        self.istid = istid
        self.name = name
        self.password = password
        self.reviews = []

    def __str__(self):
        """
        String representation of the User object.
        """
        return f"User: {self.name}, ISTID: {self.istid}"
    
class UserDB:
    def __init__(self, filename='userdb.csv'):
        self.users = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                name, istid, password = row
                self.users.append(User(istid, name, password))
                

    def add_user(self, user):
        """
        Adds a user to the database.
        """
        with open('userdb.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([user.name, user.istid, user.password])
        
        print(f"User added: {user}")

    def get_users(self):
        """
        Returns the list of users in the database.
        """
        return self.users
    
    def find_user(self, istid):
        """
        Finds a user in the database by their ISTID.
        """
        for user in self.users:
            if str(user.istid) == str(istid):
                return user
        return None

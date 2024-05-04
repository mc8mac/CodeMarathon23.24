import csv

class User:
    def __init__(self, istid,name, password):
        self.istid = istid
        self.name = name
        self.password = password
        self.reviews = []

    def add_review(self, review):
        """
        Adds a review to the user's list of reviews.
        """
        self.reviews.append(review)
        print(f"Review added: {review}")

    def get_reviews(self):
        """
        Returns the list of reviews for the user.
        """
        return self.reviews

    def __str__(self):
        """
        String representation of the User object.
        """
        return f"User: {self.name}, ISTID: {self.istid}"


class Driver(User):
    def __init__(self, istid, name, password):
        super().__init__(istid,name, password)
        self.vehicles = []

    def add_vehicle(self, brand, model, year):
        """
        Adds a vehicle to the driver's list of vehicles.
        """
        vehicle = Vehicle(brand, model, year)
        self.vehicles.append(vehicle)
        print(f"Vehicle added: {vehicle}")

    def get_vehicles(self):
        """
        Returns the list of vehicles for the driver.
        """
        return self.vehicles

    def __str__(self):
        """
        String representation of the Driver object.
        """
        return f"Driver: {self.name}, Vehicles: {self.vehicles}"


class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        """
        String representation of the Vehicle object.
        """
        return f"{self.brand} {self.model} ({self.year})"



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

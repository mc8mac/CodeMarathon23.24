class User:
    def __init__(self, istid,name, password):
        self.istid = istid
        self.name = name
        self.password = password # Note: In a real system, this should be hashed and not stored in plain text
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

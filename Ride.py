from datetime import datetime

class Ride:
    def __init__(self, driver, origin, destination, date_time):
        self.driver = driver
        self.origin = origin
        self.destination = destination
        self.date_time = datetime.strptime(date_time, '%Y-%m-%d %H:%M') # YYYY-MM-DD HH:MM
        self.passengers = []

    def add_passenger(self, passenger):
        """
        Adds a passenger to the ride.
        """
        self.passengers.append(passenger)
        print(f"{passenger.name} has been added to the ride.")

    def remove_passenger(self, passenger):
        """
        Removes a passenger from the ride.
        """
        if passenger in self.passengers:
            self.passengers.remove(passenger)
            print(f"{passenger.name} has been removed from the ride.")
        else:
            print(f"{passenger.name} is not in the ride.")

    def get_ride_details(self):
        """
        Returns a string with the ride's details.
        """
        return f"Driver: {self.driver.name}, Origin: {self.origin}, Destination: {self.destination}, Date and Time: {self.date_time.strftime('%Y-%m-%d %H:%M')}"

    def __str__(self):
        """
        String representation of the Ride object.
        """
        return self.get_ride_details()

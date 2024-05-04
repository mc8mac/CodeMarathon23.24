from Car import CarDB
from User import UserDB
from Ride import RideDB
from datetime import datetime

class DB:
    def __init__(self):
        self.car_db = CarDB()
        self.user_db = UserDB()
        self.ride_db = RideDB()

    def schedule_ride(self, user, car):
        """
        Schedules a rid.
        """
        origin = input("Enter origin: ")
        destination = input("Enter destination: ")
        date_time = input("Enter date and time (YYYY-MM-DD HH:MM): ")
        ride = self.ride_db.add_ride(user, origin, destination, date_time, car)
        print(f"Ride scheduled: {ride}")
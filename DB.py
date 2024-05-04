from Car import CarDB
from User import UserDB
from Ride import RideDB
from datetime import datetime

class DB:
    def __init__(self):
        self.car_db = CarDB()
        self.user_db = UserDB()
        self.ride_db = RideDB()
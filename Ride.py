import csv

class Ride:
    def __init__(self, driver, origin, destination, date_time, license_plate, ride_id, seats, passengers = [], stops = []):

        self.ride_id = ride_id
        self.driver = driver
        self.origin = origin
        self.destination = destination
        self.date_time = date_time
        self.license_plate = license_plate
        self.seats = seats
        self.passengers = passengers
        self.stops = stops

    def add_passenger(self, user):
        self.passengers.append(user.istid)
        
    def add_stop(self, stop):
        self.stops.append(stop)

    def __str__(self):
        return f"{self.origin} -> {self.destination} ({self.date_time}), Driver: {self.driver}, Car: {self.license_plate}, Stops: {self.stops}"

class RideDB:
    def __init__(self, filename='ridedb.csv'):
        self.rides = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                ride_id, driver, origin, destination, date_time, car, seats, passengers, stops = row
                passengers = passengers.split(', ') if passengers else []
                stops = stops.split(', ') if stops else []
                self.rides.append(Ride(driver, origin, destination, date_time, car , ride_id, seats, passengers, stops))

    def add_ride(self, driver, origin, destination, date_time, car):
        ride_id = len(self.rides) + 1
        ride = Ride(driver.istid, origin, destination, date_time, car.license_plate, ride_id, car.seats)
        self.rides.append(ride)
        return ride
    
    def get_rides(self):
        return self.rides
    
    def get_ride_by_id(self, ride_id):
        for ride in self.rides:
            if ride.ride_id == ride_id:
                return ride
        return None
    
    def find_ride(self, origin, destination):
        for ride in self.rides:
            if ride.origin == origin and ride.destination == destination:
                return ride
        return None
    
    def get_rides_by_driver(self, driver):
        rides = []
        for ride in self.rides:
            if ride.driver == driver.istid:
                rides.append(ride)
        return rides
    
    def get_rides_by_passenger(self, passenger):
        rides = []
        for ride in self.rides:
            if passenger in ride.passengers:
                rides.append(ride)
        return rides

    def save(self):
        with open('ridedb.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ride_id', 'driver', 'origin', 'destination', 'date_time', 'car', 'seats', 'passengers', 'stops'])
            for ride in self.rides:
                writer.writerow([ride.ride_id, ride.driver, ride.origin, ride.destination, ride.date_time, ride.license_plate, ride.seats, ', '.join(ride.passengers), ', '.join(ride.stops)])
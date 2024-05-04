import csv

class Ride:
    def __init__(self, driver, origin, destination, date_time, car, ride_id, passengers = [], stops = []):

        self.ride_id = ride_id
        self.driver = driver
        self.origin = origin
        self.destination = destination
        self.date_time = date_time
        self.car = car.license_plate
        self.seats = car.seats
        self.passengers = passengers
        self.stops = stops

    def add_passenger(self, user):
        self.passengers.append(user.istid)
        print(f"Passenger added: {user.istid}")

        # Read the entire file into memory
        with open('ridedb.csv', 'r') as file:
            data = list(csv.reader(file))

        # Update the relevant row
        for row in data:
            if int(row[0]) == self.ride_id:
                row[6] = ', '.join(self.passengers)

        # Write the data back to the file
        with open('ridedb.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        
    
    def add_stop(self, stop):
        self.stops.append(stop)
        print(f"Stop added: {stop}")

        # Read the entire file into memory
        with open('ridedb.csv', 'r') as file:
            data = list(csv.reader(file))

        # Update the relevant row
        for row in data:
            if int(row[0]) == self.ride_id:
                row[7] = ', '.join(self.stops)

        # Write the data back to the file
        with open('ridedb.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def __str__(self):
        return f"{self.origin} -> {self.destination} ({self.date_time}), Driver: {self.driver}, Car: {self.car}, Stops: {self.stops}, Seats Left: {int(self.seats) - len(self.passengers)}"

class RideDB:
        
        def __init__(self, filename='ridedb.csv'):
            self.rides = []
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    ride_id, driver, origin, destination, date_time, car, seats, passengers, stops = row
                    self.rides.append(Ride(driver, origin, destination, date_time, car, seats , ride_id, passengers, stops))
        
        def add_ride(self, driver, origin, destination, date_time, car):
            ride_id = len(self.rides) + 1
            ride = Ride(driver, origin, destination, date_time, car, ride_id)
            self.rides.append(ride)
            with open('ridedb.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([ride_id, driver, origin, destination, date_time, car, '', ''])
            print(f"Ride added: {ride}")
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
                if ride.driver == driver:
                    rides.append(ride)
            return rides
        
        def get_rides_by_passenger(self, passenger):
            rides = []
            for ride in self.rides:
                if passenger in ride.passengers:
                    rides.append(ride)
            return rides
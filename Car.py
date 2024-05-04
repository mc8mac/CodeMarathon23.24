import csv

class Car():
    def __init__(self, brand, model, license_plate, color, seats, istid):
        self.brand = brand
        self.model = model
        self.license_plate = license_plate
        self.color = color
        self.seats = seats
        self.istid = istid
    
    def __str__(self):
        return f"{self.color} {self.brand} {self.model} [{self.license_plate}] with {self.seats} seats"
    
class CarDB:
    
    def __init__(self, filename='carsdb.csv'):
        self.cars = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                istid, brand, model, license_plate, color, seats = row
                self.cars.append(Car(brand, model, license_plate, color, seats, istid))

    def add_car(self, car):
        self.cars.append(car)
        with open('carsdb.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([car.istid, car.brand, car.model, car.license_plate, car.color, car.seats])
        print(f"Car added: {car}")

    def get_cars(self):
        return self.cars
    
    def get_car_by_id(self, istid):
        for car in self.cars:
            if car.istid == istid:
                return car
        return None
    
    def find_car(self, license_plate):
        for car in self.cars:
            if car.license_plate == license_plate:
                return car
        return None
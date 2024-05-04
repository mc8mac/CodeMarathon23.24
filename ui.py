from DB import DB
from User import User
from Car import Car
from Ride import Ride
from Review import Review
from datetime import datetime as dt
import hashlib

db = DB()

def main():
    while True:
        print("Welcome to Shutless!")
        print("1 -> Create an Account")
        print("2 -> Log In")
        print("q -> Exit")
        choice = input()
        if choice == "1":
            create_account()
            continue
        elif choice == "2":
            user = login()
            if user:
                app(user)
                return
            continue
        elif choice == "q":
            return
        else:
            print("Invalid choice. Please try again.\n")
            
            
def create_account():
    name = input("Enter your name: ")
    istid = input("Enter your ISTID: ")
    password = input("Enter your password: ")
    isDriver = input("Registering as a Driver? (y/n): ")
    print()
    
    if not name or not istid or not password:
        print("All fields are required. Please try again.\n")
        create_account()
        return

    if db.user_db.find_user(istid):
        print("User already exists. Please try again.\n")
        create_account()
        return
    
    user = User(istid, name, hashlib.sha256(password.encode()).hexdigest())
    
    if isDriver == "y":
        brand = input("Enter your car brand: ")
        model = input("Enter your car model: ")
        license_plate = input("Enter your car license plate: ")
        color = input("Enter your car color: ")
        seats = input("Enter your car seats: ")
        car = Car(brand, model, license_plate, color, seats, istid)
        db.car_db.add_car(car)
        
    db.user_db.add_user(user)
    print("Account created successfully!\n")
    return


def login():
    istid = input("Enter your ISTID: ")
    password = input("Enter your password: ")
    print()
    
    if not istid or not password:
        print("All fields are required. Please try again.\n")
        login()
        return
    
    user = db.user_db.find_user(istid)
    
    if not user:
        print("User not found. Please try again.\n")
        login()
        return
    
    if user.password != hashlib.sha256(password.encode()).hexdigest():
        print("Incorrect password. Please try again.\n")
        login()
        return
    
    print(f"Welcome, {user.name}!\n")
    return user

def add_ride(user):
    origin = input("Enter the origin: ")
    destination = input("Enter the destination: ")
    date_time = input("Enter the date and time (YYYY-MM-DD HH:MM): ")
    db.ride_db.add_ride(user, origin, destination, date_time, db.car_db.get_car_by_id(user.istid))
    return

def view_rides(user, previous=False):
    rides = db.ride_db.get_rides_by_driver(user)

    if previous:
        rides = [ride for ride in rides if dt.strptime(ride.date_time, '%Y-%m-%d %H:%M') < dt.now()]
    else:
        rides = [ride for ride in rides if dt.strptime(ride.date_time, '%Y-%m-%d %H:%M') > dt.now()]
    
    for ride in rides:
        print(ride)

    print()
    return

def search_rides(user):
    origin = input("Enter the origin: ")
    destination = input("Enter the destination: ")
    date_time = input("Enter the date and time (YYYY-MM-DD HH:MM): ")
    rides = db.ride_db.get_rides(origin, destination, date_time)
    rides = [print(ride) for ride in rides if dt.strptime(ride.date_time, '%Y-%m-%d %H:%M') > dt.now()]

def view_my_rides(user):
    rides = db.ride_db.get_rides_by_passenger(user.istid)
    for ride in rides:
        print(ride)
    print()

def add_review(user):
    ride_id = input("Enter the ride ID: ")
    rating = input("Enter your rating (1-5): ")
    comment = input("Enter your comment: ")
    review = Review(user.istid, ride_id, rating, comment)
    db.review_db.add_review(review)
    print("Review added successfully!\n")


def app(user):
    
    if db.car_db.get_car_by_id(user.istid):
        while True:
            print("1 -> Schedule a ride")
            print("2 -> View Scheduled Rides")
            print("3 -> View Completed Rides")
            print("4 -> View Driver Reviews")
            print("5 -> View Reviews")
            print("q -> Logout")
            print()
            
            choice = input()
            
            if choice == "1": # Add a Ride
                add_ride(user)
                continue
            
            elif choice == "2": # View Rides
                view_rides(user)
                continue
            
            elif choice == "3": # View Previous Rides
                view_rides(user, True)
                continue
            
            elif choice == "4": # View User Reviews
                db.review_db.view_user_reviews(user)
                continue
            
            elif choice == "5": # View User Reviews
                db.review_db.view_user_reviews(user)
                continue
            
            elif choice == "q": # Quit
                main()
                return
            else:
                print("Invalid choice. Please try again.\n")
    
    else:
        while True:
            print("1 -> Search rides")
            print("2 -> View my rides")
            print("3 -> View my reviews")
            print("4 -> Leave a review")
            print("q -> Exit")
            choice = input()
            if choice == "1":
                search_rides(user)
            elif choice == "2":
                view_my_rides(user)
            elif choice == "3":
                db.review_db.view_user_reviews(user)
            elif choice == "4":
                add_review(user)
            elif choice == "q":
                break
            else:
                print("Invalid choice. Please try again.\n")


main()
db.save()

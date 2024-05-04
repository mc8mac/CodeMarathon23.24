from DB import DB
from User import User
from Car import Car
from Ride import Ride
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
            continue
        elif choice == "q":
            break
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

def app(user):
    if db.car_db.get_car_by_id(user.istid):
        while True:
            print("1 -> Schedule a ride")
            print("2 -> View rides")
            print("3 -> View Driver Reviews")
            print("4 -> View Reviews")
            print("q -> Logout")
            choice = input()
            if choice == "1":
                db.ride_db.schedule_ride(user, db.car_db.get_car_by_id(user.istid))
                continue
            elif choice == "2":
                db.ride_db.view_rides(user)
                continue
            elif choice == "3":
                db.review_db.view_driver_reviews(user)
                continue
            elif choice == "4":
                db.review_db.view_user_reviews(user)
                continue
            elif choice == "q":
                main()
            else:
                print("Invalid choice. Please try again.\n")
    
    while True:
        print("1 -> Add a ride")
        print("2 -> View rides")
        print("3 -> View reviews")
        print("q -> Exit")
        choice = input()
        if choice == "1":
            db.add_ride(user)
            continue
        elif choice == "2":
            db.view_rides(user)
            continue
        elif choice == "3":
            db.add_review(user)
            continue
        elif choice == "q":
            break
        else:
            print("Invalid choice. Please try again.\n")

main()

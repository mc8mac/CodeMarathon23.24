from User import *
import hashlib

UserDB = UserDB()

def main():
    while True:
        print("Welcome to Shutless!")
        print("1 -> Create an Account")
        print("2 -> Log In")
        print("q -> Exit")
        choice = input()
        if choice == "1":
            
            create_account()
            login()
            break
            
        elif choice == "2":
            login()
            break
            
        elif choice == "q":
            break
        else:
            print("Invalid choice. Please try again.\n")
            
def create_account():
    name = input("Enter your name: ")
    istid = input("Enter your ISTID: ")
    password = input("Enter your password: ")
    print()
    
    if not name or not istid or not password:
        print("All fields are required. Please try again.\n")
        create_account()
        return

    if UserDB.find_user(istid):
        print("User already exists. Please try again.\n")
        create_account()
        return
    
    user = User(istid, name, hashlib.sha256(password.encode()).hexdigest())
    UserDB.add_user(user)
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
    
    user = UserDB.find_user(istid)
    if not user:
        print("User not found. Please try again.\n")
        login()
        return
    
    if user.password != hashlib.sha256(password.encode()).hexdigest():
        print("Incorrect password. Please try again.\n")
        login()
        return
    
    print(f"Welcome, {user.name}!\n")
    return

main()
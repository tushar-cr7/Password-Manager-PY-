import hashlib
import os

def encode(text):
    return hashlib.sha256(text.encode()).hexdigest()

def set_master():
    pwd = input("Set master password: ")
    with open("data.txt", "w") as f:
        f.write(encode(pwd) + "\n")

def verify_master():
    pwd = input("Enter master password: ")
    with open("data.txt", "r") as f:
        return encode(pwd) == f.readline().strip()

def add_password():
    site = input("Website: ")
    user = input("Username: ")
    pwd = input("Password: ")
    with open("data.txt", "a") as f:
        f.write(site + "|" + user + "|" + encode(pwd) + "\n")
    print("Saved")

def view_passwords():
    with open("data.txt", "r") as f:
        lines = f.readlines()[1:]
        if not lines:
            print("No records found")
        for line in lines:
            site, user, pwd = line.strip().split("|")
            print(site, "-", user, "-", pwd)

if not os.path.exists("data.txt"):
    set_master()

if verify_master():
    while True:
        print("\n1.Add Password\n2.View Passwords\n3.Exit")
        choice = input("Choice: ")
        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            break
else:
    print("Access denied")

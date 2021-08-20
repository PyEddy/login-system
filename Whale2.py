from login import username
from login import password


class SignIn:
    Whale_version = "1.0"
    user = input("Enter your username: ")
    passkey = input("Enter your password: ")

    while user != username or passkey != password:
        print("Wrong username or password")
        user = input("Enter your username: ")
        passkey = input("Enter your password: ")
    else:
        print("You are logged in")
        input()


import Home
Home

input()

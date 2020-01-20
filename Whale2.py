from Whale import username
from Whale import password


class SignIn:
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






from login import User

username = [User.user1, User.user2]
password = [User.password1, User.password2]
print(username[1])
print(password[0])
users = 0
userPass = 0

class SignIn:
    global users, userPass
    Whale_version = "1.1"
    user = input("Enter your username: ")
    passkey = input("Enter your password: ")
    if user == username[0] and passkey == password[0]:
        users = 0
        userPass = 0
    if user == username[1] and passkey == password[1]:
        users = 1
        userPass = 1

    while user != username[users] or passkey != password[userPass]:
        print("Wrong username or password")
        user = input("Enter your username: ")
        passkey = input("Enter your password: ")
    else:
        print("You are logged in")
        input()


username = username[users]
password = password[userPass]
print(username)
print(password)

import Home

Home

input()

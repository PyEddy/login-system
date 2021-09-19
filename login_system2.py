from login import User

try:
    username = [User.user1, User.user2]
    password = [User.password1, User.password2]
    identity = [User.identity1, User.identity2]
    Browser = [User.browser1, User.browser2]
except:
    username = [User.user1]
    password = [User.password1]
    identity = [User.identity1]
    Browser = [User.browser1]
users = 0
userPass = 0
user_identity = 0
user_browser = 0
global user, passkey


def login():
    global users, userPass, user_identity, user_browser, user, passkey
    user = input("Enter your username: ")
    passkey = input("Enter your password: ")
    if user == username[0] and passkey == password[0]:
        users = 0
        userPass = 0
        user_identity = 0
        user_browser = 0
    try:
        if user == username[1] and passkey == password[1]:
            users = 1
            userPass = 1
            user_identity = 1
            user_browser = 1
    except:
        pass


class SignIn:
    global users, userPass, user_identity, user_browser, user, passkey
    login_system_version = "1.2"
    login()

    while user != username[users] or passkey != password[userPass]:
        print("Wrong username or password")
        login()
    else:
        print("You are logged in")
        input()


username = username[users]
password = password[userPass]
identity = identity[user_identity]
Browser = Browser[user_browser]

import Home

Home

input()

import configparser

global user, passkey

userID = 0


def login():
    global username, password, identity, OperatingSystem, Browser
    config = configparser.RawConfigParser()
    config.read('login.txt')
    username = config.get(str(userID), 'username')
    password = config.get(str(userID), 'password')
    identity = config.get(str(userID), "identity")
    OperatingSystem = config.get(str(userID), 'OperatingSystem')
    Browser = config.get(str(userID), 'Browser')


class UserLogins:
    global userID
    user = input("Enter your username: ")
    passkey = input("Enter your password: ")
    userID = userID + 1
    login()
    userID = 0
    while user != username or passkey != password:
        try:
            userID = userID + 1
            login()
        except:
            userID = 0
            print("Username or password not found")
            user = input("Enter your username: ")
            passkey = input("Enter your password: ")
    else:
        userID = 0
        print("You are logged in")


username = username
password = password
identity = identity
OperatingSystem = OperatingSystem
Browser = Browser
user = username
passkey = password

import Home

Home

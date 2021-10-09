import random
import configparser
import glob

Whale_User = glob.glob('login.txt')
for file in Whale_User:
    with open(file, 'r') as f:
        file_code = f.readlines()

    check = False

    for line in file_code:
        if line == "[0]\n":
            check = True
            print("You have already went through the setup")
            import login
            login
            input()
            exit()
    if not check:
        print("1. Start setup of a user")
        print("2. Skip setup")
        number = input("Enter a number: ")
        if number == "1":
            print("Starting User Setup Process")
        if number == "2":
            import login
            login
        else:
            pass

username = input("Create a username: ")
password = input("Create a password: ")
identity = random.randint(0, 1000)


def User():
    config = configparser.RawConfigParser()
    config.add_section('System')
    config.set('System', 'userid', userID)

    with open("system.txt", "a") as saveFile:
        config.write(saveFile)


def Users():
    config = configparser.ConfigParser()
    config.read('system.txt')
    config.set('System', 'userid', str(userID))

    with open("system.txt", "w") as f:
        config.write(f)


try:
    config = configparser.RawConfigParser()
    config.read('system.txt')
    userID = config.get('System', 'userid')
    userID = int(userID) + 1
    Users()
except:
    userID = 0
    userID = userID + 1
    User()

print("This is your username: " + username)
print("This is your password: " + password)


class Information:
    OperatingSystem = input("What operating system are you using: ")
    Browser = input("What browser do you use: ")
    config = configparser.RawConfigParser()
    config.add_section(str(userID))
    config.set(str(userID), 'username', username)
    config.set(str(userID), 'password', password)
    config.set(str(userID), 'identity', identity)
    config.set(str(userID), 'OperatingSystem', OperatingSystem)
    config.set(str(userID), 'Browser', Browser)

    with open("login.txt", "a") as saveFile:
        config.write(saveFile)


import login

login

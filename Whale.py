import random
import configparser
import glob


Whale_User = glob.glob('login.txt')
for file in Whale_User:
    with open(file, 'r') as f:
        file_code = f.readlines()

    check = False

    for line in file_code:
        if line == "[login]\n":
            check = True
            print("You have already went through the setup")
            input()
            exit()
    if not check:
        print("Starting User Setup Process")

username = input("Create a username: ")
password = input("Create a password: ")
identity = random.randint(0, 1000)
userID = 0

userID = userID + 1
print("This is your username: " + username)
print("This is your password: " + password)


class Information:
    OperatingSystem = input("What operating system are you using: ")
    Browser = input("What browser do you use: ")
    config = configparser.RawConfigParser()
    # config.add_section('login')
    # config.add_section('security')
    config.add_section(str(userID))
    config.set(str(userID), 'username', username)
    config.set(str(userID), 'password', password)
    config.set(str(userID), 'identity', identity)
    # config.set('security', 'OperatingSystem', OperatingSystem)
    # config.set('security', 'Browser', Browser)

    with open("login.txt", "a") as saveFile:
        config.write(saveFile)


import Home
Home

import random
import configparser

username = input("Create a username: ")
password = input("Create a password: ")
identity = random.randint(0, 1000)


print("This is your username: " + username)
print("This is your password: " + password)


class Information:
    OperatingSystem = input("What operating system are you using: ")
    Browser = input("What browser do you use: ")
    config = configparser.RawConfigParser()
    config.add_section('login')
    config.add_section('security')
    config.set('login', 'username', username)
    config.set('login', 'password', password)
    config.set('login', 'identity', identity)
    config.set('security', 'OperatingSystem', OperatingSystem)
    config.set('security', 'Browser', Browser)

    with open("login.txt", "a") as saveFile:
        config.write(saveFile)


import Home
Home

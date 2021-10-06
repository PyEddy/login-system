import configparser

global user1, password1, user2, password2


userID = 1

config = configparser.RawConfigParser()
config.read('login.txt')
username = config.get(str(userID), 'username')
password = config.get(str(userID), 'password')
identity = config.get(str(userID), "identity")
OperatingSystem = config.get(str(userID), 'OperatingSystem')
Browser = config.get(str(userID), 'Browser')

class User:
    user1 = username
    password1 = password
    identity1 = identity
    browser1 = Browser
    userID = userID + 1
    try:
        config = configparser.RawConfigParser()
        config.read('login.txt')
        username = config.get(str(userID), 'username')
        password = config.get(str(userID), 'password')
        identity = config.get(str(userID), "identity")
        OperatingSystem = config.get(str(userID), 'OperatingSystem')
        Browser = config.get(str(userID), 'Browser')
        user2 = username
        password2 = password
        identity2 = identity
        browser2 = Browser
    except:
        pass


from login_system2 import SignIn

SignIn

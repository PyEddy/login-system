import configparser

global user1, password1, user2, password2

config = configparser.RawConfigParser()
config.read('login.txt')
username = config.get('1', 'username')
password = config.get('1', 'password')
identity = config.get('1', "identity")
OperatingSystem = config.get('1', 'OperatingSystem')
Browser = config.get('1', 'Browser')

class User:
    user1 = username
    password1 = password
    identity1 = identity
    browser1 = Browser
    try:
        config = configparser.RawConfigParser()
        config.read('login.txt')
        username = config.get('2', 'username')
        password = config.get('2', 'password')
        identity = config.get('2', "identity")
        OperatingSystem = config.get('2', 'OperatingSystem')
        Browser = config.get('2', 'Browser')
        user2 = username
        password2 = password
        identity2 = identity
        browser2 = Browser
    except:
        pass


from Whale2 import SignIn

SignIn

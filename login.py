import configparser

config = configparser.RawConfigParser()
config.read('login.txt')
username = config.get('login', 'username')
password = config.get('login', 'password')
identity = config.get('login', "identity")
OperatingSystem = config.get('security', 'OperatingSystem')
Browser = config.get('security', 'Browser')

from Whale2 import SignIn
SignIn
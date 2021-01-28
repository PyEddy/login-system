import random
username = input("Create a username: ")
password = input("Create a password: ")
identity = random.randint(0, 1000)

print("This is your username: " + username)
print("This is your password: " + password)


class Information:
    OperatingSystem = input("What operating system are you using: ")
    Browser = input("What browser do you use: ")


from Whale2 import SignIn
SignIn

import webbrowser
from login import username
from login import password
from login import Browser
from login import user
from login import passkey
from login import login_system_version
import configparser


number = ""
login = 1
access = 1
security = 1


def user_menu(username):
    print("Hello ", username)
    print("1 . Admin settings")
    print("2. User settings")
    user_input = input("Enter a number: ")

def server():
    print("Launching server")

class Menu:
    if user == username and passkey == password:
        if security == 1:
            print("security question")
            whatBrowser = input("What browser do you use: ")
            while Browser != whatBrowser:
                print("Thats not your browser")
                whatBrowser = input("What browser do you use: ")

            else:
                print("correct")
                print("Would you like to log this data?")
                answer = input("Type Yes if you want to log the data: ")
                if answer == "Yes":
                    f = open("data.txt", "a")
                    f.write(username)
                    f.write("\n")
                    f.write(password)
                    f.close()

    else:
        print("Hold up")


class UserProfile:
    print(username)
    print("1. User Menu")
    print("2. Server")
    user_input = input("Enter a number: ")
    if user_input == "1":
        user_menu(username)
    else:
        server()


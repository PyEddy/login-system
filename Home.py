import webbrowser
from login_system2 import SignIn
from login_system2 import username
from login_system2 import password
from login_system2 import identity
from login_system2 import Browser
from login_system2 import user
from login_system2 import passkey
import configparser


number = ""
login = 1
access = 1
security = 1


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
                    f.write("\n")
                    f.write("Identity: ")
                    f.write(str(identity))
                    f.close()

    else:
        print("Hold up")


class UserProfile:
    number = input()
    if number != str(identity):
        access = 0
    else:
        print("You have access to admin settings")
    while login == 1:
        if access != 1:
            print(username)
            print("1. User Settings")
            print("2. Website")
            number = input("Type a number: ")
        else:
            print(username)
            print(identity)
            print("1. User Settings")
            print("2. Website")
            print("5. Admin")
            number = input("Type a number: ")
        while number == "":
            print("Sorry, I can't understand what you typed. Please try again.")
            number = input("Type a number: ")
        else:
            if number == "2":
                # noinspection UnusedImport
                # noinspection PyUnresolvedReferences
                print("Test")
                webbrowser.open("https://github.com/eddytronpie/Whale", new=1)
            else:
                if number == "5" and access == 1:
                    print("Welcome to Admin settings")
                    print("1. Enter commands")
                    number = input("Enter a number: ")
                    if number == "1":
                        print("Welcome to Whale commands")
                        console = input("Enter a command: ")
                        if console == "version":
                            print(SignIn.login_system_version)
                            input()
                else:
                    if number == "1":
                        print("User Settings")
                        print("What would you like to edit?")
                        print("1. Edit username")
                        print("2. Reset password")
                        number = input("Type a number: ")
                        if number == "1":
                            temp_username = username
                            username = input("Enter a username: ")
                            try:
                                config = configparser.ConfigParser()
                                config.read('login.txt')
                                config.set('login', 'username', username)

                                with open("login.txt", "w") as f:
                                    config.write(f)
                                print("Username is changed")
                            except:
                                print("Error: The data couldn't be opened either because it hasn't been created yet"
                                      " or its old")
                                username = temp_username

                        else:
                            if number == "2":
                                password = input("Enter a password: ")
                                try:
                                    config = configparser.ConfigParser()
                                    config.read('login.txt')
                                    config.set('login', 'password', password)

                                    with open("login.txt", "w") as f:
                                        config.write(f)
                                    print("Password has been reset")
                                except:
                                    print("Error: The data couldn't be opened either because it hasn't been created yet"
                                          " or its old")
                            else:
                                print("Welcome back to the menu")
                    else:
                        print("Sorry, I can't understand what you typed. Please try again.")
    else:
        input()

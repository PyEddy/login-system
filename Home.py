import webbrowser
from turtle import goto
from Whale import Information
from Whale import password
from Whale import username
from Whale import identity
from Whale2 import SignIn

number = ""
login = 1
access = 1


class Menu:
    if SignIn.user == username and SignIn.passkey == password:
        print("security question")
        whatBrowser = input("What browser do you use: ")
        while Information.Browser != whatBrowser:
            print("Thats not your browser")
            whatBrowser = input("What browser do you use: ")

        else:
            print("correct")
            input()
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
                    input()
                else:
                    print("Sorry, I can't understand what you typed. Please try again.")
                    print("Enter a number: ")
    else:
        input()

import webbrowser
from turtle import goto

from Whale import Information
from Whale import password
from Whale import username
from Whale2 import SignIn

number = ""
login = 1


class Menu:
    if SignIn.user == username and SignIn.passkey == password:
        print("Test")
        print("security question")
        whatBrowser = input("What browser do you use: ")
        while Information.Browser != whatBrowser:
            print("Thats not your browser")
            whatBrowser = input("What browser do you use: ")

        else:
            print("correct")
            input()
    else:
        print("Hold up")


class UserProfile:
    while login == 1:
        print(username)
        print("1. User Settings")
        print("2. Website")
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
                print("Enter a number: ")
                input()
    else:
        input()

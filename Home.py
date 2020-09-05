from Whale import username
from Whale import password
from Whale import Information
from Whale2 import SignIn


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
        exit()
    else:
        print("Hold up")

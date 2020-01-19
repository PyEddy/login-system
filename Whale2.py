from Whale import username
from Whale import password


class InformationDisplay:

    def __init__(self):
        sign = SignIn()
        user = sign.get()



class SignIn:
    @staticmethod
    def get():
        return 1
    user = input("Enter your username: ")
    passkey = input("Enter your password: ")

    if user == username and passkey == password:
        print("You are logged in")

    else:
        print("Wrong username or password")

        def __init__(self):
            sign = SignIn()
            user = sign.get()


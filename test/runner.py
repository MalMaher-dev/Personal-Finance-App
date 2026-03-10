from Objects import transaction as transaction
import Objects.account as account
from tkinter import *

# window = Tk()

session = "active"
success = False


def verify_account(fname, lname):
    with open("../Data/account_data.csv", "r") as myFile:
        for line in myFile:
            current_line = line.split(",")
            registered_name = current_line[0] + " " + current_line[1]
            new_name = fname + ' ' + lname
            # print(f"The registered name is {registered_name}")
            # print(f"The new account name is {new_name}")
            if new_name == registered_name:
                return True
        return False


while session == "active":
    while not success:
        # new_account = account.Account("Jane", "Doe", 100)
        fName, lName = input("Please input your first and last name: ").split()
        if verify_account(fName, lName):
            print("This name is already in use, please login or try a different name")
        else:
            print("New account has been made")
            success = True

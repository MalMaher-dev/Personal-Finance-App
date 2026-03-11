import random

from Objects import transaction as transaction
import Objects.account as account
from tkinter import *

# window = Tk()

session = "active"
success = False


def edit_transaction():
    transaction_id = input("What is the transaction_id of what you want to update? ")
    with open("../Data/transaction_data.csv", "r") as myFile:
        for line in myFile:
            line_split = line.split(',')
            if line_split[1] == transaction_id:
                print(line)
                action = input("What would you like to change about this transaction?").lower()
                match action:
                    case "amount":
                        amount = input("Please enter your new amount")
                        line_split[2] = amount
                    case "retailer":
                        retailer = input("Please enter the new retailer")
                        line_split[3] = retailer


def view_transactions():
    transactions = []
    with open("../Data/transaction_data.csv", "r") as myFile:
        for line in myFile:
            transactions.append(line)
    return transactions


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


#
# while session == "active":
#     while not success:
#         # new_account = account.Account("Jane", "Doe", 100)
#         fName, lName = input("Please input your first and last name: ").split()
#         if verify_account(fName, lName):
#             print("This name is already in use, please login or try a different name")
#         else:
#             print("New account has been made")
#             success = True


# for num in range(10):
#     for i in range(2):
#         t = transaction.Transaction(i,random.randint(1, 9999), "Amazon.com")
#         t.write_to_file()

def sortByAccount():
    # account_id = Text(window, width=20, height=1)
    # account_id.pack()
    transactions = view_transactions()
    sorted_transactions1 = []
    sorted_transactions2 = []
    for i in range(len(transactions)):
        line_split = transactions[i].split(",")
        if line_split[1] == '0':
            print(line_split)

    # for t in range(len(transactions)):
    #     line_split = transactions[t].split(',')
    #     if (int)(line_split[1]) == 0:
    #         sorted_transactions1.append(transactions[t])
    #     else:
    #         sorted_transactions2.append(transactions[t])
    # for i in range(len(sorted_transactions2)):
    #     sorted_transactions1.append(sorted_transactions2[i])

sortByAccount()


# print(view_transactions())

# new_account.write_to_file()
#
# print("Function was Successful")
# print(new_account.balance)

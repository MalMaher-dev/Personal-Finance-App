import random
import time
import csv
import pandas

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

# retailers = ["Amazon", "Walmart", "Ebay", "Target"]
#
# for num in range(10):
#     for i in range(2):
#         t = transaction.Transaction(i, random.randint(1, 9999), retailers[random.randint(0, len(retailers) - 1)])
#         t.write_to_file()

def totalExpenses(account_id):
    total = 0
    expenses = []
    with open("../Data/transaction_data.csv") as myFile:
        reader = csv.reader(myFile)
        for line in reader:
            if line[1] == str(account_id):
                expenses.append(line)
                total += int(line[3])
    return total, len(expenses)


def totalExpensesAmount(account_id, amount):  # Expenses by amount
    total = 0
    expenses = []
    with open("../Data/transaction_data.csv") as myFile:
        reader = csv.reader(myFile)
        for line in reader:
            if line[1] == str(account_id):
                if line[3] >= str(amount):
                    expenses.append(line)
                    total += int(line[3])
    return total, len(expenses)


def totalExpensesRetailer(account_id, retailer):  # Expenses by retailer
    total = 0
    expenses = []
    with open("../Data/transaction_data.csv") as myFile:
        reader = csv.reader(myFile)
        for line in reader:
            if line[1] == str(account_id):
                if line[4] == retailer:
                    expenses.append(line)
                    total += int(line[3])
    return total, len(expenses)


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


# sortByAccount()
def createAccount():
    first, last = input("Please enter your first and last name respectively: ").split()
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    balance = input("Enter your balance: ")
    verify = input(f"Is this information correct? {first}, {last}, {username}, {password}, {balance} (yes or no): ")
    if verify == "yes":
        if verify_account(first, last):
            print("Sorry these credentials are already registered, please try again ")
            for i in range(5):
                print(". ")
                time.sleep(0.5)
            createAccount()
        else:
            new_account = account.Account(first, last, username, password, balance)
            new_account.write_to_file()
            print("Account successfully created")


def countTransactionsByRetailer(account_id):
    Amazon = []
    spentOnAmazon = 0
    Target = []
    spentOnTarget = 0
    Walmart = []
    spentOnWalmart = 0
    Ebay = []
    spentOnEbay = 0
    transactions = 0
    with open("../Data/transaction_data.csv") as myFile:
        reader = csv.reader(myFile)
        for line in reader:
            if line[1] == str(account_id):
                match line[4]:
                    case "Amazon":
                        Amazon.append(line)
                        spentOnAmazon += int(line[3])
                    case "Target":
                        Target.append(line)
                        spentOnTarget += int(line[3])
                    case "Walmart":
                        Walmart.append(line)
                        spentOnWalmart += int(line[3])
                    case "Ebay":
                        Ebay.append(line)
                        spentOnEbay += int(line[3])
    print(f"Your transactions sorted by retailer: "
          f"Amazon (Amount of transaction: {len(Amazon)}, Amount Spent: {spentOnAmazon}),\n"
          f"Target (Amount of transaction: {len(Target)}, Amount Spent: {spentOnTarget}),\n"
          f"Walmart (Amount of transactions: {len(Walmart)}, Amount Spent: {spentOnWalmart}),\n"
          f"Ebay (Amount of transactions: {len(Ebay)},Amount Spent: {spentOnEbay}),\n"
          f"Total transactions: {len(Amazon) + len(Target) + len(Walmart) + len(Ebay)}\n"
          f"Total cost: ${spentOnAmazon + spentOnTarget + spentOnWalmart + spentOnEbay}")


# createAccount()
# print(totalExpenses(0)) # Works
# print(totalExpensesAmount(0, 9000)) # Works
# print(totalExpensesRetailer(0, "Walmart"))
# print(totalExpenses(1))
countTransactionsByRetailer(0)
# sortByAccount()

# print(view_transactions())

# new_account.write_to_file()
#
# print("Function was Successful")
# print(new_account.balance)

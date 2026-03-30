import datetime
import random


class Transaction:

    def __init__(self, account_id, trans_id, amount, retailer):
        self.dateCreated = datetime.datetime.now().strftime("%x")
        self.account_id = account_id
        self.amount = amount
        self.retailer = retailer
        self.transaction_id = trans_id
    # def edit_transaction(self, transaction_id):
    #     with open("../Data/transaction_data.csv", "r") as myFile:
    #         for line in len(myFile):
    #             line_split = line.split(',')
    #             if line_split[1] == transaction_id:
    #                 action = input("What would you like to change about this transaction?").lower()
    #                 match action:
    #                     case "amount":
    #                         amount = input("Please enter your new amount")
    #                         line_split[2] = amount
    #                     case "retailer":
    #                         retailer = input("Please enter the new retailer")
    #                         line_split[3] = retailer

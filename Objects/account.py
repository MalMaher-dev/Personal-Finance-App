import datetime
import random


class Account:
    def __init__(self, fName, lName, uName, pWord, balance, account_id):
        self.first_name = fName
        self.last_name = lName
        self.username = uName
        self.password = pWord
        self.account_number = account_id
        self.balance = balance
        self.dateCreated = datetime.datetime.now().strftime("%x")  # Make it MM/DD/YYYY

    # def write_to_file(self):
    #     with open("../Data/account_data.csv", "a") as myFile:
    #         line = (f"{self.first_name},{self.last_name},{self.username},{self.password},"
    #                 f"{self.account_number},{self.balance},{self.dateCreated}")
    #         myFile.write(line + "\n")

    def toString(self):
        return (f"{self.first_name}, {self.last_name}, {self.username} ,{self.password},"
                f" {self.account_number}, {self.balance}, {self.dateCreated}")
import datetime


class Transaction:
    def __init__(self, action, amount, seller):
        self.dateCreated = datetime.datetime.now().strftime("%c")
        self.action = action
        self.amount = amount
        self.seller = seller

    def write_to_file(self):
        with open("../Data/transaction_data.csv", "a") as myFile:
            line = f"{self.dateCreated},{self.action},{self.amount},{self.seller}"
            myFile.write(line + "\n")

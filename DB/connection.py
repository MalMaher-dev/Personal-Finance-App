import random
import time

import mysql.connector
from mysql.connector import Error


def connectToMySQL():
    database = mysql.connector.connect(
        host="127.0.0.1",
        port="3307",
        user="guest",
        password="psssword",
        database="project",
        autocommit=True
    )
    return database


mydb = connectToMySQL()


def CheckConnection():
    if mydb.is_connected():
        print("Connection successful")
    else:
        print("Connection failed")


mycursor = mydb.cursor()


def verifyAccount(username, password):
    mycursor.execute(f"SELECT * FROM accountinfo WHERE username='{username}'")
    result = mycursor.fetchall()
    if result == []:
        return False
    else:
        if result[0][5] == password:
            return True
        else:
            return False


def getAccount(username):
    mycursor.execute(f"SELECT * FROM accountinfo WHERE username='{username}'")
    result = mycursor.fetchall()
    return result


def viewAllAccounts(mycursor):
    accounts = []
    mycursor.execute("SELECT * FROM accounts")
    result = mycursor.fetchall()
    for index in result:
        accounts.append(index[3])
    return accounts


def getTransactions(num):
    transactions = []
    mycursor.execute(f"SELECT * FROM transactions WHERE accountNumber = {num}")
    result = mycursor.fetchall()
    for index in result:
        dataline = f"{index[4]}, {index[3]}, {index[0].strftime('%x')}"
        transactions.append(dataline)
        # print(index)
    return transactions


def autoGenTransactions():
    accounts = []
    mycursor.execute("SELECT accountNumber FROM accountinfo")
    result = mycursor.fetchall()
    for i in result:
        accounts.append(i[0])
    retailers = ["Amazon", "Calvin Klein", "Target", "Walmart", "Costco"]
    for x in range(10):
        account = accounts[random.randint(0, len(accounts) - 1)]
        mycursor.execute(f"INSERT INTO transactions (accountNumber,amount,retailer)"
                         f" VALUES ('{account}',"
                         f" '{random.random() * random.randint(1, 100)}', "
                         f" '{retailers[random.randint(0, len(retailers) - 1)]}');")
    mydb.commit()
    print("Transactions generated")


def addAccount():  # Add accounts to account table
    mycursor.execute("INSERT INTO accountinfo(")

    mycursor.execute("INSERT INTO accountinfo(firstName,lastName,balance,accountNumber,username,password)"
                     "VALUES ('Dayton','Dawson',0,1122,'dDawson','Daytond');")
    mydb.commit()


def sortByAccount(accountNumber):
    transactions = []
    mycursor.execute(f"SELECT * FROM transactions WHERE accountNumber='{accountNumber}'")
    result = mycursor.fetchall()
    for index in result:
        transactions.append(index)
    return transactions


def sortByRetailer(retailer):
    mycursor.execute(f"SELECT * FROM transactions WHERE retailer='{retailer}'")
    result = mycursor.fetchall()
    return result


def greaterThanAverage():
    mycursor.execute("SELECT * FROM transactions"
                     " WHERE amount >= (SELECT AVG(amount) FROM transactions)"
                     " ORDER BY amount ASC;")

#
# mycursor.execute("SELECT * FROM transactions"
#                  " WHERE amount >= (SELECT AVG(amount) FROM transactions)"
#                  " ORDER BY amount ASC"
#                  " LIMIT 10;")
# result = mycursor.fetchall()
# for x in result:
#     print(x)
#     time.sleep(2)

# mycursor.execute("SELECT * FROM accountinfo WHERE accountNumber = 1234;")

# myresult = mycursor.fetchall()
# print(myresult)

# mycursor.execute("SELECT * FROM transactions WHERE accountNumber = 1234;")

# myresult = mycursor.fetchall()
# print(myresult)

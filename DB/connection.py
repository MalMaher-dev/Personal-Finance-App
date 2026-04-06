import random
import time
from Objects import account as account

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
    mycursor.execute(f"SELECT * FROM accountinfo WHERE username='{username}';")
    result = mycursor.fetchall()
    if result == []:
        return False
    else:
        if result[0][5] == password:
            return True
        else:
            return False


def check_id(num):
    mycursor.execute(f"SELECT accountNumber FROM accountinfo WHERE accountNumber='{num}';'")
    result = mycursor.fetchall()
    if not result:
        print("id generated")
        return False
    else:
        print("id not generated")
        return True;


def getAccount(username):
    mycursor.execute(f"SELECT * FROM accountinfo WHERE username='{username}'")
    result = mycursor.fetchall()
    return result


def getAllAccounts():
    accountNum = []
    mycursor.execute("SELECT accountNumber FROM accountinfo")
    result = mycursor.fetchall()
    for i in result:
        accountNum.append(i[0])


def viewAllAccounts(mycursor):
    accounts = []
    mycursor.execute("SELECT * FROM accounts")
    result = mycursor.fetchall()
    for index in result:
        accounts.append(index[3])
    return accounts


def getBalance(accountNumber):
    mycursor.execute(f"SELECT balance FROM accountinfo WHERE accountNumber='{accountNumber}'")
    result = mycursor.fetchall()[0][0]
    return result


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


def addAccount(user):  # Add accounts to account table
    mycursor.execute(f"INSERT INTO accountinfo(firstName,lastName,balance,accountNumber,username,password) "
                     f"VALUES ('{user.first_name}','{user.last_name}',0,"
                     f"{user.account_number}','{user.username}','{user.password}');")
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

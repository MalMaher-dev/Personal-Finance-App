import random
import time
from calendar import Day, Month
from random import randint

from Objects import account as account
from datetime import datetime, date
import mysql.connector
from mysql.connector import Error


def connectToMySQL():
    database = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        user="guest",
        password="psssword",
        database="project",
        autocommit=True
    )
    return database


mydb = connectToMySQL()


def getConnection():
    global mydb
    if not mydb.is_connected():
        mydb = connectToMySQL()  # reassign the global
    return mydb


def CheckConnection():
    if mydb.is_connected():
        print("Connection successful")
    else:
        print("Connection failed")


def verifyAccount(username, password):
    db = getConnection()
    mycursor = db.cursor()
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
    db = getConnection()
    mycursor = db.cursor()
    mycursor.execute(f"SELECT accountNumber FROM accountinfo WHERE accountNumber='{num}';'")
    result = mycursor.fetchall()
    if not result:
        return False
    else:
        return True;


def getAccount(username):
    db = getConnection()
    mycursor = db.cursor()
    mycursor.execute(f"SELECT * FROM accountinfo WHERE username='{username}'")
    result = mycursor.fetchall()
    return result


def getAllAccounts():
    accountNum = []
    db = getConnection()
    mycursor = db.cursor()
    mycursor.execute("SELECT accountNumber FROM accountinfo")
    result = mycursor.fetchall()
    for i in result:
        accountNum.append(i[0])


def viewAllAccounts(mycursor):
    accounts = []
    db = getConnection()
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM accounts")
    result = mycursor.fetchall()
    for index in result:
        accounts.append(index[3])
    return accounts


def getBalance(accountNumber):
    db = getConnection()
    mycursor = db.cursor()
    mycursor.execute(f"SELECT balance FROM accountinfo WHERE accountNumber='{accountNumber}'")
    result = mycursor.fetchall()[0][0]
    return result


def getTransaction(num):
    db = getConnection()
    mycursor = db.cursor()
    mycursor.execute(f"SELECT * FROM transactions WHERE transactionNumber={num}")
    result = mycursor.fetchall()
    return result[0]


def getTransactions(num):
    transactions = []
    db = getConnection()
    mycursor = db.cursor()
    mycursor.execute(f"SELECT * FROM transactions WHERE accountNumber = {num}")
    result = mycursor.fetchall()
    count = 1
    for index in result:
        dataline = f"{count}, {index[5]}, ${index[4]}, {index[1]},{index[3]}"
        transactions.append(dataline.split(","))
        count = count + 1
        # print(index)
    return transactions


def sortTransactionsAmount(num):
    transactions = getTransactions(num)
    for i in range(len(transactions)):
        key = transactions[i]
        key_amount = float(key.split(", ")[2][1:])
        j = i - 1
        while j >= 0:
            current_amount = float(transactions[j].split(", ")[2][1:])
            if current_amount > key_amount:
                transactions[j + 1] = transactions[j]
                j -= 1
            else:
                break

        transactions[j + 1] = key
    # print(transactions)
    return transactions


def sortTransactionsDate(num):
    transactions = getTransactions(num)
    for i in range(1, len(transactions)):
        key = transactions[i]

        key_str = key.split(", ")[3]
        date_str = datetime.strptime(key_str, "%Y-%m-%d").date()
        j = i - 1

        while j >= 0:
            current_date_str = transactions[j].split(", ")[3]
            current_date = datetime.strptime(current_date_str, "%Y-%m-%d").date()

            if current_date > date_str:
                transactions[j + 1] = transactions[j]
                j -= 1
            else:
                break

        transactions[j + 1] = key

        transactions[j + 1] = key
    # print(transactions)
    return transactions


def addTransaction(num, spent, seller, date):
    db = getConnection()
    mycursor = db.cursor()
    query = """
            INSERT INTO transactions (dateDone,accountNumber,amount,retailer)
            VALUES( %s, %s, %s, %s)
    
    """
    values = (date, num, spent, seller)
    mycursor.execute(query, values)
    # mycursor.execute(f"INSERT INTO transactions (dateDone,accountNumber,amount,retailer)"
    #                  f" VALUES ('{str(date)}',{num},{spent},'{str(seller)}')")
    mydb.commit()


def editTransaction(transaction_id, retailer, amount, date):
    db = getConnection()
    mycursor = db.cursor()

    query = """
            UPDATE transactions
            SET retailer = %s,amount   = %s, dateDone = %s
            WHERE transactionNumber = %s """

    values = (retailer, amount, date, transaction_id)

    mycursor.execute(query, values)
    # mycursor.execute(
    #     f"Update transactions SET retailer = '{retailer}', amount = {amount},dateDone = '{date}' WHERE transactionNumber = {transaction_id}")
    mydb.commit()


def autoGenTransactions():
    accounts = []
    db = getConnection()
    mycursor = db.cursor()
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


def AccountautoGenTransactions(num):
    db = getConnection()
    mycursor = db.cursor()
    retailers = ["Amazon", "Calvin Klein", "Target", "Walmart", "Costco", "Sam's Club", "Aldi's", "Asda"]


    for x in range(10):
        Month = random.randint(1, 12)
        Year = random.randint(2000, date.today().year)
        Day = 0

        if Month == 2:
            if Year % 4 == 0:
                if Year % 100 == 0:
                    if Year % 400 == 0:
                        Day = random.randint(1, 29)
                else:
                    Day = random.randint(1, 28)
            else:
                Day = random.randint(1, 29)
        else:
            if Month == 1 or Month == 3 or Month == 5 or Month == 7 or Month == 8 or Month == 10 or Month == 12:
                Day = random.randint(1, 31)
            else:
                Day = random.randint(1, 30)

        if Month < 10:
            Month = "0" + str(Month)
        else:
            Month = str(Month)

        if Day < 10:
            Day = "0" + str(Day)
        else:
            Day = str(Day)

        dateS = f"{Year}-{Month}-{Day}"
        dateStr = datetime.strptime(dateS, "%Y-%m-%d").date()

        mycursor.execute(f"INSERT INTO transactions (accountNumber,amount,retailer, dateDone)"
                         f" VALUES (%s, %s, %s, %s)",
                         (num, random.random() * random.randint(10, 100),
                          retailers[random.randint(0, len(retailers) - 1)], dateStr)
                         )
    mydb.commit()
    print("Transactions generated")


def addAccount(user):  # Add accounts to account table
    db = getConnection()
    mycursor = db.cursor()
    mycursor.execute(f"INSERT INTO accountinfo(firstName,lastName,balance,accountNumber,username,password) "
                     f"VALUES ('{user.first_name}','{user.last_name}','{0}',"
                     f"'{user.account_number}','{user.username}','{user.password}');")
    mydb.commit()


def sortByAccount(accountNumber):
    transactions = []
    db = getConnection()
    mycursor = db.cursor()
    mycursor.execute(f"SELECT * FROM transactions WHERE accountNumber='{accountNumber}'")
    result = mycursor.fetchall()
    for index in result:
        transactions.append(index)
    return transactions


def sortByRetailer(retailer):
    db = getConnection()
    mycursor = db.cursor()
    mycursor.execute(f"SELECT * FROM transactions WHERE retailer='{retailer}'")
    result = mycursor.fetchall()
    return result


def greaterThanAverage():
    db = getConnection()
    mycursor = db.cursor()
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

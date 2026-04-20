import random
import time
from Objects import account as account
from datetime import datetime
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
    for index in result:
        dataline = f"{index[3]}, {index[5]}, ${index[4]}, {index[1]}"
        transactions.append(dataline)
        # print(index)
    return transactions


def sortTransactionsRetailer(num):
    transactions = getTransactions(num)
    sortedTransactions = []
    for i in range(len(transactions)):
        if i == 0:
            pass


def sortTransactionsAmount(num):
    transactions = getTransactions(num)

    for i in range(1, len(transactions)):
        key = transactions[i]
        key_amount = float(key.split(", ")[1][1:])
        j = i - 1
        while j >= 0:
            current_amount = float(transactions[j].split(", ")[1][1:])
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

        # Extract and parse the date from the key
        key_str = key.split(", ")[2]
        date_str = datetime.strptime(key_str, "%x")
        j = i - 1

        while j >= 0:
            current_date_str = transactions[j].split(", ")[2]
            current_date = datetime.strptime(current_date_str, "%x")

            if current_date > date_str:
                transactions[j + 1] = transactions[j]
                j -= 1
            else:
                break

        transactions[j + 1] = key

        transactions[j + 1] = key
    print(transactions)


def addTransaction(num, spent, seller, date):
    db = getConnection()
    mycursor = db.cursor()
    mycursor.execute(f"INSERT INTO transactions (dateDone,accountNumber,amount,retailer)"
                     f" VALUES ('{str(date).strip()}',{num},{spent},'{str(seller).strip()}')")
    mydb.commit()



def editTransaction(transaction_id, amount, date):
    db = getConnection()
    mycursor = db.cursor()
    mycursor.execute(f"Update transactions SET amount = {amount},dateDone = '{date}' WHERE transactionNumber = {transaction_id}")
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

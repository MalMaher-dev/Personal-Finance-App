import random
import time

import mysql.connector
from mysql.connector import Error

mydb = mysql.connector.connect(
    host="127.0.0.1",
    port="3307",
    user="guest",
    password="pssswrd",
    database="project",
    autocommit=True
)

try:
    if mydb.is_connected():
        print("Connection Successful")
    else:
        print("Connection Failed")
except Error as e:
    print(f"Error: {e}")

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM accountinfo;")

myresult = mycursor.fetchall()
accounts = []

for x in myresult:
    accounts.append(x[3])
    print(x)

retailers = ["Amazon", "Calvin Klein", "Target", "Walmart", "Costco"]

# for x in range(10):
#     mycursor.execute(f"INSERT INTO transactions (accountNumber,amount,retailer)"
#                      f" VALUES ('{accounts[random.randint(0, len(accounts) - 1)]}',"
#                      f" '{random.random() * random.randint(1, 100)}', "
#                      f" '{retailers[random.randint(0, len(retailers) - 1)]}');")

# def addAccount(): # Add accounts to account table
#     mycursor.execute("INSERT INTO accountinfo(")

# mycursor.execute("INSERT INTO accountinfo(firstName,lastName,balance,accountNumber,username,password)"
#                  "VALUES ('Dayton','Dawson',0,1122,'dDawson','Daytond');")
# mydb.commit()


def sortByAccount(accountNumber):
    mycursor.execute(f"SELECT * FROM transactions WHERE accountNumber='{accountNumber}'")
    result = mycursor.fetchall()
    return result


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

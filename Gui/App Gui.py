import csv
from tkinter import *
from tkinter import ttk
import re
import time
from Objects import transaction as transaction
from Objects import account as account
import DB.connection as connection

GEOMETRY_DEFAULT = "800x600"


#
# def sortByAccount():
#     # account_id = Text(window, width=20, height=1)
#     # account_id.pack()
#     transactions = connection.getTransactions(9521)
#     sorted_transactions1 = []
#     sorted_transactions2 = []
#     for t in range(len(transactions)):
#         line_split = transactions[t].split(',')
#         if line_split[1] == 'dateCreated':
#             pass
#         elif line_split[1] == '0':
#             sorted_transactions1.append(transactions[t])
#         else:
#             sorted_transactions2.append(transactions[t])
#     for i in range(len(sorted_transactions2)):
#         sorted_transactions1.append(sorted_transactions2[i])
#     return sorted_transactions1


def getCurrentGeometry():
    wGeo = re.split(r'[x,+]', window.geometry())
    windowW = wGeo[0]
    windowH = wGeo[1]
    return windowW, windowH


window = Tk()

window.title("Finance App")
window.geometry(GEOMETRY_DEFAULT)

window.resizable(False, False)

login_text = ttk.Label(window, text="Finance App")
login_text.pack(pady=100, padx=300)

# Login Text Boxes

user_label = ttk.Label(window, text="Username")
user_label.pack()
username = Text(window, width=20, height=1)
username.pack()

pass_label = ttk.Label(window, text="Password")
pass_label.pack()
password = Text(window, width=20, height=1)
password.pack()

content = ttk.Frame(window)


# Buttons


def submit():
    uName = username.get("1.0", END).strip()
    pWord = password.get("1.0", END).strip()
    print(f"Information submitted, please wait for verification {uName} and password {pWord}")
    if connection.verifyAccount(uName, pWord):
        result = connection.getAccount(uName)
        user = account.Account(result[0][0], result[0][1], result[0][4], result[0][5], result[0][3])
        print("Welcome, give us a moment to adjust somethings")
        print(user.toString())
        print(getSessionTime(), " seconds")
        cleanLogin()
        renderHomeScreen(user)
    else:
        print("Account not found, please try again")


submit_button = Button(window, text="Submit", command=submit)
submit_button.pack(pady=20)

check_button = Button(window, text="Check Connection", command=connection.CheckConnection)
check_button.pack(pady=20)


def cleanLogin():
    login_text.forget()
    user_label.forget()
    pass_label.forget()
    username.forget()
    password.forget()
    submit_button.forget()
    check_button.forget()


def renderHomeScreen(user):
    user_label = ttk.Label(window, text=f"Hello {user.first_name}")
    user_label.grid(row=0, column=0)

    View_button = ttk.Button(window, text="View Transactions", command=lambda: displayTransactions(user.account_number))
    View_button.grid(row=0, column=1, columnspan=2)


# def displayTransactions():
#     transactionList = []
#     transactions = view_transactions()
#     transvar = StringVar(value=transactions)
#
#     viewer = Listbox(window, listvariable=transvar, height=3, width=50)
#     viewer.pack()
#
#
# Sort_button = ttk.Button(window, text="Sort by account", command=sortByAccount)
# Sort_button.pack()

def displayTransactions(num):

    pass
    # Works
    # transactions = connection.getTransactions(9521)
    # Stransvar = StringVar(value=transactions)
    # Sviewer = Listbox(window, listvariable=Stransvar, height=5, width=50)
    # Sviewer.grid(row=1, column=1, rowspan=3)
    # Sviewer.pack()


def getSessionTime():
    return round(time.time() - startTime, 2)


# Session tracker

startTime = time.time()

window.mainloop()

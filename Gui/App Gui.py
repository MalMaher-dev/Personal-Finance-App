from tkinter import *
from tkinter import ttk
import re
import time
from Objects import transaction as transaction
from Objects import account as account
import DB.connection as connection
import random

from Objects.account import Account

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


def register():
    cleanLogin()
    # register_button.forget()
    global username, password, firstName, lastName

    user_label = ttk.Label(window, text="Enter a Username")
    user_label.pack()
    username = Text(window, width=20, height=1)
    username.pack()

    pass_label = ttk.Label(window, text="Enter a Password")
    pass_label.pack()
    password = Text(window, width=20, height=1)
    password.pack()

    firstName_label = ttk.Label(window, text="Enter a First Name")
    firstName_label.pack()
    firstName = Text(window, width=20, height=1)
    firstName.pack()

    lastName_label = ttk.Label(window, text="Enter a Last Name")
    lastName_label.pack()
    lastName = Text(window, width=20, height=1)
    lastName.pack()

    NewSubmit_button = ttk.Button(window, text="Submit", command=lambda: submitNewUser)
    NewSubmit_button.pack()

    # renderHomeScreen(new_account)


def submitNewUser():
    global username, password, firstName, lastName

    uName = username.get("1.0", END).strip()
    print(uName)
    pWord = password.get("1.0", END).strip()
    print(pWord)
    firstName = firstName.get("1.0", END).strip()
    print(firstName)
    lastName = lastName.get("1.0", END).strip()
    print(lastName)
    account_id = random.randint(0, 9999)
    print(f"{uName}, {pWord}, {firstName}, {lastName}, {account_id}")
    if not connection.check_id(account_id):
        account_id + 1
    else:
        new_account = Account(uName, pWord, firstName, lastName, account_id)

    print(new_account.toString())


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
#
# register_button = Button(window, text="Register", command=register)
# register_button.pack()

content = ttk.Frame(window)

# Buttons

fail_text = None


def submit():
    global fail_text
    uName = username.get("1.0", END).strip()
    pWord = password.get("1.0", END).strip()
    # print(f"Information submitted, please wait for verification {uName} and password {pWord}")
    if connection.verifyAccount(uName, pWord):
        if fail_text:
            fail_text.forget()
        result = connection.getAccount(uName)
        # print(result)
        user = account.Account(result[0][0], result[0][1], result[0][4], result[0][5], result[0][2], result[0][3])
        # print("Welcome, give us a moment to adjust somethings")
        # print(user.toString())
        # print(getSessionTime(), " seconds")
        cleanLogin()
        renderHomeScreen(user)
    else:
        fail_text = ttk.Label(window, text="Incorrect username or password")
        fail_text.pack(pady=20)


submit_button = Button(window, text="Submit", command=submit)
submit_button.pack(pady=20)


# check_button = Button(window, text="Check Connection", command=connection.CheckConnection)
# check_button.pack(pady=20)


def cleanLogin():
    login_text.forget()
    user_label.forget()
    pass_label.forget()
    username.forget()
    password.forget()
    submit_button.forget()
    # check_button.forget()


def renderHomeScreen(user):

    user_label = ttk.Label(window, text=f"Hello {user.first_name}", font=("Arial", 20))
    user_label.grid(row=0, column=0, columnspan=2, rowspan=2, ipadx=40, ipady=10, padx=30, pady=30)

    add_transaction = ttk.Button(window, text="Add Transaction", command=connection.autoGenTransactions)
    add_transaction.grid(row=3, column=0, columnspan=2, rowspan=2, ipadx=20, ipady=10)

    sort_transactions = ttk.Button(window, text="Sort Transactions", command=lambda: sorter(user.account_number))
    sort_transactions.grid(row=6, column=0, columnspan=2, rowspan=2, ipadx=20, ipady=10, pady=30)

    chart_transaction = ttk.Button(window, text="Chart Transaction", command=lambda: print("Chart works"))
    chart_transaction.grid(row=10, column=0, columnspan=2, rowspan=2, ipadx=20, ipady=10, pady=50)

    transaction_history = ttk.Button(window, text="Transaction History",
                                     command=lambda: displayTransactions(user.account_number,"show"))
    transaction_history.grid(row=3, column=5, columnspan=2, ipadx=145, ipady=10, padx=30)

    chron_sort = ttk.Button(window, text="Oldest to Newest", command=lambda: print("Old - New"))
    chron_sort.grid(row=4, column=5, ipadx=50)

    balance_label = ttk.Label(window, text=f"Balance: ${user.balance}", font=("Arial", 10), justify=CENTER)
    balance_label.grid(row=4, column=6)


    # for row in range(7):
    #     for col in range(10):
    #         Button(
    #             window,
    #             text=f"Cell ({row}, {col})",
    #             width=10,
    #             height=5,
    #         ).grid(row=row, column=col)

    # View_button = ttk.Button(window, text="View Transactions",
    #                          command=lambda: displayTransactions(int(user.account_number)))
    # View_button.grid(row=0, column=1, columnspan=2)


def displayTransactions(num, action):

    data_label = ttk.Label(window, text=f"Retailer, Amount Spent, Date", font=("Arial", 10))
    data_label.grid(row=5, column=5, columnspan=2)
    balance_label = ttk.Label(window, text=f"Balance: ${connection.getBalance(num)}", font=("Arial", 10),
                              justify=CENTER)
    balance_label.grid(row=4, column=6)

    if action == "show":
        transactions = connection.getTransactions(num)
        Stransvar = StringVar(value=transactions)
        Sviewer = Listbox(window, listvariable=Stransvar, width=30, height=2, font=("Arial", 10), justify=CENTER)
        Sviewer.grid(row=6, column=5, rowspan=8, columnspan=2, ipadx=25, ipady=100)

    elif action == "sortDate":
        transactions = connection.sortTransactionsDate(num)
        Stransvar = StringVar(value=transactions)
        Sviewer = Listbox(window, listvariable=Stransvar, width=30, height=2, font=("Arial", 10), justify=CENTER)
        Sviewer.grid(row=6, column=5, rowspan=8, columnspan=2, ipadx=25, ipady=100)

    elif action == "sortRetailer":
        transactions = connection.sortTransactionsRetailer(num)
        Stransvar = StringVar(value=transactions)
        Sviewer = Listbox(window, listvariable=Stransvar, width=30, height=2, font=("Arial", 10), justify=CENTER)
        Sviewer.grid(row=6, column=5, rowspan=8, columnspan=2, ipadx=25, ipady=100)

    elif action == "sortAmount":
        transactions = connection.sortTransactionsAmount(num)
        Stransvar = StringVar(value=transactions)
        Sviewer = Listbox(window, listvariable=Stransvar, width=30, height=2, font=("Arial", 10), justify=CENTER)
        Sviewer.grid(row=6, column=5, rowspan=8, columnspan=2, ipadx=25, ipady=100)


def sorter(num):

    sort_date = ttk.Button(window, text="By Date",
                           command=lambda: connection.sortTransactionsDate(num))
    sort_date.grid(row=7, column=0, columnspan=2, rowspan=2, ipadx=10, ipady=10, pady=30)

    sort_retailer = ttk.Button(window, text="By Retailer",
                               command=lambda: print("Undone"))
    sort_retailer.grid(row=8, column=0, columnspan=2, rowspan=2, ipadx=20, ipady=10, pady=30)

    sort_amount = ttk.Button(window, text="By Amount (Asc)",
                                   command=lambda: connection.sortTransactionsAmount(num))
    sort_amount.grid(row=9, column=0, columnspan=2, rowspan=2, ipadx=20, ipady=10, pady=30)


def getSessionTime():
    return round(time.time() - startTime, 2)


# Session tracker

startTime = time.time()

window.mainloop()

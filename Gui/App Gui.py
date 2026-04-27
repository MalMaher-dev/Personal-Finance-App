import tkinter
from datetime import datetime
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
fail_text = None


def getCurrentGeometry():
    wGeo = re.split(r'[x,+]', window.geometry())
    windowW = wGeo[0]
    windowH = wGeo[1]
    return windowW, windowH

    # renderHomeScreen(new_account)


def submitNewUser():
    global username, password, firstName, lastName, fail_text

    uName = username.get("1.0", END).strip()
    pWord = password.get().strip()
    fName = firstName.get("1.0", END).strip()
    lName = lastName.get("1.0", END).strip()
    account_id = random.randint(0, 9999)
    fields = [uName, pWord, fName, lName]
    # print(f"{uName}, {pWord}, {fName}, {lName}, {account_id}")
    if not connection.check_id(account_id):
        account_id += 1
        # new_account = account.Account(uName, pWord, firstName, lastName,balance=0, account_id=account_id)
    for field in fields:
        if field.strip() == "":
            if fail_text:
                fail_text.forget()
            fail_text = ttk.Label(window, text="Fields cannot be empty")
            fail_text.pack(pady=20)
            return

    if fail_text:
        fail_text.forget()
    new_account = account.Account(fName, lName, uName, pWord, balance=0, account_id=account_id)
    # print(new_account.toString())
    connection.addAccount(new_account)

    registration_text.forget()
    user_label.forget()
    pass_label.forget()
    firstName_label.forget()
    lastName_label.forget()

    username.forget()
    password.forget()
    firstName.forget()
    lastName.forget()
    NewSubmit_button.forget()
    loginOptionButton.forget()

    renderHomeScreen(new_account)


window = Tk()

window.title("Finance App")
window.geometry(GEOMETRY_DEFAULT)

window.resizable(False, False)

registration_text = ttk.Label(window, text="Registration")
registration_text.pack(pady=100, padx=300)

# Registration Text Boxes
user_label = ttk.Label(window, text="Enter a Username")
user_label.pack()
username = Text(window, width=20, height=1)
username.pack()

pass_label = ttk.Label(window, text="Enter a Password")
pass_label.pack()
password = Entry(window, width=25, show='*')
password.pack()

firstName_label = ttk.Label(window, text="Enter a First Name")
firstName_label.pack()
firstName = Text(window, width=20, height=1)
firstName.pack()

lastName_label = ttk.Label(window, text="Enter a Last Name")
lastName_label.pack()
lastName = Text(window, width=20, height=1)
lastName.pack()

NewSubmit_button = tkinter.Button(window, text="Submit",command=submitNewUser)
NewSubmit_button.pack()


def renderLoginScreen():
    global user_label, username, pass_label, password, firstName, lastName, login_text, submit_button
    registration_text.forget()
    user_label.forget()
    pass_label.forget()
    firstName_label.forget()
    lastName_label.forget()
    username.forget()
    password.forget()
    firstName.forget()
    lastName.forget()
    NewSubmit_button.forget()
    loginOptionButton.forget()

    login_text = ttk.Label(window, text="Login")
    login_text.pack(pady=100, padx=300)

    # Login Text Boxes
    user_label = ttk.Label(window, text="Username")
    user_label.pack()
    username = Text(window, width=20, height=1)
    username.pack()

    pass_label = ttk.Label(window, text="Password")
    pass_label.pack()
    password = Entry(window, width=25, show='*')
    password.pack()

    submit_button = Button(window, text="Submit", command=submit)
    submit_button.pack(pady=20)


loginOptionButton = tkinter.Button(window, text="If you already have an account", command=renderLoginScreen,
                                relief=tkinter.RIDGE, borderwidth=2)
loginOptionButton.pack()
content = ttk.Frame(window)


# Buttons


def submit():
    global fail_text, login_text, submit_button
    uName = username.get("1.0", END).strip()
    pWord = password.get().strip()
    login_text.forget()
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

        login_text.forget()
        user_label.forget()
        pass_label.forget()
        username.forget()
        password.forget()
        submit_button.forget()
        renderHomeScreen(user)
    else:
        fail_text = ttk.Label(window, text="Incorrect username or password")
        fail_text.pack(pady=20)


# submit_button = Button(window, text="Submit", command=submit)
# submit_button.pack(pady=20)


# check_button = Button(window, text="Check Connection", command=connection.CheckConnection)
# check_button.pack(pady=20)


def renderHomeScreen(user):
    user_label = ttk.Label(window, text=f"Hello {user.first_name},", font=("Arial", 20))
    user_label.grid(row=0, column=0, columnspan=2, rowspan=2, ipadx=40, ipady=10, padx=30, pady=30)

    add_transaction = ttk.Button(window, text="Add Transaction", command=lambda: addTransaction(user.account_number))
    add_transaction.grid(row=3, column=0, columnspan=2, rowspan=2, ipadx=20, ipady=10)

    sort_transactions = ttk.Button(window, text="Sort Transactions", command=lambda: sorter(user.account_number))
    sort_transactions.grid(row=6, column=0, columnspan=2, rowspan=2, ipadx=20, ipady=10, pady=(30, 0))

    edit_transaction = ttk.Button(window, text="Edit Transaction", command=lambda: editor(user.account_number))
    edit_transaction.grid(row=10, column=0, columnspan=2, rowspan=2, ipadx=20, ipady=10, pady=50)

    transaction_history = ttk.Button(window, text="Transaction History",
                                     command=lambda: displayTransactions(user.account_number, "show"))
    transaction_history.grid(row=3, column=5, columnspan=2, ipadx=145, ipady=10, padx=30)

    displayTransactions(user.account_number, "show")

    widgets = [user_label, add_transaction, sort_transactions, edit_transaction, transaction_history]

    # logOut = tkinter.Button(window, text="Logout", command=lambda :cleanLogin)
    # logOut.grid(row=16, columnspan=6)

def cleanLogin():
    window.destroy()
    window.title("Finance App")
    window.geometry(GEOMETRY_DEFAULT)

    window.resizable(False, False)

    login_text = ttk.Label(window, text="Login")
    login_text.pack(pady=100, padx=300)

    # Login Text Boxes
    user_label = ttk.Label(window, text="Username")
    user_label.pack()
    username = Text(window, width=20, height=1)
    username.pack()

    pass_label = ttk.Label(window, text="Password")
    pass_label.pack()
    password = Entry(window, width=25, show='*')
    password.pack()

    submit_button = Button(window, text="Submit", command=submit)
    submit_button.pack(pady=20)


    # chron_sort = ttk.Button(window, text="Oldest to Newest", command=lambda: print("Old - New"))
    # chron_sort.grid(row=4, column=5, ipadx=50)

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
    data_label = ttk.Label(window, text=f"Transaction #, Retailer, Amount Spent, Date", font=("Arial", 10))
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
    #
    # sort_date = ttk.Button(window, text="By Date",
    #                        command=lambda: connection.sortTransactionsDate(num))
    # sort_date.grid(row=7, column=0, columnspan=2, rowspan=2, ipadx=10, ipady=10, pady=30)

    # sort_retailer = ttk.Button(window, text="By Retailer",
    #                            command=lambda: print("Undone"))
    # sort_retailer.grid(row=8, column=0, columnspan=2, rowspan=1, ipadx=25)

    sort_amount = ttk.Button(window, text="By Amount (Asc)",
                             command=lambda: displayTransactions(num, "sortAmount"))
    sort_amount.grid(row=9, column=0, columnspan=2, rowspan=1, ipadx=15)


def confirmAdd(num, retailer, amount, date, pane):
    connection.addTransaction(num, amount, retailer, date)
    displayTransactions(num, "show")
    print(f"{num},{amount},{retailer},{date}")
    pane.destroy()


def addTransaction(num):
    new = Toplevel(window)
    new.title("New Transaction")
    new.geometry("300x300")

    Label(new, text="Enter transaction data to add").grid(row=0, column=0, columnspan=2, ipadx=50)

    retailer_label = Label(new, text=f"Retailer", font=("Arial", 10))
    retailer_label.grid(row=2, column=0, columnspan=2, pady=10, padx=50)

    retailerBox = Text(new, width=20, height=1)
    retailerBox.grid(row=3, column=0, padx=50, pady=5)

    amount_label = Label(new, text="Amount", font=("Arial", 10))
    amount_label.grid(row=4, column=0, columnspan=2, pady=10)

    amountBox = Text(new, width=20, height=1)
    amountBox.grid(row=5, column=0, padx=50, pady=5)

    Date_label = Label(new, text="Date (YYYY-MM-DD)", font=("Arial", 10))
    Date_label.grid(row=6, column=0, columnspan=2, pady=10)

    DateBox = Text(new, width=20, height=1)
    DateBox.grid(row=7, column=0, padx=50, pady=5)

    correct = Button(new, text="Submit",
                     command=lambda: confirmAdd(num, retailerBox.get("1.0", END),
                                                amountBox.get("1.0", END),
                                                DateBox.get("1.0", END), new))
    correct.grid(row=8, column=0, columnspan=2, pady=10)


global numberBox


def editor(num):
    global username
    number_label = Label(window, text="Transaction Number: ", font=("Arial", 10))
    number_label.grid(row=12, column=0, columnspan=2)

    username = Text(window, width=15, height=1, font=("Arial", 10))
    username.grid(row=13, column=0, columnspan=1, padx=10)

    submitButton = ttk.Button(window, text="edit", command=lambda: editTransaction(num))
    submitButton.grid(row=13, column=1, ipadx=5)


def confirmEdit(num, trans_id, retailer, amount, date, pane):

    amount = amount.strip()
    retailer = retailer.strip()
    date = date.strip()
    tran = connection.getTransaction(trans_id)

    if retailer == "":
        retailer = tran[5]  # assuming index 2 is retailer
    if amount == "":
        amount = tran[4]
    if date == "":
        dateStr = tran[1]  # already a date object
    else:
        dateStr = datetime.strptime(date, "%Y-%m-%d").date()

    if dateStr > date.today():
        fail_text = Label(pane, text="Sorry, you are not authorized to do that.")
        return

    connection.editTransaction(trans_id, retailer, amount, dateStr)
    displayTransactions(num, "show")
    pane.destroy()

def editTransaction(accountNumber):
    global fail_text, username
    id = username.get("1.0", END).strip()
    new = Toplevel(window)
    new.title("Edit Transaction")
    new.geometry("300x350")

    Label(new, text="Enter new amount").grid(row=0, column=0, columnspan=2, ipadx=50)

    transaction = connection.getTransaction(id)
    if not transaction or accountNumber != transaction[2]:
        fail_text = ttk.Label(window, text="Unable to retrieve")
        fail_text.grid(pady=20)
        return
    transData = f"{transaction[5]}, {transaction[4]}, {transaction[1]}"
    data_label = Label(new, text=f"{transData}", font=("Arial", 10))
    data_label.grid(row=2, column=0, columnspan=2, pady=20, padx=50)

    retailer_label = Label(new, text="Retailer", font=("Arial", 10))
    retailer_label.grid(row=3, column=0)

    retailerBox = Text(new, width=7, height=1)
    retailerBox.grid(row=3, column=1)

    amount_label = Label(new, text="Amount", font=("Arial", 10))
    amount_label.grid(row=4, column=0, pady=20)

    amountBox = Text(new, width=7, height=1)
    amountBox.grid(row=4, column=1, padx=10, pady=20)

    date_label = Label(new, text="Date", font=("Arial", 10))
    date_label.grid(row=5, column=0, pady=20)

    dateBox = Text(new, width=7, height=1)
    dateBox.grid(row=5, column=1, ipadx=20, pady=20)

    correct = Button(new, text="Submit",
                     command=lambda: confirmEdit(accountNumber, id, retailerBox.get("1.0", END), amountBox.get("1.0", END).strip(),
                                                 str(dateBox.get("1.0", END)).strip(),new))
    correct.grid(row=6, column=0, columnspan=2, pady=20)

def getSessionTime():
    return round(time.time() - startTime, 2)


# Session tracker

startTime = time.time()

window.mainloop()

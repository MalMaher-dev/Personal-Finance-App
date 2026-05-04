import tkinter
from datetime import *
from tkinter import *
from tkinter import ttk
import re
import time
from Objects import transaction as transaction
from Objects import account as account
import DB.connection as connection
import random
import numpy as np
import matplotlib.pyplot as plt
import textwrap
import Objects.account as Account

GEOMETRY_DEFAULT = "800x600"
fail_text = None


def getCurrentGeometry():
    wGeo = re.split(r'[x,+]', window.geometry())
    windowW = wGeo[0]
    windowH = wGeo[1]
    return windowW, windowH


def submitNewUser(uName, pWord, fName, lName):
    global fail_text

    account_id = random.randint(0, 9999)
    fields = [uName, pWord, fName, lName]
    if not connection.check_id(account_id):
        account_id += 1
    for field in fields:
        if field.strip() == "":
            if fail_text:
                fail_text.forget()
            fail_text = ttk.Label(window, text="Fields cannot be empty")
            fail_text.pack(pady=20)
            return

    if fail_text:
        fail_text.forget()
    new_account = Account(fName, lName, uName, pWord, balance=0, account_id=account_id)
    connection.addAccount(new_account)

    for widget in window.winfo_children():
        widget.destroy()

    renderHomeScreen(new_account)


window = Tk()

window.title("Finance App")
window.geometry(GEOMETRY_DEFAULT)

window.resizable(False, False)


def registration():
    registration_text = ttk.Label(window, text="Registration")
    registration_text.pack(pady=100, padx=300)

    user_label = ttk.Label(window, text="Enter a Username")
    user_label.pack()
    user_label.configure(takefocus=0)

    username = Entry(window, width=25, justify=CENTER)
    username.pack()
    username.focus()

    pass_label = ttk.Label(window, text="Enter a Password")
    pass_label.pack()
    pass_label.configure(takefocus=0)

    password = Entry(window, width=25, show='*', justify=CENTER)
    password.pack()

    firstName_label = ttk.Label(window, text="Enter a First Name")
    firstName_label.pack()
    firstName_label.configure(takefocus=0)

    firstName = Entry(window, width=25, justify=CENTER)
    firstName.pack()

    lastName_label = ttk.Label(window, text="Enter a Last Name")
    lastName_label.pack()
    lastName_label.configure(takefocus=0)

    lastName = Entry(window, width=25, justify=CENTER)
    lastName.pack()

    NewSubmit_button = tkinter.Button(window, text="Submit",
                                      command=lambda: submitNewUser(username.get(), password.get(),
                                                                    firstName.get(), lastName.get()))
    NewSubmit_button.pack()

    loginOptionButton = tkinter.Button(window, text="If you already have an account", command=renderLoginScreen,
                                       relief=tkinter.RIDGE, borderwidth=2)
    loginOptionButton.pack()


def renderLoginScreen():
    global user_label, username, pass_label, password, firstName, lastName, login_text, submit_button
    for widget in window.winfo_children():
        widget.destroy()

    login_text = ttk.Label(window, text="Login")
    login_text.pack(pady=100, padx=300)
    login_text.configure(takefocus=0)

    user_label = ttk.Label(window, text="Username")
    user_label.pack()
    user_label.configure(takefocus=0)

    username = Entry(window, width=25, justify=CENTER)
    username.pack()
    username.focus_set()

    pass_label = ttk.Label(window, text="Password")
    pass_label.pack()
    pass_label.configure(takefocus=0)

    password = Entry(window, width=25, show='*', justify=CENTER)
    password.pack()

    submit_button = Button(window, text="Submit", command=submit)
    submit_button.pack(pady=20)


def submit():
    global fail_text, login_text, submit_button
    uName = username.get().strip()
    pWord = password.get().strip()
    if connection.verifyAccount(uName, pWord):
        if fail_text:
            fail_text.forget()
        login_text.forget()
        result = connection.getAccount(uName)
        user = account.Account(result[0][0], result[0][1], result[0][4], result[0][5], result[0][2], result[0][3])

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


def charter(num):
    new = Toplevel(window)
    new.title("Chart/Graph Options")
    new.geometry("100x100")

    Pie_chart = Button(new, text="Pie Chart", font=("Arial", 10), command=lambda: chart_Transactions(num, "pie"))
    Pie_chart.grid(row=2, column=0, columnspan=2, pady=10, padx=25)

    Bar_graph = Button(new, text="Bar Graph", font=("Arial", 10), command=lambda: chart_Transactions(num, "bar"))
    Bar_graph.grid(row=3, column=0, columnspan=2, pady=10, padx=25)


def renderHomeScreen(user):
    for row in range(17):
        window.grid_rowconfigure(row, minsize=30)

    window.grid_columnconfigure(0, minsize=80)
    window.grid_columnconfigure(1, minsize=80)
    window.grid_columnconfigure(5, minsize=80)
    window.grid_columnconfigure(6, minsize=80)

    user_label = ttk.Label(window, text=f"Hello {user.first_name},", font=("Arial", 20))
    user_label.grid(row=0, column=0, columnspan=2, rowspan=2, ipadx=40, ipady=10, padx=30, pady=30)

    add_transaction = ttk.Button(window, text="Add Transaction", command=lambda: addTransaction(user.account_number))
    add_transaction.grid(row=3, column=0, columnspan=2, ipadx=20, ipady=10)

    listbox_ref = [None]

    def refresh(action="show"):
        listbox_ref[0] = displayTransactions(user.account_number, action)

    edit_transaction = ttk.Button(window, text="Edit Transaction",
                                  command=lambda: editTransaction(user.account_number, listbox_ref[0]))
    edit_transaction.grid(row=6, column=0, columnspan=2, ipadx=20, ipady=10)

    chart_Transaction = ttk.Button(window, text="Chart Transactions",
                                   command=lambda: charter(user.account_number))
    chart_Transaction.grid(row=9, column=0, columnspan=2, ipadx=20, ipady=10)

    transaction_history = ttk.Button(window, text="Transaction History",
                                     command=lambda: refresh("show"))
    transaction_history.grid(row=0, column=5, columnspan=2, ipadx=145, ipady=10, padx=30)

    refresh("show")

    logOut = tkinter.Button(window, text="Logout", command=logout)
    logOut.grid(row=13, column=6, columnspan=1, pady=10)


def sortColumn(tree, col, reverse):
    data = [(tree.set(item, col), item)
            for item in tree.get_children("")]

    if col == "amount":
        data.sort(key=lambda x: float(x[0].replace("$", "").strip()), reverse=reverse)
    elif col == "id":
        data.sort(key=lambda x: int(x[0].lower()), reverse=reverse)
    else:
        data.sort(key=lambda x: x[0].lower(), reverse=reverse)

    for index, (_, item) in enumerate(data):
        tree.move(item, "", index)

    tree.heading(col, command=lambda: sortColumn(tree, col, not reverse))


listbox_frame = None


def displayTransactions(num, action):
    global listbox_frame

    balance_label = ttk.Label(window, text=f"Balance: ${connection.getBalance(num)}", font=("Arial", 10),
                              justify=CENTER)
    balance_label.grid(row=1, column=5, columnspan=2)

    if listbox_frame:
        listbox_frame.destroy()

    transactions = []
    if action == "show":
        transactions = connection.getTransactions(num)
    elif action == "sortDate":
        transactions = connection.sortTransactionsDate(num)
    elif action == "sortAmount":
        transactions = connection.sortTransactionsAmount(num)

    listbox_frame = Frame(window)
    listbox_frame.grid(row=2, column=5, rowspan=15, columnspan=2, padx=60, pady=5, sticky=NW)

    scrollbar = ttk.Scrollbar(listbox_frame, orient=VERTICAL)
    scrollbar.pack(side=RIGHT, fill=Y)

    tree = ttk.Treeview(listbox_frame,
                        columns=("id", "retailer", "amount", "date"),
                        show="headings",
                        height=15,
                        yscrollcommand=scrollbar.set)
    scrollbar.config(command=tree.yview)

    tree.heading("id", text="#", command=lambda: sortColumn(tree, "id", False))
    tree.heading("retailer", text="Retailer", command=lambda: sortColumn(tree, "retailer", False))
    tree.heading("amount", text="Amount", command=lambda: sortColumn(tree, "amount", False))
    tree.heading("date", text="Date", command=lambda: sortColumn(tree, "date", False))

    tree.column("id", width=50, anchor=CENTER)
    tree.column("retailer", width=120, anchor=CENTER)
    tree.column("amount", width=80, anchor=CENTER)
    tree.column("date", width=100, anchor=CENTER)

    tree.pack(side=LEFT, fill=BOTH, expand=True)

    for t in transactions:
        tree.insert("", END, values=(t[0], t[1], f"{t[2]}", t[3], t[4]))

    return tree


def confirmAdd(num, retailer, amount, dateStr, pane):
    dateStr = datetime.strptime(dateStr.strip(), "%Y-%m-%d").date()
    retailer = retailer.strip()

    if dateStr > date.today():
        fail_text = Label(pane, text="Please check the date")
        fail_text.grid(row=9, column=0, columnspan=2)
        return

    connection.addTransaction(num, amount, retailer, dateStr)
    displayTransactions(num, "show")
    pane.destroy()


def addTransaction(num):
    new = Toplevel(window)
    new.title("New Transaction")
    new.geometry("275x275")

    Label(new, text="Enter transaction data to add").grid(row=0, column=0, columnspan=2, ipadx=50)

    retailer_label = Label(new, text=f"Retailer", font=("Arial", 10))
    retailer_label.grid(row=2, column=0, columnspan=2, pady=10, padx=50)

    retailerBox = Entry(new, width=20, justify=CENTER)
    retailerBox.grid(row=3, column=0, padx=60, pady=5)

    amount_label = Label(new, text="Amount", font=("Arial", 10))
    amount_label.grid(row=4, column=0, columnspan=2, pady=10)

    amountBox = Entry(new, width=20, justify=CENTER)
    amountBox.grid(row=5, column=0, padx=70, pady=5)

    Date_label = Label(new, text="Date (YYYY-MM-DD)", font=("Arial", 10))
    Date_label.grid(row=6, column=0, columnspan=2, pady=10)

    DateBox = Entry(new, width=20, justify=CENTER)
    DateBox.grid(row=7, column=0, padx=80, pady=5)

    correct = Button(new, text="Submit",
                     command=lambda: confirmAdd(num, retailerBox.get().strip(),
                                                amountBox.get().strip(),
                                                DateBox.get().strip(), new))
    correct.grid(row=8, column=0, columnspan=2, pady=10)


global numberBox


def confirmEdit(num, trans_id, retailer, amount, dateT, pane):
    amount = amount.strip()
    retailer = retailer.strip()
    dateT = dateT.strip()
    tran = connection.getTransaction(trans_id)

    if retailer == "":
        retailer = tran[5]
    if amount == "":
        amount = tran[4]
    if dateT == "":
        dateStr = datetime.strptime(str(tran[1]), "%Y-%m-%d").date()
    else:
        dateStr = datetime.strptime(dateT, "%Y-%m-%d").date()

    if dateStr > date.today():
        fail_text = Label(pane, text="Please check the date")
        fail_text.grid(row=8, column=0, columnspan=2)
        return

    connection.editTransaction(trans_id, retailer, amount, dateStr)
    displayTransactions(num, "show")
    pane.destroy()


def editTransaction(accountNumber, listbox):
    global fail_text

    if fail_text:
        fail_text.grid_forget()
        fail_text = None

    selection = listbox.selection()
    if not selection:
        fail_text = ttk.Label(window, text="Please select a transaction to edit")
        fail_text.grid(row=7, column=0, columnspan=2, pady=5)
        return

    values = listbox.item(selection[0], "values")
    id = values[4]

    new = Toplevel(window)
    new.title("Edit Transaction")
    new.geometry("275x275")

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
    retailer_label.grid(row=3, column=0, pady=10)

    retailerBox = Entry(new, width=10)
    retailerBox.grid(row=3, column=1, ipadx=10)

    amount_label = Label(new, text="Amount", font=("Arial", 10))
    amount_label.grid(row=4, column=0, pady=10)

    amountBox = Entry(new, width=10)
    amountBox.grid(row=4, column=1, ipadx=10, padx=10)

    date_label = Label(new, text="Date", font=("Arial", 10))
    date_label.grid(row=5, column=0, pady=10)

    dateBox = Entry(new, width=10)
    dateBox.grid(row=5, column=1, ipadx=10)

    correct = Button(new, text="Submit",
                     command=lambda: confirmEdit(accountNumber, id, retailerBox.get().strip(), amountBox.get().strip(),
                                                 dateBox.get().strip(), new))
    correct.grid(row=6, column=0, columnspan=2, pady=20)


def chart_Transactions(num, action):
    action = action.lower()
    total = 0
    transactions = connection.getTransactions(num)
    retailers = []
    for h in transactions:
        if h[1] not in retailers:
            retailers.append(h[1])
    costPerRetailer = []

    for index in retailers:
        cost = 0
        for i in transactions:
            if i[1] == index:
                cost += float(i[2].split('$')[1])
                total += float(i[2].split('$')[1])
        costPerRetailer.append([index.strip(" "), round(float(cost), 2)])

    x = []
    y = []

    for i in costPerRetailer:
        wrappedX = textwrap.fill(i[0], width=10)
        x = np.append(x, wrappedX)
        y = np.append(y, i[1])

    if action == "pie":
        if plt.get_fignums():
            plt.close()
        plt.title("Money spent per retailer as a whole")
        plt.pie(y, labels=x, autopct=lambda p: '${:.2f}'.format(p * sum(y) / 100))
        plt.title(f"Money Spent as a whole: ${round(total, 2)}")
        plt.show()
    else:
        if plt.get_fignums():
            plt.close()

        plt.figure(figsize=(7.5, 6))
        plt.ylabel("Money Spent ($)")
        plt.xlabel("Retailer")
        plt.title("Money Spent per Retailer")
        bars = plt.bar(x, y)
        plt.bar_label(bars)
        plt.show()


def getSessionTime():
    return round(time.time() - startTime, 2)


def logout():
    global fail_text

    for widget in window.winfo_children():
        widget.destroy()

    fail_text = None

    registration()


startTime = time.time()
registration()

window.mainloop()

from tkinter import *
from tkinter import ttk
import re

from Objects import transaction as transaction
from DB.connection import *

GEOMETRY_DEFAULT = "800x600"


def view_transactions():
    transactions = []
    with open("../Data/transaction_data.csv", "r") as myFile:
        for line in myFile:
            if line.split(',')[0] == 'dateCreated':
                pass
            else:
                transactions.append(line)
    return transactions


def sortByAccount():
    # account_id = Text(window, width=20, height=1)
    # account_id.pack()
    transactions = view_transactions()
    sorted_transactions1 = []
    sorted_transactions2 = []
    for t in range(len(transactions)):
        line_split = transactions[t].split(',')
        if line_split[1] == 'dateCreated':
            pass
        elif line_split[1] == '0':
            sorted_transactions1.append(transactions[t])
        else:
            sorted_transactions2.append(transactions[t])
    for i in range(len(sorted_transactions2)):
        sorted_transactions1.append(sorted_transactions2[i])
    return sorted_transactions1


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
    # Make Logic to compare to registered accounts


button = Button(window, text="Submit", command=submit)
button.pack(pady=20)

# View_button = ttk.Button(window, text="View Transactions", command=view_transactions)
# View_button.pack()
#
# Sort_button = ttk.Button(window, text="Sort by account", command=sortByAccount)
# Sort_button.pack()


# transactions = view_transactions()
# transvar = StringVar(value=transactions)
#
# viewer = Listbox(window, listvariable=transvar, height=3, width=50)
# viewer.pack()
#
# transactions2 = sortByAccount()
# Stransvar = StringVar(value=transactions)
#
# Sviewer = Listbox(window, listvariable=transvar, height=3, width=50)
# Sviewer.pack()

window.mainloop()

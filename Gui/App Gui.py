from tkinter import *
from tkinter import ttk
import re

GEOMETRY_DEFAULT = "800x600"


def submit():
    print("Information submitted, please wait for verification")
    # Make Logic to compare to registered accounts


def getCurrentGeometry():
    wGeo = re.split(r'[x,+]', window.geometry())
    windowW = wGeo[0]
    windowH = wGeo[1]
    return windowW, windowH


window = Tk()

window.bind("<q>", END)

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

button = Button(window, text="Submit", command=submit)
button.pack(pady=20)

window.mainloop()

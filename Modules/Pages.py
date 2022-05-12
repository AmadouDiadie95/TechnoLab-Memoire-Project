import tkinter as tk
from tkinter import *

from prettytable import PrettyTable

class Page(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
    def show(self, event=None):
        self.lift()

#   Main menu
class Menu(Page):
    def __init__(self, w):
        Page.__init__(self)
        e = Entry(self, width=30, font=('Helvetica', 24)).grid(row=5, column=0)
        # e = Entry(root, borderwidth=5 (change border size) )
        e.pack()

        def myClick():
            hello = "Hello " + e.get()  # get function return you what's inside your entry
            myLabel = Label(self, text=hello)
            e.delete(0, 'end')
            myLabel.pack()

        myButton = Button(self, text="Login", command=myClick)
        myButton.pack()


class Page2(Page):
    def __init__(self, w):
        Page.__init__(self)
        label = tk.Label(self, text="Page 1")
        label.place(x=(w/2), y=25, anchor="center")



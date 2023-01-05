# GUI
import tkinter
from tkinter import *
from tkinter import Entry, Label, Button, simpledialog


# import panda knihovny
import pandas as pd

# db loading
db = pd.read_excel('chemical_db.xlsx')


def find():
    chemical = simpledialog.askstring('Find chemical', 'Enter name')
    print(db[db.compound.str.contains(chemical)])


root = Tk()

find_chemical = Button(root, text='Find chemical', command=find)
find_chemical.pack()


root.geometry('300x300')
root.mainloop()





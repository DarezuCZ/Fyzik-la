# GUI #############################################################################################################
import tkinter as tk
from tkinter import *
from tkinter import Entry, Label, Button, simpledialog, ttk, Tk


# import panda knihovny
import pandas as pd

# db loading
db = pd.read_excel('chemical_db.xlsx')

# Popup window with search and results ############################################################################
def find():
    chemical = simpledialog.askstring('Find chemical', 'Enter name')
    while chemical == '':
        chemical = simpledialog.askstring('Find chemical', 'Enter name')
    
    results_win = tk.Tk()
    results_win.title('Chemicals found:')
    results_win.lift(root)
    results_win.iconbitmap('listICO.ico')

    results = ttk.Label(results_win, text = db[db.compound.str.contains(chemical)])
    results.pack()

    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        results_win.mainloop()
        print(db[db.compound.str.contains(chemical)])

# Root + Buttons ##################################################################################################
root = Tk(screenName='Chemical database', baseName='Chemical database')
root.title('Chemical database')
root.geometry('400x100+600+300')
root.iconbitmap('listICO.ico')

find_chemical = Button(root, text='Find chemical', command=find)
find_chemical.pack()

add_chemical = Button(root, text='Add chemical')
add_chemical.pack()

update_chemical = Button(root, text='Update chemical')
update_chemical.pack()

delete_chemical = Button(root, text='Delete chemical')
delete_chemical.pack()


try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()

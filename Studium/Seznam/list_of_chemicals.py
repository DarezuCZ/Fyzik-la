# GUI #############################################################################################################
import tkinter as tk
from tkinter import *
from tkinter import Entry, Label, Button, simpledialog, ttk, Tk, Text


# import panda knihovny
import pandas as pds
from pandas import option_context

# db loading
db = pds.read_excel('chemical_db.xlsx', usecols="A,F,G,H,I", keep_default_na=False)

# Popup window with search and results ############################################################################
def find():
    chemical = simpledialog.askstring('Find chemical', 'Enter name')
    synonym = chemical
    while chemical == '':
        chemical = simpledialog.askstring('Find chemical', 'Enter name')
    
    results_win = tk.Tk()
    results_win.title('Chemicals found:')
    results_win.lift(root)
    results_win.iconbitmap('listICO.ico')
    results_win.grid_columnconfigure(0, weight=1)
    results_win.grid_rowconfigure(0, weight=1)

    with pds.option_context('display.max_rows', None, 'display.max_colwidth', 40):
        found = tk.Text(results_win, wrap=WORD, height=30, width=105, font=('Arial', 13), spacing1=1, spacing3=1)
        found.grid(row=0, column=0, sticky=tk.EW)
        found_scrollbar = ttk.Scrollbar(results_win, orient='vertical', command=found.yview)
        found_scrollbar.grid(row=0, column=1, sticky=tk.NS)
        found['yscrollcommand'] = found_scrollbar.set
        found_compounds = db[db.compound.str.startswith(chemical)]
        '''found_synonym = db[db.synonyms.str.startswith(chemical)]'''
        found.insert('0.0', found_compounds)
        '''results_compound = ttk.Label(results_win, text = db[db.compound.str.contains(chemical)], font=('Arial', 10)).pack(expand=True)
        results_synonyms = ttk.Label(results_win, text = db[db.synonyms.str.contains(chemical)], font=('Arial', 10)).pack(expand=True)'''


    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        results_win.mainloop()



# Root + Buttons ##################################################################################################
root = Tk(screenName='Chemical database', baseName='Chemical database')
root.title('Chemical database')
root.geometry('350x350+600+300')
root.iconbitmap('listICO.ico')
root_background = tk.PhotoImage(file='background_resized.png')
root_background_set = tk.Label(root, image=root_background, compound='left').pack()

find_chemical_icon = tk.PhotoImage(file='chemical_res.png')
find_chemical = tk.Button(root, text='Find chemical', compound=tk.LEFT, font=('Arial', 10), command=find, image=find_chemical_icon, height=40, width=140)
find_chemical.pack()

add_chemical_icon = tk.PhotoImage(file='plus_res.png')
add_chemical = tk.Button(root, text='Add chemical', compound=tk.LEFT, font=('Arial', 10), image=add_chemical_icon, height=40, width=140)
add_chemical.pack()

update_chemical_icon = tk.PhotoImage(file='captcha_res.png')
update_chemical = tk.Button(root, text='Update chemical', compound=tk.LEFT, font=('Arial', 10), image=update_chemical_icon, height=40, width=140)
update_chemical.pack()

delete_chemical_icon = tk.PhotoImage(file='minus_res.png')
delete_chemical = tk.Button(root, text='Delete chemical', compound=tk.LEFT, font=('Arial', 10), image=delete_chemical_icon, height=40, width=140)
delete_chemical.pack()


try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()

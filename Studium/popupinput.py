from tkinter import *
from tkinter import simpledialog

def get_me():
    s = simpledialog.askstring('input string', 'enter name')
    print(s)

root = Tk()

button = Button(root, text='popup', command=get_me)
button.pack()


root.geometry('300x300')
root.mainloop()
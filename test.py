from tkinter import *
from tkinter import messagebox

master = Tk()

def callback():
    global buttonClicked
    buttonClicked = not buttonClicked

buttonClicked = False

b = Button(master, text="smth", command=callback)
b.pack()


if (buttonClicked == True):
    messagebox.showinfo("Attention !!!!!!!",'Incorrect Entry')
mainloop()
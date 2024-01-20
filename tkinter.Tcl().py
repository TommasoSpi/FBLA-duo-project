from tkinter import *


root = Tk()
root.configure(bg="white", padx=10, pady=10)
root.title("WELCOME- PLEASE LOGIN)")

name = Label(root, text="Name:", bg="white")
password = Label(root, text="Password", bg="white")
nameentry = Entry(root)
passwordentry = Entry(root)

name.grid(row=0, sticky=E)
password.grid(row=1, sticky=E)
nameentry.grid(row=0, column=1)
passwordentry.grid(row=1, column=1)

mainloop()
from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title("get text demo")
ws.geometry("200x200")

def welcomeMessage():
    name = name_Tf.get()
    return messagebox.showinfo("Message",f'Hi!{name},Welcome to python.')



Label(ws,text="Enter name").pack()
name_Tf = Entry(ws)
name_Tf.pack()

Button(ws, text="click here", command=welcomeMessage).pack()

ws.mainloop()
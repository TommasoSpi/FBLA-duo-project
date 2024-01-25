import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox



#create the prent window
root = tk.Tk()

#title to the parent window
root.title("FBLA Project - Attandance Tracker")
root.geometry("600x600")

# notebook can accept height, padding, width
tabControl = ttk.Notebook(root)

# creating tab frames
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)

# adding tabs
tabControl.add(tab1, text="Home")
tabControl.add(tab2, text="Students")
tabControl.add(tab3, text="Events")
tabControl.add(tab4, text="Prizes")
tabControl.add(tab5, text="FAQ")

# making tabs visible
tabControl.pack(expand=1, fill="both")

# creates what is inside of each tab 

# tab1
ttk.Label(tab1,text="Welcome to Home").grid(column=0,row=0,padx=5,pady=5)

# tab2
ttk.Label(tab2,text="First Name").grid(column=0,row=0,padx=5,pady=5)
#tk.Entry(tab2, textvariable="fname").grid(column=1,row=0,padx=10,pady=10)
ttk.Label(tab2,text="Last Name").grid(column=0,row=2,padx=5,pady=5)
#tk.Entry(tab2, textvariable="lname").grid(column=1,row=2,padx=10,pady=10)
# enter command to store info somewhere
mEntryname = Entry(tab2)
mEntryname.grid(column=1,row=0,padx=0,pady=5)

nEntryname = Entry(tab2)
nEntryname.grid(column=1,row=2,padx=10,pady=0)

mSave = Button (tab2,text="save",bg="white", command = lambda:mstore(mEntryname.get())).grid(column=1,row=3,padx=10,pady=0)
# error command for when no info is submitted == messagebox.showinfo("Attention !!!!!!!",'Incorrect Entry')
if (nEntryname == None):
    messagebox.showinfo("Attention !!!!!!!",'Incorrect Entry')

# tab3
ttk.Label(tab3,text="Welcome to Events").grid(column=0,row=0,padx=5,pady=5)

# tab4
ttk.Label(tab4,text="Welcome to Prizes").grid(column=0,row=0,padx=5,pady=5)

# tab5
ttk.Label(tab5,text="Welcome to FAQ").grid(column=0,row=0,padx=5,pady=5)

# store info into text file
def mstore(text):
    file = open("file.txt","a") #w for write a for append
    file.write(text)
    file.write("\n")
    file.close()

# searches/reads the text file
def msearch():
    #file = filedialog.askopenfilename()
    open_file = open("file.txt", "r")
    print(open_file.read())
    open_file.close()


# makes program run

root.mainloop()
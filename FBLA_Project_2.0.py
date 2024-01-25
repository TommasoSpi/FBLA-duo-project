import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

#create the parent window
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
def writetofile():
    userEntryList = [ivn1.get(), ivn2.get(), ivn3.get(), ivn4.get()]

    print("\n".join(userEntryList))
    with open("file.txt","a") as f:
        for item in userEntryList:
            f.write("%s\n" % item)

ttk.Label(tab2,text="First Name").grid(column=0,row=0,padx=5,pady=5)
#tk.Entry(tab2, textvariable="fname").grid(column=1,row=0,padx=10,pady=10)
ttk.Label(tab2,text="Last Name").grid(column=0,row=1,padx=5,pady=5)
#tk.Entry(tab2, textvariable="lname").grid(column=1,row=2,padx=10,pady=10)
ttk.Label(tab2,text="Student ID").grid(column=0,row=2,padx=5,pady=5)

ttk.Label(tab2,text="Grade Level").grid(column=0,row=3,padx=5,pady=5)
## enter command to store info somewhere
#userEntryList = []
ivn1 = StringVar()
userEntry_1 = Entry(tab2, textvariable=str(ivn1))
#userEntryList.append(userEntry)
userEntry_1.grid(column=1,row=0,padx=0,pady=5)

ivn2 = StringVar()
userEntry_2 = Entry(tab2, textvariable=str(ivn2))
#userEntryList.append(userEntry)
userEntry_2.grid(column=1,row=1,padx=10,pady=0)

ivn3 = StringVar()
userEntry_3 = Entry(tab2, textvariable=str(ivn3))
userEntry_3.grid(column=1,row=2,padx=10,pady=0)

gradeLevel = ["Select Grade", 9,10,11,12]
ivn4 = StringVar(tab2)
ivn4.set(gradeLevel[0])

userEntry_4 = OptionMenu(tab2, ivn4, *gradeLevel)
userEntry_4.grid(column=1,row=3,padx=10,pady=0)


#mSave = Button (tab2,text="save",bg="white", command = lambda:mstore(userEntryList)).grid(column=1,row=3,padx=10,pady=0)
mSave = Button (tab2,text="save", command = writetofile)
mSave.grid(column=1,row=4,padx=10,pady=0)
## error command for when no info is submitted == messagebox.showinfo("Attention !!!!!!!",'Incorrect Entry')
if (userEntry_1 == None):
    messagebox.showinfo("Attention !!!!!!!",'Incorrect Entry')
if (userEntry_2 == None):
    messagebox.showinfo("Attention !!!!!!!",'Incorrect Entry')

# tab3
ttk.Label(tab3,text="Welcome to Events").grid(column=0,row=0,padx=5,pady=5)
# tab4
ttk.Label(tab4,text="Welcome to Prizes").grid(column=0,row=0,padx=5,pady=5)
# tab5
ttk.Label(tab5,text="Welcome to FAQ").grid(column=0,row=0,padx=5,pady=5)

# store info into text file
def mstore(text):
    with open("file.txt","a") as file: #w for write a for append
        for item in text:
            x = item[:-1]
            file.append(x)
    #file.write(text)
    #file.write("\n")
    #file.close()
            


# searches/reads the text file
def msearch():
    #file = filedialog.askopenfilename()
    open_file = open("file.txt", "r")
    print(open_file.read())
    open_file.close()


# makes program run

root.mainloop()
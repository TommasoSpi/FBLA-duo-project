import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import customtkinter

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
Label(tab1,text="↑ Welcome to the Edison Attendence Tracker!", font=("arial","20")).grid(column=1,row=1,padx=5,pady=0)
Label(tab1, text="↑ Click on the above tabs to explore our program!", font=("arial","10")).grid(column=1,row=2,padx=5,pady=5)
Label(tab1, text="", font=("arial","10")).grid(column=1,row=3,padx=5,pady=5)

# tab2
def writetofile():
    userEntryList = [ivn1.get(), ivn2.get(), ivn3.get(), ivn4.get(), str(choice_1.get() + choice_2.get() + choice_3.get() + choice_4.get() + choice_5.get() + choice_6.get() + choice_7.get() + choice_8.get() + choice_9.get() + choice_10.get())]

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

ttk.Label(tab2,text="Sports").grid(column=0,row=4,padx=5,pady=5)
ttk.Label(tab2,text="Academics").grid(column=1,row=4,padx=5,pady=5)
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

choice_1 = tk.IntVar()
choice_2 = tk.IntVar()
choice_3 = tk.IntVar()
choice_4 = tk.IntVar()
choice_5 = tk.IntVar()
choice_6 = tk.IntVar()
choice_7 = tk.IntVar()
choice_8 = tk.IntVar()
choice_9 = tk.IntVar()
choice_10 = tk.IntVar()


# Sports Events
Event_1 = tk.Checkbutton(tab2, text='Football',variable=choice_1, onvalue=100, offvalue=0)
Event_1.grid(column=0,row=5,padx=5,pady=0)

Event_2 = tk.Checkbutton(tab2, text='Basketball',variable=choice_2, onvalue=200, offvalue=0)
Event_2.grid(column=0,row=6,padx=5,pady=0)

Event_3 = tk.Checkbutton(tab2, text='Volleyball',variable=choice_3, onvalue=300, offvalue=0)
Event_3.grid(column=0,row=7,padx=5,pady=0)

Event_4 = tk.Checkbutton(tab2, text='Soccer',variable=choice_4, onvalue=400, offvalue=0)
Event_4.grid(column=0,row=8,padx=5,pady=0)

Event_5 = tk.Checkbutton(tab2, text='Lacrosse',variable=choice_5, onvalue=500, offvalue=0)
Event_5.grid(column=0,row=9,padx=5,pady=0)

# Academic Events
Event_6 = tk.Checkbutton(tab2, text='Homecoming',variable=choice_6, onvalue=100, offvalue=0)
Event_6.grid(column=1,row=5,padx=5,pady=0)

Event_7 = tk.Checkbutton(tab2, text='Prom',variable=choice_7, onvalue=200, offvalue=0)
Event_7.grid(column=1,row=6,padx=5,pady=0)

Event_8 = tk.Checkbutton(tab2, text='Theater Play',variable=choice_8, onvalue=300, offvalue=0)
Event_8.grid(column=1,row=7,padx=5,pady=0)

Event_9 = tk.Checkbutton(tab2, text='Concert',variable=choice_9, onvalue=400, offvalue=0)
Event_9.grid(column=1,row=8,padx=5,pady=0)

Event_10 = tk.Checkbutton(tab2, text='International night',variable=choice_10, onvalue=500, offvalue=0)
Event_10.grid(column=1,row=9,padx=5,pady=0)

#choice_Total = tk.StringVar()
Total = choice_1.get() + choice_2.get() + choice_3.get() + choice_4.get() + choice_5.get() + choice_6.get() + choice_7.get() + choice_8.get() + choice_9.get() + choice_10.get()
#choice_Total = tk.StringVar(value = Total)


#mSave = Button (tab2,text="save",bg="white", command = lambda:mstore(userEntryList)).grid(column=1,row=3,padx=10,pady=0)
mSave = Button (tab2,text="save", command = writetofile)
mSave.grid(column=1,row=10,padx=10,pady=0)
## error command for when no info is submitted == messagebox.showinfo("Attention !!!!!!!",'Incorrect Entry')
if (userEntry_1 == None):
    messagebox.showinfo("Attention !!!!!!!",'Incorrect Entry')
if (userEntry_2 == None):
    messagebox.showinfo("Attention !!!!!!!",'Incorrect Entry')

# tab3
    #athletic
Label(tab3,text="Football: 100pts", font=("arial","10")).grid(column=5,row=1,padx=5,pady=5)
Label(tab3,text="Basketball: 200pts", font=("arial","10")).grid(column=5,row=2,padx=5,pady=5)
Label(tab3,text="Volleyball: 300pts", font=("arial","10")).grid(column=5,row=3,padx=5,pady=5)
Label(tab3,text="Soccer: 400pts", font=("arial","10")).grid(column=5,row=4,padx=5,pady=5)
Label(tab3,text="Lacrosse: 500pts", font=("arial","10")).grid(column=5,row=5,padx=5,pady=5)
    #Academic
Label(tab3,text="Homecoming: 100pts", font=("arial","10")).grid(column=6,row=1,padx=5,pady=5)
Label(tab3,text="Prom: 200pts", font=("arial","10")).grid(column=6,row=2,padx=5,pady=5)
Label(tab3,text="Theater play: 300pts", font=("arial","10")).grid(column=6,row=3,padx=5,pady=5)
Label(tab3,text="Concert: 400pts", font=("arial","10")).grid(column=6,row=4,padx=5,pady=5)
Label(tab3,text="International Night: 500pts", font=("arial","10")).grid(column=6,row=5,padx=5,pady=5)
# tab4
Label(tab4,text="School Prizes!",font=("arial","15")).grid(column=0,row=0,padx=5,pady=5)
Label(tab4,text="Eraser: 200pts",borderwidth=1, relief="solid").grid(column=0,row=1,padx=5,pady=5)
Label(tab4,text="Pencil: 200pts",borderwidth=1, relief="solid").grid(column=0,row=2,padx=5,pady=5)
Label(tab4,text="Pencil pouch: 600pts",borderwidth=1, relief="solid").grid(column=0,row=3,padx=5,pady=5)
Label(tab4,text="Homework pass: 1000pts",borderwidth=1, relief="solid").grid(column=0,row=4,padx=5,pady=5)

Label(tab4,text="Food Prizes",font=("arial","15")).grid(column=1,row=0,padx=5,pady=5)
Label(tab4,text="Happy meal: 200pts",borderwidth=1, relief="solid").grid(column=1,row=1,padx=5,pady=5)
Label(tab4,text="Burger: 400pts",borderwidth=1, relief="solid").grid(column=1,row=2,padx=5,pady=5)
Label(tab4,text="Pizza: 600pts",borderwidth=1, relief="solid").grid(column=1,row=3,padx=5,pady=5)
Label(tab4,text="Cake: 1000pts",borderwidth=1, relief="solid").grid(column=1,row=4,padx=5,pady=5)

Label(tab4,text="School Sprit Prizes",font=("arial","15")).grid(column=2,row=0,padx=5,pady=5)
Label(tab4,text="Pencil: 200pts",borderwidth=1, relief="solid").grid(column=2,row=1,padx=5,pady=5)
Label(tab4,text="T-shirt: 400pts",borderwidth=1, relief="solid").grid(column=2,row=2,padx=5,pady=5)
Label(tab4,text="Lanyard: 600pts",borderwidth=1, relief="solid").grid(column=2,row=3,padx=5,pady=5)
Label(tab4,text="Hoodie: 1000pts",borderwidth=1, relief="solid").grid(column=2,row=4,padx=5,pady=5)
# tab5
Label(tab5,text="Q: Where can I redeem my prizes?",font=("arial","15")).grid(column=0,row=0,padx=2,pady=2)
Label(tab5,text="A: The front desk.",font=("arial","15")).grid(column=0,row=1,padx=2,pady=2)
Label(tab5,text="",font=("arial","15")).grid(column=0,row=2,padx=2,pady=2)
Label(tab5,text="Q: How can I redeem my points?",font=("arial","15")).grid(column=0,row=3,padx=2,pady=2)
Label(tab5,text="A: Signing up for the event automatically redeems your points.",font=("arial","15")).grid(column=0,row=4,padx=2,pady=2)
Label(tab5,text="",font=("arial","15")).grid(column=0,row=5,padx=2,pady=2)
Label(tab5,text="Q: Why is your program so boring?",font=("arial","15")).grid(column=0,row=6,padx=2,pady=2)
Label(tab5,text="A: Because we wanted to go for a minimalist look",font=("arial","15")).grid(column=0,row=7,padx=2,pady=2)
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

#with open('file.txt') as input_file:
#    textList = []
#    for line in input_file:
#        line = line.strip()
#        textList.append(line)

def drawgrid():
    with open('file.txt') as input_file:
        textList = []
        for line in input_file:
            line = line.strip()
            textList.append(line)
    
    height = int(len(textList)/5) 
    width = 5
    for i in range(height): #Rows
        for j in range(width): #Columns
            b = Label(tab3, text=textList[5*i+j])
            b.grid(row=i, column=j)

mRefresh = Button (tab3,text="Refresh", command = drawgrid)
mRefresh.grid(column=1,row=10,padx=10,pady=0)
     
# makes program run

root.mainloop()
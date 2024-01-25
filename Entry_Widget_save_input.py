from tkinter import *
from tkinter import filedialog 

def mstore(text):
    file = open("file.txt","a")
    file.write(text)
    # adds a new line of writing
    file.write("\n")
    file.close()

def msearch():
    #file = filedialog.askopenfilename()
    open_file = open("file.txt", "r")
    print(open_file.read())
    open_file.close()

window = Tk()
window.geometry("450x500")
window.title("form Test")

mTitle = Label (window,text="heading Text",bg = "white")
mDetail =  Label (window,text="flavour you can see",bg = "white")
mFName = Label (window,text="barcode",bg = "white")
mEntryname = Entry(window)

mSave = Button (window,text="save",bg="white", command = lambda:mstore(mEntryname.get()))

mSearch = Button (window,text="search",bg="white", command= lambda: msearch())

mTitle.pack()
mDetail.pack()
mFName.pack()
mEntryname.pack()
mSave.pack()
mSearch.pack()

window.mainloop()
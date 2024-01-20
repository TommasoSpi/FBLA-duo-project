from tkinter import *
from tkinter import ttk
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

#app = customtkinter.CTk()  # create CTk window like you do with the Tk window
# app.geometry("400x240")
###app.grid_columnconfigure(1, weight=1) # this is needed only if there is only 1 button (make sure the weight is at least 1, not 0 )
#app = customtkinter.CTk()
#app.title("FBLA Project")
#app.geometry("400x150")
# app.grid_columnconfigure((0), weight=1)

#def button_function():
#    print("FART")

#def button_function2():
#    print("RAHHHH")

# Use CTkButton instead of tkinter Button
#button = customtkinter.CTkButton(master=app, text="Butt", command=button_function)
#button.place(relx=0.2, rely=0.1, anchor=customtkinter.W) #
#button.grid(row=1, column=1,padx=20, pady=20,columnspan=2 ) 
#button.grid(row=1, column=1, padx=20, pady=20, sticky="ew", columnspan=1)

#button1 = customtkinter.CTkButton(master=app, text='Scary', command=button_function2)
#button1.place(relx=0.6,rely=0.1,anchor=customtkinter.W)
#button1.grid(row=2, column=1, padx=40, pady=20, columnspan=2)

#checkbox_1 = customtkinter.CTkCheckBox(app, text="checkbox 1")
#checkbox_1.grid(row=1, column=3, padx=20, pady=(0, 20), sticky="w")
#checkbox_2 = customtkinter.CTkCheckBox(app, text="checkbox 2")
#checkbox_2.grid(row=2, column=3, padx=20, pady=(0, 20), sticky="w")






class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("FBLA Project")
        self.geometry("400x250")
        

        self.button_1 = customtkinter.CTkButton(self, text="Butt", command=self.button_function)
        self.button_1.place(relx=0.2, rely=0.1, anchor=customtkinter.CENTER) #
        self.button_1.grid(row=0, column=1,padx=20, pady=20,columnspan=2 ) 

        self.button_2 = customtkinter.CTkButton(self, text='Scary', command=self.button_function2)
        self.button_2.place(relx=0.6,rely=0.1,anchor=customtkinter.W)
        self.button_2.grid(row=2, column=1, padx=40, pady=20, columnspan=2)

    def button_function(self):
        print("PFFFFT")
    def button_function2(self):
        print("RAH")
app = App()
app.mainloop()
from tkinter import *
from tkinter import messagebox

def login():
    def clear_login():
        name_entry.delete(0, END)
        pass_entry.delete(0, END)
    Label(root, text="Name", font=10).place(x=600, y=380)
    Label(root, text="Password", font=10).place(x=600, y=410)

    name_info = StringVar()
    pass_info = StringVar()

    name_entry = Entry(root, font=10, textvariable=name_info)
    name_entry.place(x=700, y=380)
    pass_entry = Entry(root, font=10, textvariable=pass_info)
    pass_entry.place(x=700, y=410)

    Button(root, text="Enter", font=("BankGothic Lt BT", 15, "bold"), ).place(x=600, y=470)
    Button(root, text="Clear", font=("BankGothic Lt BT", 15, "bold"),command=clear_login).place(x=700, y=470)

def register():
    def clear_register():
        name_entry.delete(0, END)
        rollno_entry.delete(0, END)
        email_entry.delete(0, END)
        pass_entry.delete(0, END)
    def pass_check(password):
        l = 0
        u = 0
        p = 0
        d = 0
        if (len(password) >= 8):
            for i in password:
                if (i.islower()):
                    l += 1
                if (i.isupper()):
                    u += 1
                if (i.isdigit()):
                    d += 1
                if (i == '@' or i == '$' or i == '_'):
                    p += 1
        else:
            return False
        if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(password)):
            return True
        else:
            return False
    def check_credentials():
        name = name_info.get()
        rollno = rollno_info.get()
        email = email_info.get()
        password = pass_info.get()

        if name == "":
            messagebox.showerror("ERROR", "Please Enter your name.")
        elif rollno == "":
            messagebox.showerror("ERROR", "Please Enter your Roll Number.")
        elif email == "":
            messagebox.showerror("ERROR", "Please Enter your Email Address.")
        elif password == "":
            messagebox.showerror("ERROR", "Please set your Password.")
        else:
            pass

        if pass_check(password):
            Label(root, text="REGISTRATION SUCCESSFUL", font=("BankGothic Lt BT", 15), fg="green").place(x=30, y=580)
            Button(root, text="Proceed ->", font=("BankGothic Lt BT", 18, "bold")).place(x=650, y=550)
        else:
            messagebox.showerror("ERROR","Enter a valid password. Conditions:\n1.Lenght minimum 8 characters\n"
                                         "2.Minimum one lowercase, uppercase, special charater.")
        file = open("Records.txt", "a")
        file.write(name + " ")
        file.write(password + "\n")
        file.close()


    # Credentials for the form
    Label(root, text="Name", font=10).place(x=30, y=380)
    Label(root, text="Roll Number", font=10).place(x=30, y=410)
    Label(root, text="Email ID", font=10).place(x=30, y=440)
    Label(root, text="Password", font=10).place(x=30, y=470)

    # Entry Widgets(accepts entry)
    name_info = StringVar()
    rollno_info = StringVar()
    email_info = StringVar()
    pass_info = StringVar()

    name_entry = Entry(root, font=10, textvariable=name_info)
    name_entry.place(x=150, y=380)
    rollno_entry = Entry(root, font=10, textvariable=rollno_info)
    rollno_entry.place(x=150, y=410)
    email_entry = Entry(root, font=10, textvariable=email_info)
    email_entry.place(x=150, y=440)
    pass_entry = Entry(root, font=10, textvariable=pass_info)
    pass_entry.place(x=150, y=470)

    #Submit Button
    Button(root, text="Submit", font=("BankGothic Lt BT", 15, "bold"),command=check_credentials).place(x=30, y=530)
    Button(root, text="Clear", font=("BankGothic Lt BT", 15, "bold"),command=clear_register).place(x=150, y=530)
    name = name_info.get()
    rollno = rollno_info.get()
    email = email_info.get()
    password = pass_info.get()

    file = open("Records.txt", "a")
    file.write(name)
    file.write(password)
    file.close()


root = Tk()
#basis screen settings
root.geometry("1044x1044")
root.title("SomaiyaPay")
root.resizable(False, False)
#verical and horizontal red lines
text1 = Label(text = "Welcome to SomaiyaPay",bg = 'Red', fg = 'Black', padx = 233, pady = 4,
              font = ("BankGothic Lt BT", 18, "bold"), borderwidth = 3).pack(fill=X)
text2 = Label(text = "   ",bg = 'Red', borderwidth = 3).pack(side=LEFT, fill=Y)

#KJSCE logo
photo = PhotoImage(file = "KJSCE LOGO.PNG")
kjsce_logo = Label(image = photo)
kjsce_logo.pack()

#Buttons - Register and LogIn
Button(root,text="Register", font=("BankGothic Lt BT", 18, "bold"),command=register).place(x=250, y=300)
Button(root,text="Log In", font=("BankGothic Lt BT", 18, "bold"),command=login).place(x=650, y=300)


root.mainloop()

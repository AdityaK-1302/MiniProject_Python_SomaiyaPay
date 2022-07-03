import re
from tkinter import *
from tkinter import messagebox

class user:
    roll = []
    name = []
    password = []
    place  = -1
    balance = []
    def input(self,roll,name,password):
        self.roll.append(roll)
        self.name.append(name)
        self.password.append(password)
    def update(self):
        if(len(self.balance)==0):
            self.balance.append(0.0)
        if(len(self.balance)==self.place):
            self.balance.append(0.0)
        if(len(self.balance)<self.place):
            for i in range(len(self.balance),(self.place+1)):
                self.balance.append(0.0)    
    def add(self,amount):
        self.balance[self.place] += amount
    def subtract(self,amount):
        if(self.balance[self.place]<float(amount)):
            print("Insufficient Funds! Transaction Unsuccessful!")
        else:
            self.balance[self.place] -= float(amount)
            print("Transaction Successful!")
    def display(self):
        print("Roll No:",self.roll[self.place])
        print("Name:",self.name[self.place])
        print("Balance Left: Rs",self.balance[self.place])

class stationary:
    item = []
    number = []
    price = []
    total = 0
    def add(self,item,number,price):
        self.item.append(item)
        self.number.append(number)
        self.price.append(price)
        self.total += price
    def bill(self):
        a = len(self.item)
        print("The Final Bill is:")
        for i in range(0,a):
            print("Item:",self.item[i])
            print("Quantity:",self.number[i])
            print("Amount: Rs",self.price[i])
        print("The Total Amount is: Rs",self.total)
    def get_total(self):
        return self.total

class canteen:
    item = []
    number = []
    price = []
    total = 0
    def add(self,item,number,price):
        self.item.append(item)
        self.number.append(number)
        self.price.append(price)
        self.total += price
    def bill(self):
        a = len(self.item)
        print("The Final Bill is:")
        for i in range(0,a):
            print("Item:",self.item[i])
            print("Quantity:",self.number[i])
            print("Amount: Rs",self.price[i])
        print("The Total Amount is: Rs",self.total)
    def get_total(self):
        return self.total

def CheckR():
    print("Yes")
    if(Register() == 1):
        Menu()
        print("Yes")
        return 
    if(Register() == 0):
        messagebox.showerror("ERROR", "Account Already Exists! Please Login Instead!")
        return 

def CheckL():
    if(Login() == 1):
        Menu()
        return 
    if((Login() == 0)):
        if (len(r.roll)==0):
            messagebox.showerror("ERROR", "There are no Registered Users!")
        else:
            messagebox.showerror("ERROR", "There are no Registered Users with this Roll Number!")
        return 

def Register():
    Delete()
    roll_info = StringVar()
    Label(screen, text="PLEASE ENTER YOUR DETAILS",font = ("BankGothic Lt BT", 20,"bold")).place(x=50, y=50)
    Label(screen, text="Roll No:", font=18).place(x=50, y=100)
    roll_entry = Entry(screen, font=18,textvariable=roll_info)
    roll_entry.place(x=170, y=100)
    roll = roll_info.get()
    if((len(roll)==11) and (roll.isdigit())):
        print("Yes")
        for i in range(0,len(r.roll)):
            if (roll==r.roll[i]):
                return 0
    else:
        messagebox.showerror("ERROR", "There are no Registered Users!")
    name = input("Please Enter your Name: ")
    while(1):
        password = input("Please Enter a Valid Password(at least 6 digits):")
        if (len(password)>=6):
            break
        print("Incorrect Entry! Retry!")
    r.input(roll,name,password)
    for i in range(0,len(r.roll)):
            if (roll==r.roll[i]):
                r.place = i
                break
    return 1

def Login():
    if (len(r.roll)==0):
        return 0
    while(1):
        roll = input("Please Enter your Roll No: ")
        for i in range(0,len(r.roll)):
            if (roll==r.roll[i]):
                r.place = i
                break
        print("Incorrect Entry! Retry!")
    while(1):
        password = input("Please Enter Your Password:")
        if(password==r.password[i]):
            print("/nThank You For Logging into Somaiya Pay")
            break
        print("Incorrect Entry! Retry!")
    return 1

def Add():
    c = 0
    while(c==0):
        print("1. Credit Card")
        print("2. Unified Payments Interface(UPI)")
        choice = input("Please Select the number corresponding to the method you want to add money with: ")
        if (choice=='1'):
            c = 1
            while(1):
                card = input("Please Enter Credit Card Number: ")
                if((card.isdigit()) and (len(card)==16)):
                    break
                print("Incorrect Entry! Retry!")
            while(1):
                expiry = input("Please Enter the Expiration Date of your Credit Card Number (Format: MM/YYYY): ")
                exp = list(expiry)
                if(len(exp)!=7):
                    print("Incorrect Entry! Retry!")
                    continue
                if(exp[0]=='0'):
                    if((int(exp[1])<=0) and (int(exp[1])>=10)):
                        print("Incorrect Entry! Retry!")
                        continue
                if(exp[0]=='1'):
                    if((exp[1]!='0') and (exp[1]!='1') and (exp[1]!='2')):
                        print("Incorrect Entry! Retry!")
                        continue
                if(exp[2]!='/'):
                    print("Incorrect Entry! Retry!")
                    continue
                if(exp[3]!='2'):
                    print("Incorrect Entry! Retry!")
                    continue
                if(exp[4]!='0'):
                    print("Incorrect Entry! Retry!")
                    continue
                if(exp[5]!='2'):
                    print("Incorrect Entry! Retry!")
                    continue
                if((int(exp[6])<2) and (int(exp[6])>=10)):
                    print("Incorrect Entry! Retry!")
                    continue
                break
            while(1):
                cvv = input("Enter CVV: ")
                if((len(cvv)==3) and (cvv.isdigit())):
                    break
                print("Incorrect Entry! Retry!")
            while(1):
                amount = input("Enter the amount you want to add to your account in Rs:")
                if(float(amount)>=0):
                    print("Rs.{} Have Been added to your Somaiya Pay Account".format(amount))
                    r.add(float(amount))
                    break
                print("Incorrect Entry! Retry!")
        if(choice=='2'):
            c = 1
            while(1):
                upi=input("Enter UPI id:")
                if(len(upi)==21 and re.findall('\d{10}[@][s][o][m][a][i][y][a][p][a][y]',upi)):
                    break
                print("Incorrect Entry! Retry!")
            while(1):
                amount = input("Enter the amount you want to add to your account in Rs:")
                if(float(amount)>=0):
                    print("Rs.{} Have Been added to your Somaiya Pay Account".format(amount))
                    r.add(float(amount))
                    break
                print("Incorrect Entry! Retry!")    
        if(c==0):
            print("Incorrect Entry! Retry!")

def Stationary():
    s = stationary()
    a = 0
    while(a==0):
        print("Stationary Available:")
        print("1. Pens")
        print("2. Pencils")
        print("3. Rulers")
        print("4. Notebooks")
        print("5. Highlighters ")
        item = input("Please select the number corresponding to the item you want to buy?: ")
        if(item == '1'):
            a = 1
            print("Please select the type of pen you want to purchase:")
            print("1. Classmate Octane Gel Pen - Rs 10 per piece")
            print("2. Pilot G3 Roller Ink Gel Pen - Rs 5 per piece")
            while(1):
                sel = input("Please select the number corresponding to the item you want to buy?: ")
                if((sel == '1') or (sel == '2')):
                    while(1):
                        number = input("Enter the amount of pens you want to purchase: ")
                        if((int(number) > 0) and (number.isdigit())):
                            if(sel=='1'):
                                s.add("Classmate Octane Gel Pen - Rs 10 per piece",int(number),int(number)*10)
                            if(sel=='2'):
                                s.add("Pilot G3 Roller Ink Gel Pen - Rs 5 per piece",int(number),int(number)*5)
                            break
                        print("Incorrect Entry! Retry")
                    break
                print("Incorrect Entry! Retry")
        if(item == '2'):
            a = 1
            print("Please select the type of pencil you want to purchase:")
            print("1. Nataraj Pencils - Rs 5 per piece")
            print("2. Apsara Pencils - Rs 8 per piece")
            while(1):
                sel = input("Please select the number corresponding to the item you want to buy?: ")
                if((sel == '1') or (sel == '2')):
                    while(1):
                        number = input("Enter the amount of pencils you want to purchase: ")
                        if((int(number) > 0) and (number.isdigit())):
                            if(sel=='1'):
                                s.add("Nataraj Pencils - Rs 5 per piece",int(number),int(number)*5)
                            if(sel=='2'):
                                s.add("Apsara Pencils - Rs 8 per piece",int(number),int(number)*8)
                            break
                        print("Incorrect Entry! Retry")
                    break
                print("Incorrect Entry! Retry")
        if(item == '3'):
            a = 1
            print("Please select the type of ruler you want to purchase:")
            print("1. Doms Q Ruler 15 cm - Rs 25 per piece")
            print("2. Staedtler Ultra Flex Ruler 30 cm - Rs 30 per piece")
            while(1):
                sel = input("Please select the number corresponding to the item you want to buy?: ")
                if((sel == '1') or(sel == '2')):
                    while(1):
                        number = input("Enter the amount of rulers you want to purchase: ")
                        if((int(number) > 0) and (number.isdigit())):
                            if(sel=='1'):
                                s.add("Doms Q Ruler 15 cm - Rs 25 per piece",int(number),int(number)*25)
                            if(sel=='2'):
                                s.add("Staedtler Ultra Flex Ruler 30 cm - Rs 30 per piece",int(number),int(number)*30)
                            break
                        print("Incorrect Entry! Retry")
                    break
                print("Incorrect Entry! Retry")
        if(item == '4'):
            a = 1
            print("Please select the type of notebook you want to purchase:")
            print("1. Classmate long notebook 140 pages - 50 Rs per piece")
            print("2. Classmate Drawing Book Unruled, 40 Pages - Rs 30 per piece")
            while(1):
                sel = input("Please select the number corresponding to the item you want to buy?: ")
                if((sel == '1') or(sel == '2')):
                    while(1):
                        number = input("Enter the amount of notebooks you want to purchase: ")
                        if((int(number) > 0) and (number.isdigit())):
                            if(sel=='1'):
                                s.add("Classmate long notebook 140 pages - 50 Rs per piece",int(number),int(number)*50)
                            if(sel=='2'):
                                s.add("Classmate Drawing Book Unruled, 40 Pages - Rs 30 per piece",int(number),int(number)*30)
                            break
                        print("Incorrect Entry! Retry")
                    break
                print("Incorrect Entry! Retry")
        if(item == '5'):
            a = 1
            print("Please select the type of highlighter you want to purchase:")
            print("1. Cello Hi-lighter - Rs 20 per piece")
            print("2. Luxor 886 N Highlighter - Rs 25 per piece")
            while(1):
                sel = input("Please select the number corresponding to the item you want to buy?: ")
                if((sel == '1') or(sel == '2')):
                    while(1):
                        number = input("Enter the amount of highlighters you want to purchase: ")
                        if((int(number) > 0) and (number.isdigit())):
                            if(sel=='1'):
                                s.add("Cello Hi-lighter - Rs 20 per piecee",int(number),int(number)*20)
                            if(sel=='2'):
                                s.add("Luxor 886 N Highlighter - Rs 25 per piece",int(number),int(number)*25)
                            break
                        print("Incorrect Entry! Retry")
                    break
                print("Incorrect Entry! Retry")
        if(a==0):
            print("Incorrect Entry! Retry!")
            continue
        check = int(input("Enter 1 if you want to purchase more items: "))
        if(check==1):
            a = 0
    s.bill()
    r.subtract(s.get_total())

def Canteen():
    c = canteen()
    a = 0
    while(a==0):
        print("Items Available:")
        print("1. Snacks")
        print("2. Main Course")
        print("3. Beverages")
        item = input("Please select the number corresponding to the item you want to buy?: ")
        if(item == '1'):
            a = 1
            print("Please select the type of snack you want to purchase:")
            print("1. Cinnamon Churros - Rs 20")
            print("2. Cheese Sandwich - Rs 30")
            while(1):
                sel = input("Please select the number corresponding to the item you want to buy?: ")
                if((sel == '1') or (sel == '2')):
                    while(1):
                        number = input("Enter the amount of snacks you want to purchase: ")
                        if((int(number) > 0) and (number.isdigit())):
                            if(sel=='1'):
                                c.add("Cinnamon Churros - Rs 20",int(number),int(number)*20)
                            if(sel=='2'):
                                c.add("Cheese Sandwich - Rs 30",int(number),int(number)*30)
                            break
                        print("Incorrect Entry! Retry")
                    break
                print("Incorrect Entry! Retry")
        if(item == '2'):
            a = 1
            print("Please select the type of main course you want to purchase:")
            print("1. Spaghetti Bolognese - Rs 90")
            print("2. Cheese Pizza - Rs 60")
            while(1):
                sel = input("Please select the number corresponding to the item you want to buy?: ")
                if((sel == '1') or (sel == '2')):
                    while(1):
                        number = input("Enter the amount of main courses you want to purchase: ")
                        if((int(number) > 0) and (number.isdigit())):
                            if(sel=='1'):
                                c.add("Spaghetti Bolognese - Rs 90",int(number),int(number)*90)
                            if(sel=='2'):
                                c.add("Cheese Pizza - Rs 60",int(number),int(number)*60)
                            break
                        print("Incorrect Entry! Retry")
                    break
                print("Incorrect Entry! Retry")
        if(item == '3'):
            a = 1
            print("Please select the type of beverage you want to purchase:")
            print("1. Tea - Rs 15")
            print("2. Coffee - Rs 30")
            while(1):
                sel = input("Please select the number corresponding to the item you want to buy?: ")
                if((sel == '1') or(sel == '2')):
                    while(1):
                        number = input("Enter the amount of beverages you want to purchase: ")
                        if((int(number) > 0) and (number.isdigit())):
                            if(sel=='1'):
                                c.add("Tea - Rs 15",int(number),int(number)*15)
                            if(sel=='2'):
                                c.add("Coffee - Rs 30",int(number),int(number)*30)
                            break
                        print("Incorrect Entry! Retry")
                    break
                print("Incorrect Entry! Retry")
        if(a==0):
            print("Incorrect Entry! Retry!")
            continue
        check = int(input("Enter 1 if you want to purchase more items: "))
        if(check==1):
            a = 0
    c.bill()
    r.subtract(c.get_total()) 

def Menu():
    Button(screen, text="Add Money", font=("BankGothic Lt BT", 18),command=Add).place(x=50, y=50)
    Button(screen, text="Purchase", font=("BankGothic Lt BT", 18),command=CheckP).place(x=50, y=110)
    Button(screen, text="Balance", font=("BankGothic Lt BT", 18),command=r.display).place(x=50, y=170)
    Button(screen, text="Logout", font=("BankGothic Lt BT", 18),command=Mains).place(x=50, y=230)

def CheckP():
    Button(screen, text="Stationary", font=("BankGothic Lt BT", 18),command=Stationary).place(x=50, y=50)
    Button(screen, text="Canteen", font=("BankGothic Lt BT", 18),command=Canteen).place(x=50, y=110)

def Exit():
    quit()

def Mains():
    Button(screen, text="Register", font=("BankGothic Lt BT", 18),command=CheckR).place(x=50, y=150)
    Button(screen, text="Login", font=("BankGothic Lt BT", 18),command=CheckL).place(x=50, y=210)
    Button(screen, text="Exit", font=("BankGothic Lt BT", 18),command=Exit).place(x=50, y=270)

def Delete():
    frame = Frame(screen)
    frame.pack(side="top", expand=True, fill="both")
    for widgets in frame.winfo_children():
        widgets.destroy()


screen = Tk()
screen.geometry("1044x1044")
text1 = Label(text = "SomaiyaPay",bg = 'Red', fg = 'Black', padx = 233, pady = 4, font = ("BankGothic Lt BT", 18, "bold"), borderwidth = 3).pack(fill=X)
text2 = Label(text = "   ",bg = 'Red', borderwidth = 3).pack(side=LEFT, fill=Y)
Label(screen, text="WELCOME TO SOMAIYA PAY",font = ("BankGothic Lt BT", 20,"bold")).place(x=325, y=50)
Label(screen, text="What Would You Like to Do Today? ",font = ("BankGothic Lt BT", 18,"bold")).place(x=50, y=100)
r = user()
Mains()

screen.mainloop()
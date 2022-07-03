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
                                c.add("Spaghetti Bolognese - Rs 90",int(number),int(number)*5)
                            if(sel=='2'):
                                c.add("Cheese Pizza - Rs 60",int(number),int(number)*8)
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
                                c.add("Tea - Rs 15",int(number),int(number)*25)
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

class stationary:
    item = []
    number = []
    price = []
    total = 0

    def add(self, item, number, price):
        self.item.append(item)
        self.number.append(number)
        self.price.append(price)
        self.total += price

    def bill(self):
        a = len(self.item)
        print("The Final Bill is:")
        for i in range(0, a):
            print("Item:", self.item[i])
            print("Quantity:", self.number[i])
            print("Amount: Rs", self.price[i])
        print("The Total Amount is: Rs", self.total)


def Stationary():
    s = stationary()
    a = 0
    while (a == 0):
        print("Stationary Available:")
        print("1. Pens")
        print("2. Pencils")
        print("3. Rulers")
        print("4. Notebooks")
        print("5. Highlighters ")
        item = input(
            "Please select the number corresponding to the item you want to buy?: "
        )
        if (item == '1'):
            a = 1
            print("Please select the type of pen you want to purchase:")
            print("1. Classmate Octane Gel Pen - Rs 10 per piece")
            print("2. Pilot G3 Roller Ink Gel Pen - Rs 5 per piece")
            while (1):
                sel = input(
                    "Please select the number corresponding to the item you want to buy?: "
                )
                if ((sel == '1') or (sel == '2')):
                    while (1):
                        number = input(
                            "Enter the amount of pens you want to purchase: ")
                        if ((int(number) > 0) and (number.isdigit())):
                            if (sel == '1'):
                                s.add(
                                    "Classmate Octane Gel Pen - Rs 10 per piece",
                                    int(number),
                                    int(number) * 10)
                            if (sel == '2'):
                                s.add(
                                    "Pilot G3 Roller Ink Gel Pen - Rs 5 per piece",
                                    int(number),
                                    int(number) * 5)
                            break
                        print("Incorrect Entry! Retry")
                    break
                print("Incorrect Entry! Retry")
        if (item == '2'):
            a = 1
            print("Please select the type of pencil you want to purchase:")
            print("1. Nataraj Pencils - Rs 5 per piece")
            print("2. Apsara Pencils - Rs 8 per piece")
            while (1):
                sel = input(
                    "Please select the number corresponding to the item you want to buy?: "
                )
                if ((sel == '1') or (sel == '2')):
                    while (1):
                        number = input(
                            "Enter the amount of pencils you want to purchase: "
                        )
                        if ((int(number) > 0) and (number.isdigit())):
                            if (sel == '1'):
                                s.add("Nataraj Pencils - Rs 5 per piece",
                                      int(number),
                                      int(number) * 5)
                            if (sel == '2'):
                                s.add("Apsara Pencils - Rs 8 per piece",
                                      int(number),
                                      int(number) * 8)
                            break
                        print("Incorrect Entry! Retry")
                    break
                print("Incorrect Entry! Retry")
        if (item == '3'):
            a = 1
            print("Please select the type of ruler you want to purchase:")
            print("1. Doms Q Ruler 15 cm - Rs 25 per piece")
            print("2. Staedtler Ultra Flex Ruler 30 cm - Rs 30 per piece")
            while (1):
                sel = input(
                    "Please select the number corresponding to the item you want to buy?: "
                )
                if ((sel == '1') or (sel == '2')):
                    while (1):
                        number = input(
                            "Enter the amount of rulers you want to purchase: "
                        )
                        if ((int(number) > 0) and (number.isdigit())):
                            if (sel == '1'):
                                s.add("Doms Q Ruler 15 cm - Rs 25 per piece",
                                      int(number),
                                      int(number) * 25)
                            if (sel == '2'):
                                s.add(
                                    "Staedtler Ultra Flex Ruler 30 cm - Rs 30 per piece",
                                    int(number),
                                    int(number) * 30)
                            break
                        print("Incorrect Entry! Retry")
                    break
                print("Incorrect Entry! Retry")
        if (item == '4'):
            a = 1
            print("Please select the type of notebook you want to purchase:")
            print("1. Classmate long notebook 140 pages - 50 Rs per piece")
            print(
                "2. Classmate Drawing Book Unruled, 40 Pages - Rs 30 per piece"
            )
            while (1):
                sel = input(
                    "Please select the number corresponding to the item you want to buy?: "
                )
                if ((sel == '1') or (sel == '2')):
                    while (1):
                        number = input(
                            "Enter the amount of notebooks you want to purchase: "
                        )
                        if ((int(number) > 0) and (number.isdigit())):
                            if (sel == '1'):
                                s.add(
                                    "Classmate long notebook 140 pages - 50 Rs per piece",
                                    int(number),
                                    int(number) * 50)
                            if (sel == '2'):
                                s.add(
                                    "Classmate Drawing Book Unruled, 40 Pages - Rs 30 per piece",
                                    int(number),
                                    int(number) * 30)
                            break
                        print("Incorrect Entry! Retry")
                    break
                print("Incorrect Entry! Retry")
        if (item == '5'):
            a = 1
            print(
                "Please select the type of highlighter you want to purchase:")
            print("1. Cello Hi-lighter - Rs 20 per piece")
            print("2. Luxor 886 N Highlighter - Rs 25 per piece")
            while (1):
                sel = input(
                    "Please select the number corresponding to the item you want to buy?: "
                )
                if ((sel == '1') or (sel == '2')):
                    while (1):
                        number = input(
                            "Enter the amount of highlighters you want to purchase: "
                        )
                        if ((int(number) > 0) and (number.isdigit())):
                            if (sel == '1'):
                                s.add("Cello Hi-lighter - Rs 20 per piecee",
                                      int(number),
                                      int(number) * 20)
                            if (sel == '2'):
                                s.add(
                                    "Luxor 886 N Highlighter - Rs 25 per piece",
                                    int(number),
                                    int(number) * 25)
                            break
                        print("Incorrect Entry! Retry")
                    break
                print("Incorrect Entry! Retry")
        if (a == 0):
            print("Incorrect Entry! Retry!")
            continue
        check = int(input("Enter 1 if you want to purchase more items: "))
        if (check == 1):
            a = 0
    s.bill()


Stationary()

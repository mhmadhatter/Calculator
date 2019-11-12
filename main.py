from tkinter import *

root = Tk()
root.title("Calculator")
# Frame for the entry field
field = Frame(root)
field.pack(side=TOP, expand=False, fill=BOTH)

# Frame for the numbers
digits = Frame(root, width=200, height=300)
digits.pack_propagate(0)
digits.pack(side=LEFT, expand=True, fill=BOTH)

row1 = Frame(digits)
row1.pack(expand=True, fill=BOTH)

row2 = Frame(digits)
row2.pack(expand=True, fill=BOTH)

row3 = Frame(digits)
row3.pack(expand=True, fill=BOTH)

row4 = Frame(digits)
row4.pack(expand=True, fill=BOTH)

#row5 = Frame(digits)
#row5.pack(expand=True, fill=BOTH)


# Frame for the operators
others = Frame(root, width=75, height=300)
others.pack_propagate(0)
others.pack(side=RIGHT, expand=True, fill=BOTH)

row_1 = Frame(others)
row_1.pack(expand=True, fill=BOTH)

row_2 = Frame(others)
row_2.pack(expand=True, fill=BOTH)

row_3 = Frame(others)
row_3.pack(expand=True, fill=BOTH)

row_4 = Frame(others)
row_4.pack(expand=True, fill=BOTH)

row_5 = Frame(others)
row_5.pack(expand=True, fill=BOTH)



# Doing the actual calculations
def calculation(num1, num2, operator):
    num1 = float(num1)
    num2 = float(num2)
    if operator == "+":
        if (num1 + num2) % 1 != 0:
            return float(num1 + num2)
        else:
            return int(num1+num2)
    elif operator == "-":
        if (num1 - num2) % 1 != 0:
            return float(num1 - num2)
        else:
            return int(num1-num2)
    elif operator == "x":
        if (num1 * num2) % 1 != 0:
            return float(num1 * num2)
        else:
            return int(num1*num2)
    elif operator == "/":
        if (num1 / num2) % 1 != 0:
            return float(num1 / num2)
        else:
            return int(num1/num2)
    elif operator == "=":
        pass
    else:
        return "I don't know what that is"
    
    
# Figuring out if what is in the entry field is a number or not
def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Function for inputting numbers into the text field. Deleting what is in the text field if is not a number.
def pressnum(num):
    global num1
    global num2
    global total
    value = Entry.get(E1)
    if value == str(total):
        num1 = 0
        num2 = 0
        total = 0
        Entry.delete(E1, 0, END)
        Entry.insert(E1, END, num)
    elif "." in value and num == ".":
        pass
    elif value == ".":
        Entry.insert(E1, END, num)
    elif is_number(value) is True:
        Entry.insert(E1, END, num)
    else:
        Entry.delete(E1, 0, END)
        Entry.insert(E1, END, num)


num1 = 0
num2 = 0
operation = ""
total = 0
# Function for the operators. Deleting what is in the entry field and entering the desired operator
def equals(operator):
    global num1
    global num2
    global total
    global operation
    value = Entry.get(E1)
    if is_number(value) is True:
        #print("your number is ", value)
        #print("your operator is ", operator)
        if operator == "=":
            if num1 == 0:
                pass
            elif num2 == 0:
                num2 = value
                total = calculation(num1, num2, operation)
                #print(num1, num2, operation, total)
                if total == "I don't know what that is":
                    Entry.delete(E1, 0, END)
                    Entry.insert(E1, END, "error")
                else:
                    Entry.delete(E1, 0, END)
                    Entry.insert(E1, END, total)
                    num1 = total
                    #print(num1, num2, total, operation)
            else:
                if float(value) == total:
                    total = calculation(num1, num2, operation)
                    #print(total)
                else:
                    num2 = value
                    total = calculation(num1, num2, operation)
                    #print("This is your total")
                Entry.delete(E1, 0, END)
                Entry.insert(E1, END, total)
                num1 = total
                #print(num1, num2, total)
        # Any other operator but =
        else:
            if num1 == 0:
                num1 = value
            elif num2 == 0:
                num2 = value
                total = calculation(num1, num2, operation)
                num1 = total
                num2 = 0
            else:
                total = calculation(num1, num2, operation)
                num2 = 0
            Entry.delete(E1, 0, END)
            Entry.insert(E1, END, operator)
            #print(num1, num2, total)
            operation = operator
    elif value == "":
        pass
    else:
        Entry.delete(E1, 0, END)
        if operator == "=":
            Entry.insert(E1, END, "Can't do that")
        else:
            Entry.insert(E1, END, operator)
# Clearing the entry field
def clear():
    global num1
    global num2
    global total
    global operation
    Entry.delete(E1, 0, END)
    num1 = 0
    num2 = 0
    total = 0
    operation = ""


# Buttons for the calculator

B1 = Button(row1, text="1", command=lambda: pressnum(1))
B1.pack(side = LEFT, expand=True, fill=BOTH)
B2 = Button(row1, text="2", command=lambda: pressnum(2))
B2.pack(side = LEFT, expand=True, fill=BOTH)
B3 = Button(row1, text="3", command=lambda: pressnum(3))
B3.pack(side = LEFT, expand=True, fill=BOTH)
B4 = Button(row2, text="4", command=lambda: pressnum(4))
B4.pack(side = LEFT, expand=True, fill=BOTH)
B5 = Button(row2, text="5", command=lambda: pressnum(5))
B5.pack(side = LEFT, expand=True, fill=BOTH)
B6 = Button(row2, text="6", command=lambda: pressnum(6))
B6.pack(side = LEFT, expand=True, fill=BOTH)
B7 = Button(row3, text="7", command=lambda: pressnum(7))
B7.pack(side = LEFT, expand=True, fill=BOTH)
B8 = Button(row3, text="8", command=lambda: pressnum(8))
B8.pack(side = LEFT, expand=True, fill=BOTH)
B9 = Button(row3, text="9", command=lambda: pressnum(9))
B9.pack(side = LEFT, expand=True, fill=BOTH)
B0 = Button(row4, text="0", command=lambda: pressnum(0))
B0.pack(side = LEFT, expand=True, fill=BOTH)
B00 = Button(row4, text=".", command=lambda: pressnum("."))
B00.pack(side = LEFT, expand=True, fill=BOTH)

Bmulti = Button(row_1, text="x", command=lambda: equals("x"))
Bmulti.pack(side=BOTTOM, expand=True, fill=BOTH)
Bdivide = Button(row_2, text="/", command=lambda: equals("/"))
Bdivide.pack(side=BOTTOM, expand=True, fill=BOTH)
Badd = Button(row_3, text="+", command=lambda: equals("+"))
Badd.pack(side=BOTTOM, expand=True, fill=BOTH)
Bsub = Button(row_4, text="-", command=lambda: equals("-"))
Bsub.pack(side=BOTTOM, expand=True, fill=BOTH)
Bequal = Button(row_5, text="=", command=lambda: equals("="))
Bequal.pack(side=RIGHT, expand=True, fill=BOTH)

Bclear = Button(row_5, text="Clear", command=clear)
Bclear.pack(side=LEFT, expand=True, fill=BOTH)

# Entry field
E1 = Entry(field, bd=5)
E1.pack(side=BOTTOM, expand=True, fill=BOTH)

#a = Label(field, text="Calculator")
#a.pack(side=TOP, expand=True, fill=X)

root.mainloop()
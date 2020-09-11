from tkinter import *
import tkinter.ttk as ttk
import math

root = Tk()
root.title("Standard Calculator")
# root.configure(bg="black")
root.iconbitmap("images/calculator.ico")

e = ttk.Entry(root, width=60)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

# assining functions


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))


def button_add():
    f_number = e.get()
    global f_num
    global operation
    operation = "addition"
    f_num = int(f_number)
    e.delete(0, END)


def button_subtract():
    f_number = e.get()
    global f_num
    global operation
    operation = "subtraction"
    f_num = int(f_number)
    e.delete(0, END)


def button_multiply():
    f_number = e.get()
    global f_num
    global operation
    operation = "multiplication"
    f_num = int(f_number)
    e.delete(0, END)


def button_divide():
    f_number = e.get()
    global f_num
    global operation
    operation = "division"
    f_num = int(f_number)
    e.delete(0, END)


def button_square():
    f_number = e.get()
    global f_num
    f_num = int(f_number)
   # global operation
   # operation = "square"
    e.delete(0, END)
    e.insert(0, f_num*f_num)


def button_sqrt():
    global f_num
    f_num = int(e.get())
   # global operation
   # operation = "sqrt"
    e.delete(0, END)
    e.insert(0, math.sqrt(f_num))


def button_percentile():
    f_number = e.get()
    global f_num
    f_num = int(f_number)
    global operation
    operation = "percentile"
    e.delete(0, END)


def button_reciprocal():
    global f_num
    f_num = int(e.get())
    #global operation
    # operation="reciprocal"
    e.delete(0, END)
    e.insert(0, 1/f_num)


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if operation == "addition":
        e.insert(0, f_num+int(second_number))

    if operation == "subtraction":
        e.insert(0, f_num-int(second_number))

    if operation == "multiplication":
        e.insert(0, f_num * int(second_number))

    if operation == "division":
        e.insert(0, f_num/int(second_number))

    '''if operation == "square":
        e.insert(0, f_num*f_num)

    if operation == "sqrt":
        e.insert(0, math.sqrt(f_num))'''

    if operation == "percentile":
        e.insert(0, f_num % int(second_number))

    '''if operation == "reciprocal":
        e.insert(0, 1/f_num)'''


def button_clear():
    e.delete(0, END)

# defining buttons


button_1 = ttk.Button(root, text="1",
                      command=lambda: button_click(1))
button_2 = ttk.Button(root, text="2",
                      command=lambda: button_click(2))
button_3 = ttk.Button(root, text="3",
                      command=lambda: button_click(3))
button_4 = ttk.Button(root, text="4",
                      command=lambda: button_click(4))
button_5 = ttk.Button(root, text="5",
                      command=lambda: button_click(5))
button_6 = ttk.Button(root, text="6",
                      command=lambda: button_click(6))
button_7 = ttk.Button(root, text="7",
                      command=lambda: button_click(7))
button_8 = ttk.Button(root, text="8",
                      command=lambda: button_click(8))
button_9 = ttk.Button(root, text="9",
                      command=lambda: button_click(9))
button_0 = ttk.Button(root, text="0",
                      command=lambda: button_click(0))

button_add = ttk.Button(root, text="+",
                        command=button_add)
button_subtract = ttk.Button(root, text="-",
                             command=button_subtract)
button_multiply = ttk.Button(root, text="*",
                             command=button_multiply)
button_divide = ttk.Button(root, text="/",
                           command=button_divide)

button_equal = ttk.Button(root, text="=",
                          command=button_equal)
button_clear = ttk.Button(root, text="C",
                          command=button_clear)

button_square = ttk.Button(root, text="square", command=button_square)

button_sqrt = ttk.Button(root, text="sqrt",
                         command=button_sqrt)

button_percentile = ttk.Button(root, text="%",
                               command=button_percentile)

button_reciprocal = ttk.Button(root, text="1/x",
                               command=button_reciprocal)

button_square.grid(column=0, row=5, ipadx=10, ipady=20)
button_sqrt.grid(column=1, row=5, ipadx=10, ipady=20)
button_percentile.grid(row=5, column=3, ipadx=10, ipady=20)
button_reciprocal.grid(row=5, column=2, ipadx=10, ipady=20)

button_1.grid(row=3, column=0, ipadx=10, ipady=20)
button_2.grid(row=3, column=1, ipadx=10, ipady=20)
button_3.grid(row=3, column=2, ipadx=10, ipady=20)

button_4.grid(row=2, column=0, ipadx=10, ipady=20)
button_5.grid(row=2, column=1, ipadx=10, ipady=20)
button_6.grid(row=2, column=2, ipadx=10, ipady=20)

button_7.grid(row=1, column=0, ipadx=10, ipady=20)
button_8.grid(row=1, column=1, ipadx=10, ipady=20)
button_9.grid(row=1, column=2, ipadx=10, ipady=20)

button_0.grid(row=4, column=1, ipadx=10, ipady=20)

button_add.grid(row=3, column=3, ipadx=10, ipady=20)
button_subtract.grid(row=2, column=3, ipadx=10, ipady=20)
button_multiply.grid(row=1, column=3, ipadx=10, ipady=20)
button_divide.grid(row=4, column=3, ipadx=10, ipady=20)

button_equal.grid(row=4, column=2, ipadx=10, ipady=20)
button_clear.grid(row=4, column=0, ipadx=10, ipady=20)


root.mainloop()

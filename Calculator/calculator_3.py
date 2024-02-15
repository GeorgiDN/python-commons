from tkinter import *

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + number)

def button_clear():
    e.delete(0, END)

def perform_operation(operator):
    first_number = e.get()
    global f_num
    global math
    math = operator
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    global f_num
    second_number = e.get()
    e.delete(0, END)

    result = 0  # Initialize result

    if math == "addition":
        result = f_num + int(second_number)
    elif math == "subtraction":
        result = f_num - int(second_number)
    elif math == "multiplication":
        result = f_num * int(second_number)
    elif math == "division":
        result = f_num / int(second_number)
    elif math == "exponentiation":
        result = f_num ** int(second_number)

    e.insert(0, result)

    # Store the calculation in a text file
    with open('calculations.txt', 'a') as file:
        file.write(f"{f_num} {math} {second_number} = {result}\n")

root = Tk()
root.title("My calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'Clear', '=', '+',
    '**'
]

row_val = 1
col_val = 0
math = None  # Initialize math
f_num = None

for button in buttons:
    if button == 'Clear':
        btn = Button(root, text=button, padx=40, pady=20, command=button_clear)
    elif button == '=':
        btn = Button(root, text=button, padx=40, pady=20, command=button_equal)
    else:
        btn = Button(root, text=button, padx=40, pady=20, command=lambda b=button: button_click(b))

    btn.grid(row=row_val, column=col_val, padx=2, pady=2)
    col_val += 1

    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()

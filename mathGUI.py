from tkinter import *
from sympy import *
from pyperclip import *
from webbrowser import *
import matplotlib.pyplot as plot

import doubleIntegralCalc

x,y,z = symbols('x y z')

win = Tk()
win.title("Math Helper")
win.geometry('800x500')

greet = Frame(win)
integration = Frame(win)

menubar = Menu(win)
win.config(menu=menubar)

# Configuring Integration Frame
integration.rowconfigure([0, 1, 2, 3, 4], minsize=100, weight=1)
integration.columnconfigure([0, 1, 2, 3, 4], minsize=100, weight=1)

# Holds what we are doing
status = ""

xlow = Entry()
xhigh = Entry()
inlow = Entry()
inhigh = Entry()
midlow = Entry()
midhigh = Entry()
outlow = Entry()
outhigh = Entry()


def clear():
    for widget in integration.grid_slaves():
        if (((int(widget.grid_info()["row"] >= 1) and int(widget.grid_info()["row"] <= 3) and int(
                widget.grid_info()["column"] >= 0) and int(widget.grid_info()["column"] <= 2))
             or (widget.grid_info()["row"] == 2 and widget.grid_info()["column"] == 3)) or
                (widget.grid_info()["row"] == 2 and widget.grid_info()["column"] == 4)):
            widget.grid_forget()


# Holds the function we are integrating
function = Entry(master=integration)


def setupsingle():
    global status, xlow, xhigh
    status = "single"
    clear()
    xlow = Entry(master=integration)
    xhigh = Entry(master=integration)
    xhigh.grid(row=1, column=0)
    intSign = Label(master=integration, text="∫")
    intSign.config(font=("Arial", 50))
    intSign.grid(row=2, column=0)
    xlow.grid(row=3, column=0)
    function.grid(row=2, column=1)
    Label(master=integration, text="dx").grid(row=2, column=2)


def setupdouble():
    global status, outlow, outhigh, midlow, midhigh
    status = "double"
    clear()
    outlow = Entry(master=integration)
    outhigh = Entry(master=integration)
    midlow = Entry(master=integration)
    midhigh = Entry(master=integration)
    outhigh.grid(row=1, column=0)
    outlow.grid(row=3, column=0)
    midhigh.grid(row=1, column=1)
    midlow.grid(row=3, column=1)
    intSign = Label(master=integration, text="∫")
    intSign.config(font=("Arial", 50))
    intSignTwo = Label(master=integration, text="∫")
    intSignTwo.config(font=("Arial", 50))
    intSign.grid(row=2, column=0)
    intSignTwo.grid(row=2, column=1)
    function.grid(row=2, column=2)
    options = [
        "dydx",
        "dxdy",
        "rdrdθ"
    ]
    variable = StringVar(master=integration)
    variable.set(options[0])

    order = OptionMenu(integration, variable, *options)
    order.grid(row=2, column=3)


def setuptriple():
    global status
    status = "triple"
    clear()
    global outlow, outhigh, midlow, midhigh, inlow, inhigh
    outlow = Entry(master=integration)
    outhigh = Entry(master=integration)
    midlow = Entry(master=integration)
    midhigh = Entry(master=integration)
    inlow = Entry(master=integration)
    inhigh = Entry(master=integration)
    outhigh.grid(row=1, column=0)
    outlow.grid(row=3, column=0)
    midhigh.grid(row=1, column=1)
    midlow.grid(row=3, column=1)
    inhigh.grid(row=1, column=2)
    inlow.grid(row=3, column=2)
    intSign = Label(master=integration, text="∫")
    intSign.config(font=("Arial", 50))
    intSignTwo = Label(master=integration, text="∫")
    intSignTwo.config(font=("Arial", 50))
    intSignThree = Label(master=integration, text="∫")
    intSignThree.config(font=("Arial", 50))
    intSign.grid(row=2, column=0)
    intSignTwo.grid(row=2, column=1)
    intSignThree.grid(row=2, column=2)
    function.grid(row=2, column=3)
    options = [
        "dxdydz",
        "dxdzdy",
        "dydxdz",
        "dydzdx",
        "dzdxdy",
        "dzdydx"
    ]
    variable = StringVar(master=integration)
    variable.set(options[0])

    order = OptionMenu(integration, variable, *options)
    order.grid(row=2, column=4)


single = Button(master=integration, text="Single Integral", command=setupsingle)
double = Button(master=integration, text="Double Integral", command=setupdouble)
triple = Button(master=integration, text="Triple Integral", command=setuptriple)
single.grid(row=0, column=1)
double.grid(row=0, column=2)
triple.grid(row=0, column=3)


def evaluate():
    if status == "single":
        integral = integrate(sympify(function.get()), x)
        temp = simplify(integral.subs(x, sympify(xhigh.get())) - integral.subs(x, sympify(xlow.get())))
        copy(latex(temp))
        open_new("https://www.quicklatex.com/")
    if status == "double":
        print("from" + str(outlow.get()) + "to" + str(outhigh.get()))


calc = Button(master=integration, text="Calculate", command=evaluate)
calc.grid(row=4, column=2)


def change_to_integration():
    integration.pack(fill='both', expand=1)
    greet.pack_forget()


def change_to_greet():
    greet.pack(fill='both', expand=1)
    integration.pack_forget()


operation_menu = Menu(
    menubar,
    tearoff=0
)

operation_menu.add_command(
    label="Integration",
    command=change_to_integration
)
operation_menu.add_command(
    label="Vector Calculus"
)

operation_menu.add_separator()

menubar.add_cascade(
    label="Operations",
    menu=operation_menu,
    underline=0
)

win.mainloop()

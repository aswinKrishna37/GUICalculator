import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("GUICalculator")
root.config(bg="black")


e = tk.Entry(root, width=20, font=('Arial', 18), borderwidth=1, relief='flat')
e.grid(row=0, column=0, columnspan=4, rowspan=2, padx=10, pady=10, ipady=10, ipadx=10)


def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def buttonf_clear():
    e.delete(0,END)

def buttonf_add():
    global num1
    num1 = int(e.get())
    e.delete(0,END)
    global op
    op = "+"
    
def buttonf_sub():
    global num1
    num1 = int(e.get())
    e.delete(0,END)
    global op
    op = "-"
    

def buttonf_mul():
    global num1
    num1 = int(e.get())
    e.delete(0,END)
    global op
    op = "*"
    

def buttonf_div():
    global num1
    num1 = int(e.get())
    e.delete(0,END)
    global op
    op = "/"
    
    



def buttonf_eq():
    global num2
    num2 = int(e.get())
    e.delete(0,END)
    global op
    match op:
        case "+":
            e.insert(0,str(num1+num2))
        case "-":
            e.insert(0,str(num1-num2))
        case "*":
            e.insert(0,str(num1*num2))
        case "/":
            e.insert(0,str(num1/num2))
            
            
    





button_1 = Button(root, text="1", padx=30, pady=10, bg="black", fg="white", command = lambda: button_click(1))
button_2 = Button(root, text="2", padx=30, pady=10, bg="black", fg="white", command = lambda: button_click(2))
button_3 = Button(root, text="3", padx=30, pady=10, bg="black", fg="white", command = lambda: button_click(3))
button_4 = Button(root, text="4", padx=30, pady=10, bg="black", fg="white", command = lambda: button_click(4))
button_5 = Button(root, text="5", padx=30, pady=10, bg="black", fg="white", command = lambda: button_click(5))
button_6 = Button(root, text="6", padx=30, pady=10, bg="black", fg="white", command = lambda: button_click(6))
button_7 = Button(root, text="7", padx=30, pady=10, bg="black", fg="white", command = lambda: button_click(7))
button_8 = Button(root, text="8", padx=30, pady=10, bg="black", fg="white", command = lambda: button_click(8))
button_9 = Button(root, text="9", padx=30, pady=10, bg="black", fg="white", command = lambda: button_click(9))
button_0 = Button(root, text="0", padx=30, pady=10, bg="black", fg="white", command = lambda: button_click(0))

button_add = Button(root, text="+", padx=30, pady=10, bg="black", fg="white", command = buttonf_add)
button_sub = Button(root, text="-", padx=31, pady=10, bg="black", fg="white", command = buttonf_sub)
button_mul = Button(root, text="x", padx=31, pady=10, bg="black", fg="white", command = buttonf_mul)
button_div = Button(root, text="/", padx=32, pady=10, bg="black", fg="white", command = buttonf_div)

button_eq = Button(root, text="=", padx=30, pady=10, bg="black", fg="white", command = buttonf_eq)
button_clear = Button(root, text="AC", padx=25, pady=10, bg="black", fg="white", command = buttonf_clear)



button_1.grid(row=2, column=0)
button_2.grid(row=2, column=1)
button_3.grid(row=2, column=2)


button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)

button_0.grid(row=5, column=0)

button_add.grid(row=2, column=3)
button_sub.grid(row=3, column=3)
button_mul.grid(row=4, column=3)
button_div.grid(row=5, column=3)

button_eq.grid(row=5, column=1)
button_clear.grid(row=5, column=2)

root.mainloop()

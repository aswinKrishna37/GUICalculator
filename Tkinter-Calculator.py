import tkinter as tk
from tkinter import * 

root = tk.Tk()

label = Label(root,text="Output")
label.grid(row=1,column=1,columnspan=4,rowspan=2)

root.rowconfigure(1, minsize=40)
root.rowconfigure(2, minsize=40)


button_1 = Button(root,text="1",padx=20,pady=10)
button_2 = Button(root,text="2",padx=20,pady=10)
button_3 = Button(root,text="3",padx=20,pady=10)
button_4 = Button(root,text="4",padx=20,pady=10)
button_5 = Button(root,text="5",padx=20,pady=10)
button_6 = Button(root,text="6",padx=20,pady=10)
button_7 = Button(root,text="7",padx=20,pady=10)
button_8 = Button(root,text="8",padx=20,pady=10)
button_9 = Button(root,text="9",padx=20,pady=10)
button_0 = Button(root,text="0",padx=20,pady=10)

button_add = Button(root,text="+",padx=20,pady=10)
button_sub = Button(root,text="-",padx=20,pady=10)
button_mul = Button(root,text="x",padx=20,pady=10)
button_div = Button(root,text="/",padx=20,pady=10)

button_eq = Button(root,text="=",padx=46,pady=10)


button_1.grid(row=3,column=1)
button_2.grid(row=3,column=2)
button_3.grid(row=3,column=3)
button_4.grid(row=4,column=1)
button_5.grid(row=4,column=2)
button_6.grid(row=4,column=3)
button_7.grid(row=5,column=1)
button_8.grid(row=5,column=2)
button_9.grid(row=5,column=3)
button_0.grid(row=6,column=1)
button_add.grid(row=3,column=4)
button_sub.grid(row=4,column=4)
button_mul.grid(row=5,column=4)
button_div.grid(row=6,column=4)
button_eq.grid(row=6,column=2,columnspan=2)

root.mainloop()

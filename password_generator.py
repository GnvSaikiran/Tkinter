from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import random

root=Tk()
root.title('Password Generator')
root.geometry("300x100")

def generate():
    password=''
    weak = 'abcdefghijklmnopqrstuvwxyz'
    moderate = weak+'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    strong = moderate+'0123456789!@#$&*^%'
    number = int(entry2.get())
    if var.get() == 'weak':
        for i in range (number):
            password=password+random.choice(weak)
    elif var.get() == "moderate":
        for i in range (number):
            password=password+random.choice(moderate)
    elif var.get() == "strong":
        for i in range (number):
            password=password+random.choice(strong)

    messagebox.showinfo('Password',password)


label1=Label(root,text='Password Stength:',padx=8,pady=8).grid(row=0,column=0)
label2=Label(root,text='Length of password:',padx=8,pady=8).grid(row=1,column=0,)

#entry1=Entry(root)
#entry1.grid(row=0,column=1,padx=8,pady=8)

entry2=ttk.Entry(root)
entry2.grid(row=1,column=1,padx=8,pady=8)

options=[
            'select',
            'weak',
            'moderate',
            'strong'
        ]
var=StringVar()
#var.set(options[2])

menu=ttk.OptionMenu(root,var,*options).grid(row=0,column=1)

button=ttk.Button(root,text='Generate',command=generate).grid(row=2,column=1,columnspan=2)
mainloop()

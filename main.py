from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Finansee | Your Personal Finance Manager")
root.geometry('1800x900')
root.configure(background = 'light blue')

lbl = Label(root, text = "Welcome to Finansee")
lbl.config(font =("Courier", 44))
lbl.pack(expand=True, fill='both')
lbl.grid(column=700, row=400)


# function to display text when
# button is clicked
def clicked():
    lbl.pack(text = "I just got clicked")
    lbl.pack(expand=True, fill='both')
# button widget with red color text
# inside
btn = Button(root, text = "Click me" ,
             fg = "red", command=clicked)
# set Button grid
btn.grid(column=700, row=500)

# Execute Tkinter
root.mainloop()
from tkinter import *

root = Tk()
root.title("Welcome to GeekForGeeks")
root.geometry('1800x900')

lbl = Label(root, text = "Are you a Geek?")
lbl.grid()

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
from tkinter import *
from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox,Entry,Label,Button

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("FinanSee - Main")
        self.root.iconbitmap(default='images\pngwing.com.ico')## Image ico
        self.label = Label(root, text="FinanSee !", width=20, height=2, font=("Arial", 16),bg="#00FF7F", fg="black").place(x=200, y=10)
        self.button1 = Button(root, text="Inciar", command=self.on_button_click, width=20, height=2, bg="#4CAF50", fg="white")
        self.button1.pack(side=TOP, pady=50)

        self.geometry()


    def on_button_click(self):
        self.label.config(text="Button Clicked!")

    def geometry(self):
        self.root.geometry("800x600")
        self.root.wm_minsize(width=800, height=600)
        self.root.configure(background='#00FF7F')

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
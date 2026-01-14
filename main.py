from tkinter import *
from tkinter import ttk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("FinanSee - Main")
        root.geometry("500x500+10+50") 
        
        self.label = Label(root, text="FinanSee !")
        self.label.pack(pady=10)
        self.label.config(font=("Arial", 24))

        self.button = Button(root, text="Inciar", command=self.on_button_click)
        self.button.pack(pady=10)

        self.tela()

    def on_button_click(self):
        self.label.config(text="Button Clicked!")

    def tela(self):
        self.root.configure(background='#00FF7F')

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
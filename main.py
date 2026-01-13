from tkinter import *
from tkinter import ttk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Tkinter App")

        self.label = Label(root, text="Hello, Tkinter!")
        self.label.pack(pady=10)

        self.button = Button(root, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)

    def on_button_click(self):
        self.label.config(text="Button Clicked!")

    def tela(self):
        self.root.configure(background='lightblue')

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
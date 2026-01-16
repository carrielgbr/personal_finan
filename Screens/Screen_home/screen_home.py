from tkinter import *
from tkinter import ttk

class screen_home:
    def __init__(self, root):
        self.root = root

    def geometry(self):
        self.root.geometry("800x600")
        self.root.wm_minsize(width=800, height=600)
        self.root.configure(background='#00FF7F')

    
    
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter
from PIL import Image
from PIL import ImageTk
import tkinter.messagebox

class Smarties:
    def __init__(self, master,color):
        self.master = master
        self.color = color
        self.image = Image.open(color+".jpeg")
        self.photo = ImageTk.PhotoImage(self.image)
        
        master.title("A simple GUI")

        self.label = tkinter.Label(master, text="This is our first GUI!")
        self.label.pack()

        self.button = tkinter.Button(master,image=self.photo, command = self.print_color)
        self.button.pack()
        
        self.greet_button = tkinter.Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = tkinter.Button(master, text="Close", command=self.greet)
        self.close_button.pack()

    def print_color(self):
        tkinter.Label(self.master, text = self.color +"!").pack()
    def greet(self):
        print("Greetings!")

root = tkinter.Tk()
#root.geometry('350x600')
my_gui_red = Smarties(root,'red')
#my_gui_green = Smarties(root,'green')

root.mainloop()

"""

"""




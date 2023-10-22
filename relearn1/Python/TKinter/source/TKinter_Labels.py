import tkinter as tk
from tkinter import ttk

root = tk.Tk()

#assigns text to widget at creation using keyword arguments
ttk.Label(root, text='Hi, there').pack()

#creates and attaches label to root window
label = ttk.Label(root)
#assignes text to label using a dictionary index after widget creation
label["text"]= "hello there"
#packs label for display
label.pack()

#assigns text to label using config() method with keyword attributes
label2 = ttk.Label(root)
label2.config(text="General Kenobi")
label2.pack()

root.mainloop()
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def button_clicked():
    label1.config(text="my button has been clicked")
    label1.pack()

def select(option):
    txt="you have chosen "+ option
    label2.config(text=txt) 
    
label1=ttk.Label(text="")
label2=ttk.Label(text="Choose your weapon")

label1.pack()
label2.pack()

btnClick= ttk.Button(root, text="click me", command =button_clicked)
btnClick.pack()

btnRock= ttk.Button(root, text="rock", command=lambda: select("rock"))
btnRock.pack()

btnPaper= ttk.Button(root, text="Paper", command=lambda: select("Paper"))
btnPaper.pack()

btnScizors= ttk.Button(root, text="Scizors", command=lambda: select("Scizors"))
btnScizors.pack()

root.mainloop()
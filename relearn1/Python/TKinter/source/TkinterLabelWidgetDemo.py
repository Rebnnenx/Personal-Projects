import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry("400x300+100+100")
root.resizable(False,False)
root.title("Label Widget Demo")

#shows a label
lbl_label1 = ttk.Label(root,
              text="This is a label in Helvetica font", #add the text
              font=("Helvetica", 14))    #customizes font and size

lbl_label1.pack(ipadx=10, ipady=10)


photo = tk.PhotoImage(file="./Python/Tkinter/assets/images/logo.png")

lbl_image = ttk.Label(
    root,
    image=photo,
    text="Python is fun",
    padding=5,
    compound="top"
)
lbl_image.pack()

root.mainloop()
import tkinter as tk
from tkinter import ttk


root=tk.Tk()
root.title("Login")
root.geometry("350x220")

#initialize dictionary for fields
fields = {}


#create label and entry widgets for username
fields["lbl_username"]= ttk.Label(text="Username")
fields["entry_username"]=ttk.Entry()


#create label and entry widgets for passwords
fields['lbl_password'] = ttk.Label(text='Password:')
fields['entry_password'] = ttk.Entry(show="*")

#iterates through the fields in dictionary and packs them
for field in fields.values():
    field.pack(anchor=tk.W, padx=10, pady=5)

#add login button
ttk.Button(text="Login").pack(anchor=tk.W, padx=10,pady=5)

root.mainloop()
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Sign In')
root.iconbitmap("./Python/TKinter/assets/images/logo.ico")

#store email address and password
email = tk.StringVar()
password =tk.StringVar()

def login_clicked():
    """callback when the login button is clicked
    """
    msg=f"you endtered email: {email.get()} and password:{password.get()}"
    showinfo(
        title="Information",
        message=msg
    )

#sign in frame
signin=ttk.Frame(root)
signin.pack(padx=10,pady=10,fill="x", expand=True)

#email
lbl_email=ttk.Label(signin, text="Email Address")
lbl_email.pack(fill="x", expand=True)

entry_email = ttk.Entry(signin, textvariable=email, font="unown")
entry_email.pack(fill="x", expand=True)
entry_email.focus()

#password
lbl_password= ttk.Label(signin, text="Password")
lbl_password.pack(fill="x",expand=True)

#hides password with the 'show' option 
entry_password=ttk.Entry(signin, textvariable=password,font="unown", show="X")
entry_password.pack(fill="x", expand=True)

#login button
btn_login= ttk.Button(signin, text="Login", command=login_clicked)
btn_login.pack(fill="x",expand=True,pady=10)


root.mainloop()
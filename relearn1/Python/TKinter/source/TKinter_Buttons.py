import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def download_clicked():
    btn_exit.state(["!disabled"])
    showinfo(
        title="Information",
        message="Download started!"
    )

# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Image Button Demo')
root.iconbitmap("./Python/TKinter/assets/images/logo.ico")

#download button
img_downloadIcon=tk.PhotoImage(file="./Python/Tkinter/assets/images/download.png")
btn_download=ttk.Button(
    root,
    image=img_downloadIcon,
    text="Download",
    compound=tk.LEFT,
    command=download_clicked
)

btn_download.pack(
    ipadx=5,
    ipady=5,
    expand=True
)


# exit button
btn_exit = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)
btn_exit.state(["disabled"])
btn_exit.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()
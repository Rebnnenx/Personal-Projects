import tkinter as tk
from tkinter import *
import time
from random import randrange
import ctypes


def clickedHello():
    msg.config(text= "Hello World!")
    
    
def clickedGoodbye():
    msg.config(text= "Goodbye World!")
    
    
root = tk.Tk()
root.title("Hello World")
root.geometry("800x800")
root["bg"]= "darkgreen"

frameGreeting = tk.Frame(root,width="300", height="300",relief="raised",bd = 2, bg="darkblue")

#displays top message
greet = Label(frameGreeting,text = "Greetings!",bg="light green", font=("bold",18),fg="white", relief="raised" )
greet.place(anchor ="n", relx=0.5, rely=0.1)

#displays selected message
msg= Label(frameGreeting,text="",bg="light green", font=("bold",18),fg="white", relief="raised" )
msg.place(anchor ="center", relx=0.5, rely=0.5)

#adds hello button
btnHello = Button(frameGreeting, text="Hello", command=clickedHello, width ="6")
btnHello.place(relx=0.25, rely =0.75, anchor= CENTER)

#adds goodbye button
btnGoodbye = Button(frameGreeting, text="Goodbye", command=clickedGoodbye, width ="6")
btnGoodbye.place(relx=0.75, rely =0.75, anchor= CENTER)

frameGreeting.pack(fill ="both",pady=("5","5"), padx=("5","5"))





root.mainloop()


#print ("hello world")
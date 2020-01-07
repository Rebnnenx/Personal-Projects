import tkinter as tk
from tkinter import *
from random import randrange
import time
from PIL import Image, ImageTk
import ctypes

def win():
#   ctypes.windll.user32.MessageBoxW(0, "Winner", "Results", 1)
    result.configure(text="WINNER!!!")

def lose():
#    ctypes.windll.user32.MessageBoxW(0, "Lose", "Results", 1)
    result.configure(text="You Lose!!")
def tie(): 
#    ctypes.windll.user32.MessageBoxW(0, "Tie", "Results", 1)
    result.configure(text="Tie!!")

def clickedRock():
    imgPlayer.configure(image=rock)
    generateWinner(1)

def clickedPaper():
    imgPlayer.configure(image=paper)
    generateWinner(2)

def clickedScissors():
    imgPlayer.configure(image=scissors)
    generateWinner(3)

def generateWinner(player):
    computer = randrange(3)+1 #generates computer result

    
    if player == 1:#player chose rock
        if computer == 1:#rock
            imgComputer.configure(image=rock)
            tie()

        elif computer == 2:#paper
            imgComputer.configure(image=paper)
            lose()

        elif computer == 3:#scissors
            imgComputer.configure(image=scissors)
            win()

    elif player == 2: #player chose paper
        if computer == 1:#rock
            imgComputer.configure(image=rock)
            win()
            

        elif computer == 2:#paper
            imgComputer.configure(image=paper)
            tie()

        elif computer == 3:#scissors
            imgComputer.configure(image=scissors)
            lose()

    elif player == 3: #player chose scissors
        if computer == 1:#rock
            imgComputer.configure(image=rock)
            lose()
            

        elif computer == 2:#paper
            imgComputer.configure(image=paper)
            win()

        elif computer == 3:#scissors
            imgComputer.configure(image=scissors)
            tie()

root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("400x300+200+100")
root["bg"] = "black"

vs =ImageTk.PhotoImage(Image.open("vs.png").resize((50, 50), Image.ANTIALIAS))
rock = ImageTk.PhotoImage(Image.open("rock.png").resize((125, 125), Image.ANTIALIAS))
paper = ImageTk.PhotoImage(Image.open("paper.png").resize((125, 125), Image.ANTIALIAS))
scissors = ImageTk.PhotoImage(Image.open("scissors.png").resize((125, 125), Image.ANTIALIAS))
    
options = tk.Frame(root,width="300", height="75",relief="raised",bd = 2, bg="darkred")

btnRock = Button(options, text="Rock", command=clickedRock, width ="6")
btnRock.place(relx=0.25, rely =0.75, anchor= CENTER)

btnPaper = Button(options, text="Paper", command=clickedPaper, width ="6")
btnPaper.place(relx=0.5, rely =0.75, anchor= CENTER)

btnScissors = Button(options, text="Scissors", command=clickedScissors, width ="6")
btnScissors.place(relx=0.75, rely =0.75, anchor= CENTER)

options.pack(pady=("5","5"), padx=("5","5"), fill ="x")

battle =tk.Frame(root, width="300", height ="300", relief = "sunken",bd=2, bg="maroon")
framePlayer =tk.Frame(battle, width ="150", height="150",relief ="sunken", bd =2,bg="maroon")
frameVS =tk.Frame(battle, width ="75", height="75",relief ="raised", bd =5,bg="maroon")
frameComputer =tk.Frame(battle, width ="150", height="150",relief ="sunken", bd =2,bg="maroon")

result= Label(battle, fg="white", font= ("bold", 18), bg="maroon")
result.place(anchor ="n", relx=0.5, rely =0.05)

imgPlayer=Label(framePlayer, bg="maroon")
imgPlayer.place(relx =0.5, rely=0.5, anchor =CENTER)
framePlayer.place(anchor = CENTER, relx= 0.2, rely =0.6)
    
imgVS=Label(frameVS,image=vs)
imgVS.place(relx =0.5, rely=0.5, anchor =CENTER)
frameVS.place(anchor = CENTER, relx=0.5, rely =0.6)
    
imgComputer=Label(frameComputer, bg="maroon")
imgComputer.place(relx =0.5, rely=0.5, anchor =CENTER)
frameComputer.place(anchor = CENTER, relx= 0.80, rely =0.6)

battle.pack(fill ="both", padx =(2,2), pady=(0,5))

lbl = Label(options,text = "Choose Your Weapon!",bg="maroon", font=("bold",18),fg="white", relief="raised" )
lbl.place(anchor ="n", relx=0.5, rely=0)


root.mainloop()


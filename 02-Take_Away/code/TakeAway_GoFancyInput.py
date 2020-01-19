import random
import tkinter as tk
from turtle import simpledialog
messagebox = simpledialog.messagebox


wh = t.Screen()

def getComputerMove(coins):
    move = random.randint(1,3)
    return move

def getHumanMove(coins):
    # human move -- need to check input bacuase human cheat !
    while True:
        #move = int(input("How many coins do you want to take (1, 2 or 3)? "))
        move = simpledialog.askinteger("Input", "How many coins do you want to take (1, 2 or 3)? ", parent=application_window)
        if move is None: continue
        if move>coins:
            messagebox.showwarning("Warning", "The pile only contains %s coins. Try again" % coins, parent=application_window)
        elif move not in [1,2,3]:
            pass
            messagebox.showwarning("Warning", "Expected a move of '1', '2' or '3'.")
        else:
            break
    return move

# initialise game

coins = random.randint(15, 21)
isComputerMove = False

# output instructions

simpledialog.messagebox.showinfo ("Welcome", "Game instructions go here ...\n\n")

# play the game

while coins>0:
    
    messagebox.showinfo("Information", "The pile contains %s coins." % coins)
    
    if isComputerMove:
        move = getComputerMove(coins)
        messagebox.showinfo("Information", "I'm taking %s coins" % move)
    else:
        move = getHumanMove(coins)
        messagebox.showinfo("Information", "You're taking %s coins" % move)
                
    coins = coins - move
    isComputerMove = not isComputerMove                                 

# output result of game

if isComputerMove:
    messagebox.showinfo("Information", "\nYou moved last. you win")
else:
    messagebox.showinfo("Information", "\nI moved last. you lose")
    


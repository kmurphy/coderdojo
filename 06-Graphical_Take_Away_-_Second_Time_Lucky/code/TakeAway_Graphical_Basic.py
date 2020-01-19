import turtle
import random

screen = turtle.Screen()
bob = turtle.Turtle()
bob.state = "start"
  
def startGame():
    bob.coins = random.randint(15,21)
    print ("Starting game with %s coins." % bob.coins)
    print ("Do you want to play first (Y/N) ?")
    bob.state = "start"
    update()
    
def player_No():
    if bob.state == "start":
        print("Great! I will play first ...")
        bob.state = "computer"
    
def player_Yes():
    if bob.state == "start":
        print("OK, you can play first ...")
        bob.state = "human"

def player_1():
    playerMove(1)
def player_2():
    playerMove(2)
def player_3():
    playerMove(3)

def playerMove(move):
    if bob.state != "human": return
    
    bob.coins = bob.coins - move
    print("You have taken %s coins" % move)
    bob.state = "computer"
    update()

def computerMove():
    move = random.randint(1, min(1,bob.coins))
    bob.coins = bob.coins - move
    print("I'm going to take %s coins" % move)
    bob.state = "human"
    update()

def update():
    
    print ("Game has %s coins left." % bob.coins)
    
    # check for game over
    if bob.coins<=0:
        if bob.state == "computer":
            print("OK, OK you won")
        else:
            print("Look I won again!")
        bob.state = "end"
        drawScreen()
        return
    
    if bob.state == "computer":
        computerMove()
    
    drawScreen()
  
def drawScreen():
    print("drawScreen not implemented yet")
    
screen.onkey(startGame, "s")
screen.onkey(player_1, "1")
screen.onkey(player_2, "2")
screen.onkey(player_3, "3")
screen.onkey(player_No, "n")
screen.onkey(player_Yes, "y")

startGame()
screen.listen()
screen.mainloop()


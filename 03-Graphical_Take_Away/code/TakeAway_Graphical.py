import turtle
import random

screen = turtle.Screen()
bob = turtle.Turtle()
bob.busy = False
bob.state = "start"


isComputerMove = False

def drawScreen():
    
    print (bob.state)
    
    bob.reset()
    bob.penup()
    bob.speed("fastest")
    # ttle 
    bob.goto(0,200)
    bob.write("Take Away", align="center", font=("Arial", 60))
    # coins
    bob.goto(0,0)
    bob.write(bob.coins, align="center", font=("Arial", 100))
    bob.goto(0,-40)
    bob.pendown()
    bob.width(5)
    bob.circle(100)
    # coins
    bob.penup()
    bob.goto(-300,-200)
    bob.write("\n".join(bob.messages[-5:]), align="left", font=("Arial", 20))
    
def startGame():
    bob.coins = random.randint(15,21)
    bob.messages = ["Starting game with %s coins." % bob.coins]
    bob.messages.append("Do you want to play first (Y/N) ?")

def playerMove1(): playerMove(1)
def playerMove2(): playerMove(2)
def playerMove3(): playerMove(3)
def playerMove(move):
    if bob.state != "player": return
    
    bob.coins = bob.coins - move
    bob.messages.append("You have taken %s coins" % move)
    bob.state = "computer"
    update()

def playerKeyN():
    if bob.state == "start":
        bob.state = "computer"
        bob.messages.append("OK I will play first ...")
        update()
        
def playerKeyY():
    if bob.state == "start":
        bob.state = "player"
        bob.messages.append("OK you can play first ...")
        update()

def computerMove():
    move = random.randint(1, min(1,bob.coins))
    bob.coins = bob.coins - move
    bob.messages.append("I'm going to take %s coins" % move)
    bob.state = "player"
    update()

def update():
    
    # check for game over
    if bob.coins==0:
        if bob.state == "computer":
            bob.messages.append("OK, OK you won")
        else:
            bob.messages.append("Look I won again!")
        bob.state = "end"
        drawScreen()
        return
    
    if bob.state == "computer":
        computerMove()
    
    drawScreen()
    
startGame()
drawScreen()

screen.onkey(startGame, "s")
screen.onkey(playerMove1, "1")
screen.onkey(playerMove2, "2")
screen.onkey(playerMove3, "3")
screen.onkey(playerKeyN, "n")
screen.onkey(playerKeyY, "y")

screen.listen()
screen.mainloop()
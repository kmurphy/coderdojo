import turtle
import random

screen = turtle.Screen()
bob = turtle.Turtle()
bob.state = "start"
  
def startGame():
    bob.coins = random.randint(15,21)
    bob.messages = ["Starting game with %s coins." % bob.coins]    
    bob.messages.append("Do you want to play first (Y/N) ?")
    bob.state = "start"
    update()
    
def player_No():
    if bob.state == "start":
        bob.messages.append("Great! I will play first ...")
        bob.state = "computer"
        update()
    
def player_Yes():
    if bob.state == "start":
        bob.messages.append("OK, you can play first ...")
        bob.state = "human"
        update()

def player_1():
    playerMove(1)
def player_2():
    playerMove(2)
def player_3():
    playerMove(3)

def playerMove(move):
    if bob.state != "human": return
    
    bob.coins = bob.coins - move
    bob.messages.append("You have taken %s coins" % move)
    bob.state = "computer"
    update()

def computerMove():
    move = random.randint(1, min(1,bob.coins))
    bob.coins = bob.coins - move
    bob.messages.append("I'm going to take %s coins" % move)
    bob.state = "human"
    update()

def update():
    
    bob.messages.append("Game has %s coins left." % bob.coins)
    
    # check for game over
    if bob.coins<=0:
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
    temp = "\n".join(bob.messages[-5:])
    bob.write(temp, align="left", font=("Arial", 20))
    
screen.onkey(startGame, "s")
screen.onkey(player_1, "1")
screen.onkey(player_2, "2")
screen.onkey(player_3, "3")
screen.onkey(player_No, "n")
screen.onkey(player_Yes, "y")

startGame()
screen.listen()
screen.mainloop()


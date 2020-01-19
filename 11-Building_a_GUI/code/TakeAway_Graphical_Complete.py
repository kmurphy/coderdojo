import turtle
import random, time, sys

screen = turtle.Screen()
bob = turtle.Turtle()
bob.state = "start"

bob.games = 0
bob.wins = 0
bob.level = "Beginner"

def jump(b,x,y):
    b.penup()
    b.goto(x,y)
    b.pendown()

# ants simulation

bob.runningAnts = False
bob.ants = []
for k in range(10):
    ant = turtle.Turtle()
    ant.hideturtle()
    ant.shape("turtle")
    r = random.uniform(0,1)
    ant.color(r,1-r, 1-r)
    bob.ants.append(ant)
    
def startAnts():
    screen.tracer(0)
    bob.nants = random.randint(2,10)
    for ant in bob.ants[:bob.nants]:
        jump(ant,0,50)
        ant.penup()
        ant.left(random.randint(1,360))
    bob.runningAnts = True
    screen.tracer(1)
    updateAnts()

def updateAnts():
    for ant in bob.ants[:bob.nants]:
        d = random.randint(1,100)
        if d<=5:
            ant.left(90)
        elif d<=10:
            ant.right(90)
        ant.forward(5)
        
        # only show if not insize coind
        if ant.distance((0,50))<110:
            ant.hideturtle()
        else:
            ant.showturtle()
            
    if bob.runningAnts:
        screen.ontimer(updateAnts, 15)
    else:
        for ant in ants:
            ant.hideturtle()

# game functions          
    
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

def beginner():
    if bob.level ==  "Beginner": return
    bob.level = "Beginner"
    bob.games = 0
    bob.wins = 0
    startGame()

def expert():
    if bob.level ==  "Expert": return
    bob.level = "Expert"
    bob.games = 0
    bob.wins = 0
    startGame()
    
def extreme():
    if bob.level ==  "Expert": return
    bob.level = "eXtreme"
    bob.games = 0
    bob.wins = 0
    startGame()
    
def playerMove(move):
    if bob.state != "human": return
    
    bob.coins = bob.coins - move
    bob.messages.append("You have taken %s coins" % move)
    bob.state = "computer"
    update()

def quit():
    screen.bye()
    sys.exit()

def restartGame():
    if bob.state!="end":
        bob.games = bob.games + 1
    startGame()

def computerMove():
    
    skill= {"Beginner":0.1, "Expert":0.5, "eXtreme":1.0}[bob.level]
    
    bob.runningAnts = False
    # fake think for a while ...
    bob.messages.append("Thinking ")
    drawScreen()
    for k in range(random.randint(0,1)):
        time.sleep(1)
        bob.messages[-1] = bob.messages[-1] + "."
        drawScreen(False)
    bob.messages = bob.messages[:-1] # delete last message in list 
    
    move = random.randint(1, min(3,bob.coins))
    bob.coins = bob.coins - move
    bob.messages.append("I'm going to take %s coins" % move)
    bob.state = "human"
    update()


def update():
    
    if bob.state!="start":
        bob.messages.append("Game has %s coins left." % bob.coins)
    
    # check for game over
    if bob.coins<=0:
        bob.games = bob.games + 1
        if bob.state == "computer":
            bob.wins = bob.wins + 1
            bob.messages.append("OK, OK you won")
        else:
            bob.messages.append("Look I won again!")
        bob.state = "end"
        bob.messages.append("\nPress 'r' to start a new game")
        drawScreen()
        return
    elif bob.state!="start" and bob.state=="human":
        bob.messages.append("How many coins will you take ?")
        startAnts()
    if bob.state == "computer":
        computerMove()
    
    drawScreen()
  
def drawScreen(update=True):
    
    screen.tracer(0)
    
    print (bob.state)
    
    if update: bob.reset()
    bob.penup()
    bob.speed("fastest")
    bob.hideturtle()
    
    # ttle 
    bob.goto(0,200)
    bob.write("Take Away", align="center", font=("Arial", 60))
    
    # coins
    jump(bob,0,-40)
    bob.width(5)
    bob.fillcolor("gray")
    bob.begin_fill()
    bob.circle(102)
    bob.end_fill()
    jump(bob,-5,-35)
    bob.fillcolor("white")
    bob.begin_fill()
    bob.circle(100)
    bob.end_fill()
    jump(bob,0,0)
    bob.write(bob.coins, align="center", font=("Arial", 100))
    
    # coins
    bob.penup()
    bob.goto(-300,-250)
    temp = "\n".join(bob.messages[-7:])
    bob.write(temp, align="left", font=("Arial", 20))
    
    # game level
    jump(bob,350, 350)
    bob.write(bob.level, align="right", font=("Arial", 20))
         
    # game history
    jump(bob,350, 300)
    score = "Played %s, won %s games." % (bob.games, bob.wins)
    bob.write(score, align="right", font=("Arial", 20))

    screen.tracer(1)

screen.onkey(startGame, "s")
screen.onkey(player_1, "1")
screen.onkey(player_2, "2")
screen.onkey(player_3, "3")
screen.onkey(player_No, "n")
screen.onkey(player_Yes, "y")
screen.onkey(quit, "q")
screen.onkey(restartGame, "r")

screen.onkey(beginner, "b")
screen.onkey(expert, "e")
screen.onkey(extreme, "x")


startGame()

screen.listen()
turtle.mainloop()


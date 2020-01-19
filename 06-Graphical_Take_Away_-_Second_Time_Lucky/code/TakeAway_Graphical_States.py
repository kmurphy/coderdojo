import turtle

screen = turtle.Screen()
bob = turtle.Turtle()
bob.state = "start"
  
def startGame():
    print ("Starting game.")
    print ("Do you want to play first (Y/N) ?")
    bob.state = "start"
    
def player_No():
    if bob.state == "start":
        print("Great! I will play first ...")
        bob.state = "computer"
    
def player_Yes():
    if bob.state == "start":
        print("OK, you can play first ...")
        bob.state = "human"

def player_1():
    print ("player_1 not done yet!")
def player_2():
    print ("player_2 not done yet!")
def player_3():
    print ("player_3 not done yet!")

screen.onkey(startGame, "s")
screen.onkey(player_1, "1")
screen.onkey(player_2, "2")
screen.onkey(player_3, "3")
screen.onkey(player_No, "n")
screen.onkey(player_Yes, "y")

screen.listen()


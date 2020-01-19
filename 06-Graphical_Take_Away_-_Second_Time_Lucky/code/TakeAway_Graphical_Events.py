import turtle

screen = turtle.Screen()
bob = turtle.Turtle()
  
def startGame():
    print ("startGame not done yet!")

def player_1():
    print ("player_1 not done yet!")
def player_2():
    print ("player_2 not done yet!")
def player_3():
    print ("player_3 not done yet!")
    
def player_No():
    print ("player_No not done yet!")
def player_Yes():
    print ("player_Yes not done yet!")
   
screen.onkey(startGame, "s")
screen.onkey(player_1, "1")
screen.onkey(player_2, "2")
screen.onkey(player_3, "3")
screen.onkey(player_No, "n")
screen.onkey(player_Yes, "y")

screen.listen()


# 1 - Import needed modules 


import turtle
import os, sys


# 2 - Create screen


background = "background_1.gif"

screen = turtle.Screen()
screen.addshape(background)
turtle.shape(background)

bob = turtle.Turtle()
bob.hideturtle()
bob.speed("fastest")


# 3 - Define helper functions


def jump(t, x, y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(0)

def drawButton(x=0 ,y=0, w=150,h=50, label="My Button",
        font=("Comic Sans", 40, "normal")):
    
    print ("Button `%s` Not done yet" % label)

    # draw label
    jump(bob, x,y)
    bob.write(label, align="center", font=font)

    # draw border
    for k in range(2):
        bob.forward(w)
        bob.left(90)
        bob.forward(h)
        bob.left(90)
        
    # save button information
    
    
# 4 - Build sceen


jump(bob,0,220)
bob.write("Welcome", align="center",
    font=("Comic Sans", 70, "normal"))

drawButton(y=100, label="Press Me")
drawButton(y=0, label="No Press Me")
drawButton(y=-100, label="Forget them, PRESS ME")

turtle.mainloop()





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

from collections import namedtuple
Button = namedtuple('Button', 'x y w h label')
bob.buttons = []

    
# 3 - Define helper functions


def jump(t, x, y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(0)


def drawRectangle(x=0, y=0, w=150, h=50, color="black", fill=None, pensize=2, shadow=True):
    
    if shadow:
        drawRectangle(x+3,y-3, w,h, "#666", shadow=False)
        drawRectangle(x+1,y-1, w,h, "#555", shadow=False)
            
    bob.color(color)
    bob.pensize(pensize)
    jump(bob, x,y)        
    if fill:
        bob.fillcolor(fill)
        bob.begin_fill()
    
    for k in range(2):
        bob.forward(w)
        bob.left(90)
        bob.forward(h)
        bob.left(90)
        
    if fill: bob.end_fill()
    
       
def drawButton(x=0 ,y=0, w=150,h=50, label="My Button",
        font=("Comic Sans", 40, "normal"), fill="yellow"):

    # draw border
    drawRectangle(x-w/2,y, w,h, fill=fill)
       
    # draw label
    jump(bob, x,y)
    bob.write(label, align="center", font=font)

    # save button information
    bob.buttons.append( Button(x,y,w,h, label) )


def onclick(mx,my):
        
    for b in bob.buttons:
        if (b.x-b.w/2 <= mx <= b.x+b.w/2) and (b.y<=my<=b.y+b.h):
                    
            print ("Button clicked =  %s " % b.label)
            break
    
# 4 - Build sceen


jump(bob,0,220)
bob.write("Welcome", align="center",
    font=("Comic Sans", 70, "normal"))

drawButton(y=100, w=175, label="Press Me")
drawButton(y=0,  w=250, label="No Press Me")
drawButton(y=-100,  w=450, label="Forget them, PRESS ME")

screen.onclick(onclick, btn=1)
screen.listen()
turtle.mainloop()










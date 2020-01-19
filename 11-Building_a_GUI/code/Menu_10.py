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
                       
            if b.label=="Take Away Game":
                os.system("python TakeAway_Graphical_Complete.py")
                
            elif b.label=="Color Spiral":
                os.system("python Color_Spiral.py")
                
            elif b.label=="Time to go home ...":
                print("Going home ... ")
                screen.bye()
                sys.exit(1)
            else:
                print ("Unknown button clicked = %s" % b.label)

            break
 
 
# 4 - Build sceen

screen.tracer(0)
jump(bob,0,220)
bob.write("Welcome", align="center",
    font=("Comic Sans", 70, "normal"))

jump(bob,-350,160)
bob.write("Games ...", align="left",
    font=("Comic Sans", 20, "normal"))

drawButton(y=100, w=350, label="Take Away Game")
drawButton(y=25, w=250, label="Monky Wars")

jump(bob,-350,-50)
bob.write("Turtle Graphics ...", align="left",
    font=("Comic Sans", 20, "normal"))

drawButton(x=-200, y=-100, w=240, label="Squares")
drawButton(x=50, y=-100, w=240, label="Color Spiral")
drawButton(x=250, y=-100, w=150, label="Chess")
drawButton(x=-200, y=-175, w=240, label="Face")
drawButton(x=50, y=-175, w=240, label="Party")

drawButton(x=-200, y=-310,  w=300, label="Time to go home ...",
        font=("Comic Sans", 30, "normal"),
        fill="red")

screen.onclick(onclick, btn=1)

screen.tracer(1)
screen.listen()
turtle.mainloop()












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
buttons = []


# 3 - Define helper functions


def jump(t, x, y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(0)


def drawButton(x=0 ,y=0,w=150,h=50, label="My Button",
        font=("Comic Sans", 40, "normal")):

    jump(bob, x,y)
    bob.write(label, align="center", font=font)
    
    jump(bob, x-w/2, y)
    for k in range(2):
        bob.forward(w)
        bob.left(90)
        bob.forward(h)
        bob.left(90)
    
    return Button(x,y,w,h, label)


def onClick(x,y):
    print ("click at ", x, y)
    for button in buttons:
        if abs(button.x-x)<=button.width//2 and abs(button.y-y)<=button.height//2:
            print ("Button clicked =  %s " % button.label)
            if button.label=="Take Away Game":
                os.system("python TakeAway_Graphical_Complete.py")
            elif button.label=="Time to go home ...":
                print("Going home ... ")
                screen.bye()
                sys.exit(1)


# 4 - Build sceen

jump(bob,0,220)
bob.write("Welcome", align="center", font=("Comic Sans", 70, "normal"))

drawButton(w=300,label="Hey Press me ")

drawButton(y=-200, w=300,label="Hey Press me ")



#buttons.append(drawButton(0,100, 320,50, "Take Away Game"))

#buttons.append(drawButton(0,0, 100,50, "Me"))

#buttons.append(drawButton(0,-200, 380,50, "Time to go home ..."))


# 5 - Events


screen.onclick(onClick,btn=1)

turtle.mainloop()

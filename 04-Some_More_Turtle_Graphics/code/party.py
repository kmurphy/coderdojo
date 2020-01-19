import turtle

bob = turtle.Turtle()
bob.speed("fastest")

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def draw_circle(radius, color="black", fillcolor=None):
    bob.color(color)
    if fillcolor!=None:
        bob.fillcolor(fillcolor)
        bob.begin_fill()
    bob.circle(radius)
    if fillcolor!=None:
        bob.end_fill()
        

def draw_face(x,y, scale):
    # face
    jump(x+0*scale, y-150*scale)
    draw_circle(200*scale, "yellow", "yellow")

    # eyes
    jump(x-60*scale, y+100*scale)
    draw_circle(15*scale, "black", "black")
    jump(x+60*scale, y+100*scale)
    draw_circle(15*scale, "black", "black")

    # mouth
    bob.width(15*scale)
    jump(x-70*scale, y+0*scale)
    bob.setheading(-50)
    bob.circle(100*scale,100)
    bob.hideturtle()

    bob.setheading(0)
    

screen = turtle.Screen()
screen.bgcolor("black")

import random
for f in range(100):
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    draw_face(x, y, 0.25)